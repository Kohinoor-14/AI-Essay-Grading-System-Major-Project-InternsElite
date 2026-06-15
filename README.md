# 📄 AI Essay Grading & Visualization System

## Overview

The AI Essay Grading & Visualization System is an intelligent web-based application developed using Natural Language Processing (NLP), Machine Learning, Data Analytics, and Data Visualization techniques. The system automatically evaluates essays based on multiple linguistic and semantic parameters and generates detailed performance reports.

The project aims to reduce the manual effort involved in essay evaluation while providing consistent, objective, and data-driven feedback to students.

---

## Features

### Essay Evaluation

* Automated essay grading
* Grammar analysis
* Vocabulary analysis
* Readability analysis
* Topic relevance analysis
* ML-based score prediction
* Final composite score generation

### Plagiarism Detection

* Checks similarity with previously submitted essays
* Calculates plagiarism percentage
* Promotes originality in submissions

### Data Visualization

* Performance Radar Chart
* Student Performance Dashboard
* Score Distribution Analysis
* Historical Performance Tracking

### Report Generation

* Professional PDF Report
* KIIT branded report layout
* Student information summary
* Score breakdown table
* Grade generation
* AI-generated feedback

### Database Management

* SQLite database integration
* Student history storage
* Previous evaluation retrieval
* Analytics generation

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* Scikit-learn
* Linear Regression

### Natural Language Processing

* NLTK
* TextBlob

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Plotly
* Matplotlib
* Seaborn

### Database

* SQLite

### Report Generation

* ReportLab

---

## Project Architecture

Essay Input
↓
Text Preprocessing
↓
Grammar Analysis
↓
Vocabulary Analysis
↓
Readability Analysis
↓
Topic Relevance Analysis
↓
Machine Learning Score Prediction
↓
Plagiarism Detection
↓
Final Score Generation
↓
Database Storage
↓
Visualization Dashboard
↓
PDF Report Generation

---

## Folder Structure

```text
Essay Grading System
│
├── assets/
│   └── logo.png
│
├── data/
│   └── essay_dataset.csv
│
├── database/
│   └── essays.db
│
├── models/
│   └── essay_model.pkl
│
├── reports/
│
├── src/
│   ├── essay_analyzer.py
│   ├── database_manager.py
│   ├── report_generator.py
│   ├── radar_chart.py
│   ├── plagiarism.py
│   ├── semantic_analyzer.py
│   └── ml_model.py
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd Essay-Grading-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Project

### Train ML Model

```bash
python train_model.py
```

### Start Application

```bash
streamlit run app.py
```

Application will launch at:

```text
http://localhost:8501
```

---

## Sample Evaluation Parameters

The system evaluates essays based on:

| Parameter         | Description                        |
| ----------------- | ---------------------------------- |
| Grammar Score     | Measures grammatical quality       |
| Vocabulary Score  | Measures vocabulary richness       |
| Readability Score | Measures ease of reading           |
| Topic Relevance   | Measures similarity to essay topic |
| ML Score          | Machine Learning predicted score   |
| Plagiarism Score  | Similarity with previous essays    |
| Overall Score     | Final composite score              |

---

## Sample Output

* AI Generated Score
* Grade Assignment
* Radar Chart Visualization
* Analytics Dashboard
* Student History Tracking
* PDF Evaluation Report

---

## Future Scope

* Deep Learning-based Essay Evaluation
* BERT/Sentence Transformer Models
* Multi-language Essay Assessment
* Cloud Deployment
* Teacher Portal
* Student Login System
* Advanced Plagiarism Detection

---

## Author

**Kohinoor Soni**

B.Tech Computer Science Engineering

KIIT University

---

## License

This project is developed for educational and academic purposes.
