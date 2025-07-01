#app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import io
from utils import expected_loss, assign_risk_band

# Load model and scaler
model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

# Streamlit Page Config
st.set_page_config(page_title="Loan Default Risk Predictor", layout="centered")
st.title("💼 Loan Default Risk Predictor")
st.markdown("Estimate borrower's **default probability**, **risk category**, and **expected loss** on a loan.")

# 🔔 Add disclaimer about model limitations
st.warning(
    "**⚠️ Disclaimer**: This model was trained on synthetic data with loan amounts typically ranging between "
    "$1,000\u00A0and\u00A0$10,750. Predictions may be unreliable for inputs significantly outside this range. "
    "For more accurate results, consider retraining on your institution’s portfolio."
)




# Input fields
st.header("Borrower Details")
income = st.number_input("Annual Income ($)", min_value=10000, max_value=500000, step=5000)
loan_amt = st.number_input("Loan Amount Outstanding ($)", min_value=1000, max_value=200000, step=1000)
years_employed = st.slider("Years Employed", min_value=0, max_value=50, value=5)
fico_score = st.slider("FICO Score", min_value=300, max_value=850, value=650)

# Predict button
if st.button("📊 Predict Risk"):
    # Feature engineering (only use selected features)
    # debt_to_income = total_debt / income
    loan_to_income = loan_amt / income

    # 🚨 Warn if input is outside training data distribution
    if loan_amt > 11000 or loan_to_income > 0.15:
        st.error("⚠️ Warning: The loan amount or loan-to-income ratio is outside the range used for training. Prediction may be unreliable.")


    input_data = pd.DataFrame([[
    loan_amt,
    income,
    fico_score,
    years_employed,
    loan_to_income
     ]], columns=[
         'loan_amt_outstanding',
         'income',
         'fico_score',
         'years_employed',
         'loan_to_income'
])


    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    pd_score = model.predict_proba(input_scaled)[0][1]
    risk_band = assign_risk_band(pd_score)
    eloss = expected_loss(pd_score, loan_amt)

    # Output
    st.subheader("📈 Prediction Results")
    st.metric("Default Probability", f"{pd_score:.2%}")
    st.metric("Risk Category", risk_band)
    st.metric("Expected Loss", f"${eloss:,.0f}")

    # Gauge Chart
    st.subheader("📉 Risk Probability Gauge")
    import plotly.graph_objects as go
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=pd_score * 100,
        title={'text': "Default Probability (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkred"},
            'steps': [
                {'range': [0, 30], 'color': "lightgreen"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "tomato"},
            ]
        }
    ))
    st.plotly_chart(fig)

    # Create CSV for download
    result_df = pd.DataFrame({
        "Annual Income ($)": [income],
        "Loan Amount ($)": [loan_amt],
        "Years Employed": [years_employed],
        "FICO Score": [fico_score],
        "Loan-to-Income": [loan_to_income],
        "Predicted Default Probability": [f"{pd_score:.2%}"],
        "Risk Category": [risk_band],
        "Expected Loss ($)": [f"${eloss:,.0f}"]
    })

    csv_buffer = io.StringIO()
    result_df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="📥 Download Results as CSV",
        data=csv_buffer.getvalue(),
        file_name="loan_risk_assessment.csv",
        mime="text/csv"
    )



    

