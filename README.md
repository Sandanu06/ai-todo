
# ✅ AI-Powered Task Generator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://platform.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🚀 *AI-powered Python tool that transforms plain-English project ideas into structured, actionable to-do lists with due dates, priorities, and tags — all in seconds.*

---

## ✨ About the Project
This is a **10-minute intermediate Python project** that leverages AI to generate a fully organized **to-do list** from a simple text description.  

Instead of manually writing tasks, just describe your project — *“Build a landing page and launch a social media campaign in 2 weeks”* — and the script will return a structured list of tasks in **JSON format** with:
- 📌 Titles  
- 📝 Descriptions  
- ⏳ Estimated effort  
- 📅 Due dates  
- 🔖 Tags  
- 🚦 Priority levels  

It’s perfect for developers, students, and creators who want to **boost productivity with AI**.

---

## 🔥 Features
- 🧠 AI-powered task breakdown (via OpenAI API).  
- 🗂 Generates clean **JSON** task files for reuse.  
- 🎨 Beautiful CLI output with [Rich](https://github.com/Textualize/rich).  
- 📅 Automatic due dates (within 14 days if not specified).  
- ⚡ Run in less than 10 minutes.  

---

## 🚀 Quick Start

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/Sandanu06/ai-todo.git
cd ai-todo
````

### 2️⃣ Create Virtual Environment & Install

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate.ps1  # Windows PowerShell

pip install -r requirements.txt
```

### 3️⃣ Set OpenAI API Key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=sk-xxxxxx
```

### 4️⃣ Run the Script

```bash
python ai_todo.py "Launch a landing page and social media campaign within 2 weeks"
```

Example output:

```
1. Setup Landing Page — Create basic HTML/CSS/JS layout
   due: 2025-10-14 • priority: high • estimate: 120m • tags: web,frontend

2. Configure Analytics — Add Google Analytics tracking
   due: 2025-10-15 • priority: medium • estimate: 60m • tags: analytics,tracking
```

And a `tasks.json` file will be saved automatically ✅

---

## 📂 Project Structure

```
.
├── ai_todo.py        # Main script
├── requirements.txt  # Dependencies
├── .env.example      # API key template
└── README.md         # Project docs
```

---

## 🌱 Next Steps

* 📆 Export tasks as `.ics` calendar events
* 🖥️ Build a [Streamlit](https://streamlit.io/) web UI
* 📲 Integrate with Notion / Todoist APIs
* 🗄️ Add SQLite for persistent task management

---

## 🛠️ Built With

* [Python](https://www.python.org/)
* [OpenAI API](https://platform.openai.com/)
* [Rich](https://github.com/Textualize/rich)
* [dotenv](https://pypi.org/project/python-dotenv/)

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

### ⭐ If you like this project, give it a star on GitHub and share it!

```
