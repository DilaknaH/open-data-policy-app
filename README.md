# Open Data Policy App

## Intelligent Policy Summarization & Scenario-Based Policy Adaptation Platform

---

## 1. Project Overview

The **Open Data Policy App** is a full-stack AI-powered web application designed to:

- Summarize complex open data governance policies
- Adapt summarized policies to multiple organizational contexts
- Allow direct **file upload for policy processing**
- Demonstrate real-world NLP integration within a structured full-stack system

The system implements **Natural Language Processing (NLP)** using transformer-based models and follows a clean dual-panel architecture:

- **Left Panel → Policy Summarisation**
- **Right Panel → Scenario-Based Policy Generation**

The application now supports both:

- Manual text input
- File upload (policy documents)

All components run on a **single Flask server**, serving both backend API and React frontend.

---

## 2. Objectives

- Automate summarization of governance and regulatory documents
- Enable scenario-based adaptation of a single policy into multiple contexts
- Provide structured two-panel academic layout
- Support file-based document processing
- Demonstrate practical integration of AI models within a deployable architecture

---

## 3. Scenario Definitions

The system adapts the same summarized policy into three realistic organizational contexts. This demonstrates how governance frameworks shift based on institutional priorities.

---

### 1️⃣ Research Universities

**Target Context:** Academic institutions and research bodies

**Focus Areas:**

- Research transparency and open access publishing
- Ethical handling of research datasets
- Student and faculty data privacy
- Compliance with institutional review boards (IRBs)
- Secure sharing of datasets for academic collaboration

**Priority Shift:**
Emphasis on **academic integrity, ethical research governance, and controlled data dissemination**.

---

### 2️⃣ Startups & Technology Companies

**Target Context:** Innovation-driven private sector organizations

**Focus Areas:**

- Regulatory compliance and data protection laws
- Secure API-based data sharing
- Product innovation using open datasets
- Intellectual property considerations
- Cybersecurity and risk management

**Priority Shift:**
Emphasis on **innovation, scalability, commercial sustainability, and secure data utilization**.

---

### 3️⃣ NGOs & Social Impact Organizations

**Target Context:** Non-profit and humanitarian organizations

**Focus Areas:**

- Donor transparency and reporting
- Beneficiary data protection
- Ethical data collection in vulnerable communities
- Community accountability
- Responsible use of open data for advocacy

**Priority Shift:**
Emphasis on **trust, ethical responsibility, and social accountability**.

---

## 4. System Architecture

User Input / File Upload (React Frontend)
↓
Flask REST API (Backend)
↓
HuggingFace Transformer Models
↓
Generated Summary
↓
Scenario-Based Policy Draft
↓
Displayed in Dual Panel Interface

---

## 5. Technology Stack

### Frontend

- React.js
- CSS (Professional Night Mode Theme)
- Fetch API

### Backend

- Python
- Flask
- Flask-CORS

### AI / NLP Models

- **Hugging Face Transformers Library**
- **Facebook AI BART (facebook/bart-large-cnn)** – Abstractive Summarization
- **OpenAI GPT-2** – Scenario-Based Draft Generation

---

## 6. Key Features

- Dual-panel structured academic layout
- AI-powered policy summarization
- Scenario-based policy drafting
- **New: File upload support for policy documents**
- Dynamic draft regeneration
- Word counter
- Copy-to-clipboard functionality
- Download generated draft
- Reset functionality
- Collapsible session history
- Professional landing page
- Single-server deployment (Flask serves frontend + backend)

---

## 7. Application Structure

```
open-data-policy-app/
│
├── backend/
│   ├── app.py                # Combined backend + frontend server
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── components/
│   │   │   ├── PolicyUpload.js     # File upload component
│   │   │   ├── SummaryPanel.js
│   │   │   ├── ScenarioPanel.js
│   │   │   ├── HistoryPanel.js
│   │   │   └── ...
│   │   └── ...
│   └── package.json
│
├── Policy_Sample/            # Sample policy documents for testing
│   ├── sample_policy.txt
│
├── demo.mp4
└── README.md
```

> Frontend build is served directly through Flask.
> No separate `npm start` required after build.

---

## 8. Installation & Run Guide

### Clone Repository

```bash
git clone https://github.com/DilaknaH/open-data-policy-app.git
cd open-data-policy-app
```

---

### Backend Setup

```bash
cd backend
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

## 9. API Endpoints

### POST `/summarize`

**Request**

```json
{
  "text": "policy content"
}
```

**Response**

```json
{
  "summary": "Generated summary text"
}
```

---

### POST `/generate`

**Request**

```json
{
  "summary": "summarized text",
  "scenario": "Research University"
}
```

**Response**

```json
{
  "draft": "Scenario adapted policy draft"
}
```

---

## 10. Academic & Practical Contribution

This project demonstrates:

- Practical NLP implementation
- Transformer-based summarization
- Controlled generative adaptation
- Full-stack integration (React + Flask)
- Scenario-aware policy transformation
- Single-server production deployment

It serves as both:

- A portfolio-ready AI system
- A foundation for future research in governance-aware NLP systems

---

## 11. Limitations

- GPT-2 may generate occasional repetition
- File upload currently supports text-based documents only
- No database persistence for history
- No user authentication system

---

## 12. Future Improvements

- PDF & DOCX structured parsing
- Database integration (persistent history)
- Fine-tuned domain-specific model
- Cloud deployment
- Role-based access control
- Structured export formatting (PDF reports)

---

## 13. Author

**Dilakna Godagamage**
BSc (Hons) Applied Data Science & Communication
General Sir John Kotelawala Defence University

---
