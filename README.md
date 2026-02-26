# Open Data Policy App

## Intelligent Policy Summarization and Scenario Adaptation Platform

---

## 1. Project Overview

The **Open Data Policy App** is a full-stack AI-powered web application designed to summarize complex data governance policies and adapt them to different organizational contexts such as Universities, Startups, and NGOs.

The application demonstrates the practical use of Natural Language Processing (NLP) in policy analysis and automated decision-support systems, while providing a structured two-panel dashboard interface aligned with academic requirements.

---

## 2. Objectives

- Automate summarization of governance policies
- Adapt policies for different organizational scenarios
- Maintain clear structural separation between summarization and scenario generation
- Provide an intuitive and professional Night Mode interface
- Implement scalable full-stack architecture

---

## 3. System Architecture

User Input (React Frontend)  
↓  
Flask REST API (Backend)  
↓  
HuggingFace Transformer Models  
↓  
Generated Summary & Scenario Draft  
↓  
Displayed in Frontend

---

## 4. Technology Stack

### Frontend

- React.js
- CSS (Night Mode theme – deep brown with orange accents)
- Fetch API

### Backend

- Python
- Flask
- Flask-CORS

### AI / NLP Models

- **BART (facebook/bart-large-cnn)** – Abstractive Summarization
- **GPT-2** – Scenario-based Text Generation
- HuggingFace Transformers Library

---

## 5. Application Layout (Updated Structure)

The application strictly follows the required two-panel layout:

### Left Panel – Policy Summarisation

- Policy text input (manual paste)
- AI-generated summary output
- Word count display
- Reset functionality
- Loading spinner

### Right Panel – Scenario-Based Policy Generation

- Scenario selection dropdown:
  - University
  - Startup
  - NGO
- Generate draft button
- Scenario-adapted policy output
- Collapsible session history
- Copy & download options

The interface supports **iteration**, allowing users to:

- Change scenarios
- Regenerate drafts
- Reset and reprocess new policies

---

## 6. Welcome Screen (UI Enhancements)

- Professional landing page
- Animated gradient background
- Italic tagline for visual emphasis
- Clean “Get Started” button
- Removed sparkle/glow hover animation for professional academic presentation

---

## 7. Project Structure

open-data-policy-app/
│── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── ...
│── frontend/
│ ├── src/
│ │ ├── App.js
│ │ ├── App.css
│ │ ├── components/
│ │ │ ├── PolicyUpload.js
│ │ │ ├── SummaryPanel.js
│ │ │ ├── ScenarioPanel.js
│ │ │ ├── HistoryPanel.js
│ │ │ └── WelcomeScreen.js
│ ├── package.json
│ └── ...
│── demo.mp4
└── README.md

---

## 8. Installation Guide

### Step 1 – Clone Repository

```bash
git clone https://github.com/DilaknaH/open-data-policy-app.git
cd open-data-policy-app
Step 2 – Backend Setup
cd backend
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run backend:

python app.py

Backend runs on:

http://localhost:5000
Step 3 – Frontend Setup

Open a new terminal:

cd frontend
npm install
npm start

Frontend runs on:

http://localhost:3000
9. API Endpoints
POST /summarize

Request

{
  "text": "policy content"
}

Response

{
  "summary": "Generated summary text"
}
POST /generate

Request

{
  "summary": "summarized text",
  "scenario": "University"
}

Response

{
  "draft": "Scenario adapted policy draft"
}
10. Demo

The included demo.mp4 demonstrates:

Welcome screen

Policy summarisation (Left Panel)

Scenario-based generation (Right Panel)

Iterative scenario switching

Download functionality

Reset feature

Session history

11. Limitations

Output quality depends on input length

GPT-2 may generate repetitive text

Manual policy input only (no PDF upload yet)

12. Future Improvements

Add PDF upload support

Integrate database for persistent history

Improve prompt engineering

Deploy fully online cloud version

Add authentication system

Enhance UI animations while maintaining academic professionalism

Author

Dilakna Godagamage
Applied Data Science & Communication
General Sir John Kotelawala Defence University
```
