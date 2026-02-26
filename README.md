# Open Data Policy App

## Intelligent Policy Summarization and Scenario Adaptation Platform

---

## 1. Project Overview

The Open Data Policy App is a full-stack AI-powered web application designed to summarize complex data governance policies and adapt them to different organizational contexts such as Universities, Startups, and NGOs.

The application demonstrates the practical use of Natural Language Processing (NLP) in policy analysis and automated decision-support systems.

---

## 2. Objectives

- Automate summarization of governance policies
- Adapt policies for different organizational scenarios
- Provide an intuitive and user-friendly interface
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
- CSS
- Fetch API

### Backend

- Python
- Flask
- Flask-CORS

### AI / NLP Models

- BART (facebook/bart-large-cnn) – Abstractive Summarization
- GPT-2 – Scenario-based Text Generation
- HuggingFace Transformers Library

---

## 5. Features

- Policy text input (manual paste)
- AI-powered summarization
- Scenario-based draft generation:
  - University
  - Startup
  - NGO
- Copy to clipboard
- Download generated output
- Reset functionality
- Loading spinner indicators
- Error handling

---

## 6. Project Structure

open-data-policy-app/

│── backend/  
│ ├── app.py  
│ ├── requirements.txt  
│ └── ...

│── frontend/  
│ ├── src/  
│ ├── package.json  
│ └── ...

│── demo.mp4  
└── README.md

---

## 7. Installation Guide

### Step 1 – Clone Repository

git clone https://github.com/DilaknaH/open-data-policy-app.git  
cd open-data-policy-app

---

### Step 2 – Backend Setup

cd backend  
python -m venv venv

Activate environment:

Windows:  
venv\Scripts\activate

Mac/Linux:  
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run backend:

python app.py

Backend runs on:
http://localhost:5000

---

### Step 3 – Frontend Setup

Open a new terminal:

cd frontend  
npm install  
npm start

Frontend runs on:
http://localhost:3000

---

## 8. API Endpoints

### POST /summarize

Request:
{
"text": "policy content"
}

Response:
{
"summary": "Generated summary text"
}

---

### POST /generate

Request:
{
"summary": "summarized text",
"scenario": "University"
}

Response:
{
"draft": "Scenario adapted policy draft"
}

---

## 9. Deployment Options

### Cloud Deployment

Backend → Render / Heroku / Azure  
Frontend → Vercel / Netlify

### Docker Deployment

Use Dockerfile and docker-compose for containerized execution.

### Local Start Script

Create a start.bat file to run backend and frontend together.

---

## 10. Demo

A demonstration video (demo.mp4) is included showing:

- Policy input
- AI summarization
- Scenario selection
- Generation of different drafts
- Download functionality
- Reset feature

---

## 11. Limitations

- Output quality depends on input length
- GPT-2 may generate repetitive text
- Manual policy input (no PDF upload yet)

---

## 12. Future Improvements

- Add PDF upload support
- Integrate database for history tracking
- Improve prompt engineering
- Deploy fully online cloud version
- Add authentication system

---

## Author

Dilakna Godagamage  
Applied Data Science & Communication  
General Sir John Kotelawala Defence University
