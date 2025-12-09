# app_streamlit_dummy.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# Page config & styling
# -----------------------
st.set_page_config(
    page_title="FalconShield — Smart Fraud Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(180deg, #0f172a 0%, #0b1220 100%); color: white; }
    .big-font { font-size:28px !important; font-weight:600; color: #E6F1FF; }
    .subtle { color:#BBD6FF; }
    .card { background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01)); padding: 12px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True
)

# -----------------------
# Dummy fraud prediction function
# -----------------------
def predict_fraud(data):
    """
    Rule-based prediction:
    - Amount > 5000 is fraud
    - Time > 80000 seconds is fraud
    """
    if data["Amount"] > 5000 or data["Time"] > 80000:
        return "Fraud 🚨"
    else:
        return "Legit ✅"

# -----------------------
# UI layout
# -----------------------
st.markdown('<div style="display:flex;align-items:center;gap:16px"> \
                <div><img src="https://img.icons8.com/color/96/000000/shield.png" width="60"></div> \
                <div><span class="big-font">FalconShield</span><div class="subtle">Smart Credit Card Fraud Detector</div></div> \
             </div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar controls
with st.sidebar:
    st.header("Configure")
    threshold = st.slider("Fraud threshold (ignored in dummy)", 0.0, 1.0, 0.50, 0.01)
    st.markdown("---")
    st.write("This version uses a simple rule-based prediction (no ML model).")

# Tabs
tab1, tab2 = st.tabs(["Predict Single Transaction", "Batch Scoring (CSV)"])

# -----------------------
# Tab 1: Single transaction
# -----------------------
with tab1:
    st.subheader("🔎 Predict Single Transaction")
    col1, col2 = st.columns(2)

    Time = col1.number_input("Time (seconds)", value=100000, min_value=0, step=1)
    Amount = col2.number_input("Amount", value=100.0, min_value=0.0, format="%.2f")

    if st.button("Run Prediction"):
        transaction = {"Time": Time, "Amount": Amount}
        result = predict_fraud(transaction)
        if result == "Fraud 🚨":
            st.error(f"Prediction: {result}")
        else:
            st.success(f"Prediction: {result}")

# -----------------------
# Tab 2: Batch scoring
# -----------------------
with tab2:
    st.subheader("📁 Batch Scoring (CSV upload)")
    st.markdown("Upload CSV with columns: Time, Amount. V1..V28 not required.")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview uploaded data:")
        st.dataframe(df.head(5))

        # Run predictions
        if st.button("Run Batch Prediction"):
            df["prediction"] = df.apply(lambda row: predict_fraud({"Time": row["Time"], "Amount": row["Amount"]}), axis=1)
            st.success("Batch prediction completed!")
            st.dataframe(df.head(10))

            # Download link
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download scored CSV", csv, "scored_transactions.csv", "text/csv")

st.markdown("---")
st.caption("FalconShield — Dummy Fraud Detector • Rule-based version for demo/prototyping. Users only input Time & Amount.")
