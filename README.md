📌 Project Idea

AgroSmart Advisor is a data-driven platform to help farmers make smarter crop choices.
It combines soil data, market prices, and weather forecasts to suggest crops that are both suitable and profitable.

🚀 Progress — Week 1

In Phase 1 & Phase 2, the following steps were completed:

Project Setup

Organized folders: data/raw, data/interim, data/processed, models, app

Created virtual environment (.venv) for package management.

Dataset Collection & Cleaning

Imported Kaggle Crop Recommendation dataset and performed basic cleaning.

Imported AgmarkNet commodity price dataset, renamed columns, converted date format, created month feature.

Feature Engineering

Generated monthly median prices per state and commodity.

Added 3-month moving averages and 12-month median baseline indicators.

Weather Integration

Connected to OpenWeather API (tested 5-day forecast).

Saved forecast to data/raw/weather.json.

Model Training (MVP)

Trained crop suitability models (RandomForest, one-vs-rest per crop).

Trained demand model (LightGBM using commodity price trends).

Saved trained models to models/.

Streamlit App (Initial Draft)

Created app/app.py for simple MVP interface.

Currently shows placeholder prediction results.

📂 Repository Structure
AgroSmart-Advisor/
│
├── app/                   # Streamlit app
│   └── app.py
│
├── data/
│   ├── raw/               # Raw datasets (Kaggle, AgmarkNet, Weather API)
│   ├── interim/           # Cleaned datasets
│   └── processed/         # Processed datasets (features, trends)
│
├── models/                # Trained ML models
│
├── notebooks/             # Jupyter notebooks (experiments)
│
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

🛠️ Tech Stack

Python 3.9+

Libraries: pandas, scikit-learn, LightGBM, joblib, requests, Streamlit

APIs: OpenWeather (forecast data)

Tools: GitHub, VS Code, Jupyter Notebook

✅ Next Steps (Week 2 Plan)

Improve data cleaning (remove invalid values like negative rainfall).

Add richer weather features (temperature/humidity averages, rainfall).

Build better Streamlit UI for farmers (crop & price recommendations).

Test models with more states and crops.

✍️ Author: Kushal V R
📅 Week 1 Milestone Completed
