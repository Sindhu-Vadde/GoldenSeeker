# 🏆 GoldenSeeker
### *"Finding your golden opportunity in a chaotic job market"*

---

## What Is GoldenSeeker

GoldenSeeker is an AI-powered job market intelligence platform that collects real job postings, extracts skills using NLP and ML, predicts salary ranges, and matches your CV against thousands of real jobs — showing you exactly where you stand in the market and what to learn next.

---

## Features

- 📊 **Market Intelligence Dashboard** — live skills demand, salary ranges, location trends across thousands of real job postings
- 📄 **CV Match Analyser** — upload your CV and get a match percentage against real job descriptions
- 🎯 **Skills Gap Report** — missing skills ranked by how often they appear in your target roles
- 💰 **Salary Predictor** — predict salary range from any job description
- 🔍 **Semantic Job Search** — search jobs by meaning not just keywords
- 📈 **Demand Forecasting** — which skills are growing or declining

---

## Tech Stack

| Category | Tools |
|---|---|
| Data Collection | requests, beautifulsoup4, pdfplumber |
| Data Processing | pandas, numpy, PostgreSQL, SQLAlchemy |
| Data Validation | Great Expectations |
| NLP | spaCy, HuggingFace Transformers, sentence-transformers |
| Machine Learning | scikit-learn, XGBoost, Optuna |
| Explainability | SHAP |
| Experiment Tracking | MLflow |
| Monitoring | Evidently AI |
| API | FastAPI, Pydantic, uvicorn |
| UI | Streamlit, Plotly |
| Testing | pytest |
| Containerisation | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Deployment | Hugging Face Spaces |

---

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/yourusername/goldenseeker.git
cd goldenseeker

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Create your .env file
Create a file called .env in the root folder and add your own values:
DB_NAME=goldenseeker
DB_USER=postgres
DB_PASSWORD=your_own_password_here
DB_HOST=localhost
DB_PORT=5432

### 5. Download the dataset
Download the job postings dataset from Kaggle and place in data/raw/jobs.csv

### 6. Run the application
streamlit run ui/app.py

---

## Dataset

This project uses the Job Postings Dataset from Kaggle.
Download and place in data/raw/jobs.csv

---

## Author
Sindhu Vadde — LinkedIn — GitHub