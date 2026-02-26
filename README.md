# Open Data Policy App

## Intelligent Policy Summarization and Scenario Adaptation Platform

---

## 1. Project Overview

The Open Data Policy AI System is a full-stack AI-powered web application designed to summarize complex data governance policies and adapt them to different organizational contexts such as Universities, Startups, and NGOs.

The system demonstrates the practical application of Natural Language Processing (NLP) in policy analysis and automated decision-support systems.

---

## 2. Objectives

- Automate summarization of governance policies
- Adapt policies for different organizational scenarios
- Provide an intuitive user interface
- Implement scalable AI architecture

---

## 3. System Architecture

User Input (React Frontend)  
↓  
Flask REST API  
↓  
HuggingFace Transformer Models  
↓  
Generated Summary & Scenario Draft  
↓  
Displayed in Frontend

---

## 4. Technology Stack

Frontend:

- React.js
- CSS
- Fetch API

Backend:

- Python
- Flask
- Flask-CORS

AI Models:

- BART (facebook/bart-large-cnn) – Summarization
- GPT-2 – Draft Generation

---

## 5. Features

- Policy text input
- AI-powered summarization
- Scenario-based draft generation
- Copy & download options
- Reset & history
- Error handling
- Loading indicators

---

## 6. Installation Guide

### Clone Repository

git clone https://github.com/DilaknaH/open-data-policy-app.git  
cd open-data-policy-app

### Backend Setup

cd backend  
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
python app.py

### Frontend Setup

cd frontend  
npm install  
npm start

---

## 7. API Endpoints

POST /summarize  
POST /generate

---

## 8. Deployment

Backend → Render  
Frontend → Vercel

---

## 9. Limitations

- Output quality depends on input size
- GPT-2 may produce repetitive text
- No direct PDF upload support

---

## 10. Future Improvements

- PDF upload feature
- Database integration
- Improved prompt engineering
- Larger language models
- Full cloud deployment

---

## Author

Dilakna Godagamage  
Applied Data Science & Communication  
General Sir John Kotelawala Defence University
