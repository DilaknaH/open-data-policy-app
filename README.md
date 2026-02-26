# Open Data Policy App

## Intelligent Policy Summarization and Scenario-Based Policy Generation Platform

---

## 1. Project Overview

The **Open Data Policy App** is a full-stack AI-powered web application designed to:

- Summarize complex open data governance policies
- Adapt summarized policies to different organizational contexts

The system demonstrates practical implementation of **Natural Language Processing (NLP)** within a structured full-stack architecture using React and Flask.

The interface follows a clean dual-panel structure:

- **Left Panel → Policy Summarisation**
- **Right Panel → Scenario-Based Policy Generation**

This design strictly follows the assignment requirement for structural clarity and iterative interaction.

---

## 2. Objectives

- Automate summarization of governance policies
- Enable scenario-based policy adaptation
- Provide structured two-panel layout as specified
- Support iterative regeneration of outputs
- Demonstrate integration of frontend, backend, and NLP models

---

## 3. System Architecture

User Input (React Frontend)  
↓  
Flask REST API (Backend)  
↓  
HuggingFace Transformer Models  
↓  
Generated Summary  
↓  
Scenario-Based Policy Draft  
↓  
Displayed in Structured Dual Panels

---

## 4. Technology Stack

### Frontend

- React.js
- CSS (Night Mode Theme – Deep Brown + Orange Accent)
- Fetch API

### Backend

- Python
- Flask
- Flask-CORS

### AI / NLP Models

- **BART (facebook/bart-large-cnn)** – Abstractive Summarization
- **GPT-2** – Scenario-Based Policy Draft Generation
- HuggingFace Transformers Library

---

## 5. Application Structure (UI Layout)

### Left Panel – Policy Summarisation

- Policy text input
- Word counter
- Summarize button
- AI-generated summary output
- Reset functionality

### Right Panel – Scenario-Based Policy Generation

- Scenario selection dropdown
- Generate draft button
- Generated scenario-specific draft
- Collapsible session history panel

The system supports iteration:

- Users can change scenarios
- Outputs regenerate dynamically
- History is tracked per session

---

## 6. Welcome Screen Design

The application includes a professional landing page with:

- Project title
- Tagline (italic styled)
- Feature highlights
- Clean "Get Started" button
- Subtle animated gradient background
- No hover sparkle effect (removed for professional polish)

---

## 7. Project Structure

```

open-data-policy-app/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── ...
│
├── frontend/
│ ├── src/
│ │ ├── App.js # Main layout & state management
│ │ ├── App.css # Styling (Night Mode + Welcome Screen)
│ │ ├── components/
│ │ │ ├── PolicyUpload.js
│ │ │ ├── SummaryPanel.js
│ │ │ ├── ScenarioPanel.js
│ │ │ └── HistoryPanel.js
│ │ └── ...
│ ├── package.json
│ └── ...
│
├── demo.mp4
└── README.md

```

---

## 8. Installation Guide

### Step 1 – Clone Repository

```bash
git clone https://github.com/DilaknaH/open-data-policy-app.git
cd open-data-policy-app
```

---

### Step 2 – Backend Setup

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

Run backend:

```bash
python app.py
```

Backend runs on:

```
http://localhost:5000
```

---

### Step 3 – Frontend Setup

Open a new terminal:

```bash
cd frontend
npm install
npm start
```

Frontend runs on:

```
http://localhost:3000
```

---

## 9. API Endpoints

### POST /summarize

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

### POST /generate

**Request**

```json
{
  "summary": "summarized text",
  "scenario": "University"
}
```

**Response**

```json
{
  "draft": "Scenario adapted policy draft"
}
```

---

## 10. Key Features

- Structured two-panel layout (requirement-aligned)
- AI-powered policy summarization
- Scenario-based policy generation
- Dynamic regeneration capability
- Loading indicators
- Copy to clipboard
- Download generated draft
- Reset functionality
- Session history tracking
- Professional welcome interface

---

## 11. Limitations

- GPT-2 may occasionally generate repetitive content
- No PDF upload support (text input only)
- Session history is not persisted in a database

---

## 12. Future Improvements

- PDF document upload
- Database integration for persistent history
- Model fine-tuning for domain-specific policies
- Cloud deployment
- Authentication system
- UI enhancement with structured export formatting

---

## 13. Demonstration

The included `demo.mp4` demonstrates:

- Welcome screen
- Policy input
- AI summarization
- Scenario selection
- Draft regeneration
- History tracking
- Reset functionality

---

## Author

**Dilakna Godagamage**

BSc (Hons) Applied Data Science & Communication,
General Sir John Kotelawala Defence University
