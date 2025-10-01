# ai_todo.py
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
import json
import re
import argparse
from datetime import datetime, timedelta
import openai
from rich import print, pretty

pretty.install()

# Load API key from env
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise SystemExit("Set OPENAI_API_KEY in your environment before running.")

SYSTEM_INSTRUCTIONS = """
You are a JSON generator. Convert the user's plain-language project description
into a JSON array of task objects. **Return only valid JSON** (no explanatory text).
Each task object must have these fields:
 - title: short string
 - description: one-sentence explanation
 - due_date: YYYY-MM-DD (if no explicit due date, place within next 14 days)
 - priority: one of "low", "medium", "high"
 - estimate_minutes: integer (reasonable estimate)
 - tags: array of short strings (max 4)
Produce between 3 and 12 tasks, organized for a reasonable, actionable plan.
"""

PROMPT_TEMPLATE = """
User description:
\"\"\"
{desc}
\"\"\"
Return the JSON array now.
"""

def extract_json(text):
    # extract first JSON array in text
    start = text.find('[')
    end = text.rfind(']')
    if start == -1 or end == -1:
        return None
    return text[start:end+1]

def ask_ai_to_make_tasks(description):
    messages = [
        {"role": "system", "content": SYSTEM_INSTRUCTIONS},
        {"role": "user", "content": PROMPT_TEMPLATE.format(desc=description)}
    ]
    resp = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.2,
        max_tokens=700
    )
    raw = resp.choices[0].message.content
    jtext = extract_json(raw)
    if not jtext:
        # fallback: just return raw (will error later)
        jtext = raw
    try:
        tasks = json.loads(jtext)
        return tasks
    except Exception as e:
        print("[red]Failed to parse JSON from AI. Raw output below:[/red]")
        print(raw)
        raise

def pretty_print_tasks(tasks):
    print("\n[bold underline]Generated Tasks[/bold underline]\n")
    for i, t in enumerate(tasks, 1):
        due = t.get("due_date", "n/a")
        print(f"[bold]{i}. {t.get('title')}[/bold] — {t.get('description')}")
        print(f"    due: {due} • priority: {t.get('priority')} • estimate: {t.get('estimate_minutes')}m • tags: {', '.join(t.get('tags',[]))}\n")

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
    print(f"[green]Saved tasks to {filename}[/green]")

def main():
    ap = argparse.ArgumentParser(description="AI TODO generator")
    ap.add_argument("description", nargs="+", help="Project description in plain English (wrap in quotes)")
    ap.add_argument("--out", "-o", default="tasks.json", help="Output JSON filename")
    args = ap.parse_args()
    desc = " ".join(args.description)

    tasks = ask_ai_to_make_tasks(desc)
    pretty_print_tasks(tasks)
    save_tasks(tasks, args.out)

if __name__ == "__main__":
    main()
