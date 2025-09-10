🌾 AgroSmart Advisor

AgroSmart Advisor is an intelligent crop recommendation system that helps farmers decide which crops to grow based on soil nutrients, weather, season, and market prices. It provides top crop recommendations along with expected profitability, while also highlighting crops to avoid.

🚀 Features

Accepts farmer inputs: NPK values, soil pH, temperature, humidity, rainfall, season, and month.

Recommends top crops with suitability score + expected price per kg.

Highlights crops to avoid in current conditions.

Season-aware recommendations (Kharif, Rabi, Zaid, Monsoon).

Interactive web app built with Streamlit.

Simple and farmer-friendly interface.

🖥️ Tech Stack

Python 3.10+

Streamlit – web interface

Scikit-learn – ML models

Pandas / NumPy – data processing

Matplotlib / Seaborn – visualizations

📂 Project Structure
AgroSmart-Advisor/
│── app.py                        # Main Streamlit app
│── phase6_prediction_pipeline.py # Crop prediction logic
│── models/                       # Saved ML models (.pkl) [not tracked in Git]
│── data/                         # Dataset files [not tracked in Git]
│── requirements.txt              # Python dependencies
│── README.md                     # Project documentation

⚙️ Setup Instructions

Clone this repository:

git clone https://github.com/KushVRK/AgroSmart-Advisor-.git
cd AgroSmart-Advisor-


Create a virtual environment:

python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate # On Mac/Linux


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py


Open your browser at:

http://localhost:8503/

🌱 Indian Crop Seasons

To help farmers choose the correct season input:

Kharif (June – October) 🌧️

Crops: Rice, Maize, Cotton, Soybean, Groundnut, Bajra, Sugarcane

Rabi (November – April) ❄️

Crops: Wheat, Barley, Gram, Mustard, Peas, Linseed

Zaid (March – June) ☀️

Crops: Watermelon, Muskmelon, Cucumber, Vegetables, Fodder crops

Monsoon (varies, overlaps Kharif) 🌦️

Crops: Paddy, Jute, Cotton

👉 Example: Since September falls in Kharif season, select “Kharif” in the app.


📊 Dataset & Models

Large datasets and trained ML models are not uploaded to GitHub due to size limits.

🔗 Download them here:

Google Drive Link
 (replace with your actual link)

After downloading:

Place datasets inside data/ folder

Place models inside models/ folder

✅ Future Improvements

Add farmer language support (Hindi, Telugu, Kannada, etc.)

Integrate real-time weather API

Add yield prediction and fertilizer recommendation

Deploy online for public farmers’ access

👨‍💻 Author

Kushal V R
🔗 kushVRK
