# Open Data Policy App

## Intelligent Policy Summarization & Scenario-Based Policy Adaptation Platform

---

# 1. Project Overview

The **Open Data Policy App** is a full-stack AI-powered web application designed to intelligently process complex governance and regulatory documents.

The system performs two core tasks:

- Abstractive policy summarization
- Scenario-based policy transformation

It allows:

- Manual text input
- Direct file upload (text-based documents)
- Real-time AI-driven draft generation
- Structured academic dual-panel interaction

The application runs on a **single Flask server**, serving both backend APIs and the React frontend.

---

# 2. System Purpose

Modern governance documents are lengthy, technical, and difficult to adapt across institutions.

This platform demonstrates how transformer-based NLP models can:

- Extract structured summaries from complex policies
- Adapt a single governance framework into multiple organizational contexts
- Maintain structural consistency across generated outputs
- Reduce repetition and incomplete generation issues through controlled prompt design

---

# 3. Core Functional Design

The interface follows a structured dual-panel architecture:

LEFT PANEL
→ Policy Summarisation

RIGHT PANEL
→ Scenario-Based Policy Generation

Processing Flow:

User Input / File Upload
↓
Flask REST API
↓
Transformer Models (Summarization + Generation)
↓
Structured Summary
↓
Scenario-Specific Policy Draft
↓
Rendered in UI

---

# 4. Scenario Adaptation Framework

The system transforms one summarized policy into three differentiated institutional contexts.

---

## 1️⃣ Research Universities

Target Context: Academic institutions

Strategic Focus:

- Research governance frameworks
- Ethical review compliance
- Institutional data protection standards
- Academic transparency
- Controlled scholarly data dissemination

Priority Emphasis:
Academic integrity, structured oversight, and responsible research data management.

---

## 2️⃣ Startups & Technology Companies

Target Context: Innovation-driven private sector entities

Strategic Focus:

- Regulatory compliance
- Scalable AI adoption
- Secure API and data exchange
- Intellectual property governance
- Cybersecurity integration

Priority Emphasis:
Commercial sustainability, innovation enablement, and regulatory risk mitigation.

---

## 3️⃣ NGOs & Social Impact Organizations

Target Context: Non-profit and humanitarian bodies

Strategic Focus:

- Donor accountability
- Ethical data collection in vulnerable communities
- Beneficiary privacy safeguards
- Transparent reporting frameworks
- Responsible data advocacy

Priority Emphasis:
Trust, ethical responsibility, and community-centered governance.

---

# 5. AI Architecture

The system integrates transformer-based NLP models:

- **facebook/bart-large-cnn**
  → Abstractive summarization

- **GPT-2 (controlled generation)**
  → Scenario-based structured policy drafting

Improvements implemented:

- Repetition control
- Structured section-based generation
- Length stabilization
- Prompt refinement for differentiated outputs
- Faster inference configuration

---

# 6. Technology Stack

Frontend

- React.js
- CSS (Professional Night Mode Theme)
- Fetch API

Backend

- Python
- Flask
- Flask-CORS

AI Layer

- Hugging Face Transformers
- PyTorch

Deployment

- Single-server architecture (Flask serves frontend build + APIs)

---

# 7. Key Features

- Dual-panel academic layout
- AI-powered policy summarization
- Scenario-based adaptive drafting
- File upload support (text documents)
- Dynamic regeneration
- Copy-to-clipboard
- Download draft functionality
- Word counter
- Reset system
- Session history panel
- Single-server deployment

---

# 8. Application Structure

```
open-data-policy-app/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── components/
│   │   │   ├── PolicyUpload.js
│   │   │   ├── SummaryPanel.js
│   │   │   ├── ScenarioPanel.js
│   │   │   ├── HistoryPanel.js
│   │   │   └── ...
│   └── package.json
│
├── Policy_Sample/
│   ├── sample_policy.pdf
│   └── ...
│
├── demo.mp4
└── README.md

```

Frontend production build is served directly through Flask.

---

# 9. Installation & Run Guide

Clone repository:

```bash
git clone https://github.com/DilaknaH/open-data-policy-app.git
cd open-data-policy-app
```

Backend setup:

```bash
cd backend
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
python app.py
```

Access:

```
http://localhost:5000
```

---

# 10. API Endpoints

POST `/summarize`

Request:

```json
{
  "text": "policy content"
}
```

Response:

```json
{
  "summary": "Generated summary"
}
```

---

POST `/generate`

Request:

```json
{
  "summary": "summarized text",
  "scenario": "Research University"
}
```

Response:

```json
{
  "draft": "Scenario-adapted policy draft"
}
```

---

# 11. Academic & Practical Contribution

This system demonstrates:

- Applied transformer-based NLP
- Scenario-aware controlled generation
- Governance-focused AI modeling
- Full-stack AI system deployment
- Structured prompt engineering for policy adaptation

It serves as:

- A portfolio-ready AI system
- A research foundation for governance-aware NLP systems
- A scalable base for domain-specific model fine-tuning

---

# 12. Current Limitations

- GPT-2 is not fine-tuned on governance-specific corpora
- Only text-based file upload supported
- No persistent database storage
- No authentication or user roles

---

# 13. Future Improvements

- PDF & DOCX structured parsing
- Fine-tuned governance language model
- Database integration
- Role-based access control
- Policy comparison engine
- Structured PDF export reports
- Cloud deployment

---

# 14. Author

Dilakna Godagamage
BSc (Hons) Applied Data Science & Communication
General Sir John Kotelawala Defence University

---
