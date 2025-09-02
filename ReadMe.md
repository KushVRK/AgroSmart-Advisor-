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