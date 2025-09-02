import streamlit as st
import pandas as pd

# Title
st.title("🌾 AgroSmart Advisor - MVP")

# Upload dataset
uploaded_file = st.file_uploader("Upload Price Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Data loaded successfully!")

    # Show first few rows
    st.subheader("📊 Dataset Preview")
    st.write(df.head())

    # Select crop
    crop = st.selectbox("Select Commodity:", df["Commodity"].unique())

    # Filter dataset
    filtered = df[df["Commodity"] == crop]

    # Show summary
    st.subheader(f"📈 Price Trends for {crop}")
    st.line_chart(filtered["Modal_x0020_Price"])
else:
    st.info("Please upload a dataset to begin.")
