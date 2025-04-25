#  Web Research Report Generator

## OverView

This is a Flask-based web application that takes a user's query, processes it using a custom research agent, and generates a clean, well-formatted report. The report is rendered using Markdown and styled with CSS for better readability.

---
## Agent FlowChart

User Query → Web Search API → Get URLs → Crawl & Scrape Content → Filter & Extract Relevant Info → Summarize & Structure → Final Report

##  Features

- Input a query to generate a research report.
- Markdown support for formatted report rendering.
- Clean and responsive HTML + CSS frontend.
- Lightweight and easy to deploy.
- Easily extendable with AI models or data sources.

---

##  Preview

![App Preview](static/preview.png)  
<sub>*Example: Terror attack summary query rendered as a formatted report.*</sub>

---

## Requirements

- **Flask**
- **fpdf**
- **gemini-1.5-pro**
- **requests**
- **beautifulsoup4**
- **python-dotenv**
- **markdown**

  ---

##  Project Structure

```
research-report-app/
│
├── app.py                  # Main Flask server
├── research_agent.py       # Your logic to generate reports
├── templates/
│   └── index.html          # HTML template for UI
├── static/
│   └── style.css           # CSS for styling
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---
##  Installation

```bash
git clone https://github.com/your-username/research-report-app.git
cd research-report-app
pip install -r requirements.txt
```

Flask
markdown
```

---
##  Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## Output


       Link: https://github.com/user-attachments/assets/37d627c1-b48d-478b-9f12-62ea0a4c1a68


##  Example Usage

1. Enter a query like:
   ```
   "Pahalgam terror attack 2025"
   2. Click **Generate Report**.

3. See a formatted summary with:
   - Executive Summary
   - Incident Details
   - Government Response
   - Public Reaction
   - Casualties
   - Sources

---
## Render Depolyment 

Link:  https://web-research-4.onrender.com/

##  Credits
Created by  https://github.com/Jayaram976
Feel free to fork, improve, and share 

---
