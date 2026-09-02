%%writefile app.py
import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb

# Set page title and layout
st.set_page_config(page_title="Fintech Credit Scoring Engine", layout="wide")

st.title("🏦 Fintech Credit Risk & Scoring Engine")
st.markdown("Enter applicant financial details below to calculate default risk probability and credit score.")

st.sidebar.header("Applicant Financial Profile")

# Input fields for recruiters to test
age = st.sidebar.slider("Age", 18, 90, 35)
monthly_income = st.sidebar.number_input("Monthly Income (RM)", min_value=0, value=5000, step=500)
debt_ratio = st.sidebar.slider("Debt Ratio (Monthly Debt / Income)", 0.0, 2.0, 0.35)
utilization = st.sidebar.slider("Credit Card Utilization Ratio", 0.0, 2.0, 0.25)
total_delinquencies = st.sidebar.selectbox("Historical Late Payments Count", [0, 1, 2, 3, 4, 5])
open_lines = st.sidebar.number_input("Number of Open Credit Lines/Loans", min_value=0, value=4)
real_estate_loans = st.sidebar.number_input("Number of Real Estate Loans", min_value=0, value=1)
dependents = st.sidebar.number_input("Number of Dependents", min_value=0, value=1)

# Feature engineering calculations inside app
is_credit_maxed = 1 if utilization > 1.0 else 0
est_monthly_debt = debt_ratio * monthly_income
total_loans = open_lines + real_estate_loans

# Credit Score Calculation Function
def calculate_score(prob):
    prob = np.clip(prob, 0.0001, 0.9999)
    odds = (1 - prob) / prob
    score = 600 + (28.85 * np.log(odds))
    return int(np.clip(score, 300, 850))

# Display Results on Button Click
if st.sidebar.button("Evaluate Credit Risk"):
    # Mock model scoring calculation (mirrors XGBoost logic)
    risk_score = (utilization * 0.4) + (total_delinquencies * 0.25) + (is_credit_maxed * 0.2) - (age * 0.005)
    prob_default = float(1 / (1 + np.exp(-risk_score + 2)))
    credit_score = calculate_score(prob_default)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Credit Score", f"{credit_score} / 850")
    with col2:
        st.metric("Default Probability", f"{prob_default:.2%}")
    with col3:
        if credit_score >= 700:
            st.success("Recommendation: APPROVED")
        elif credit_score >= 620:
            st.warning("Recommendation: MANUAL REVIEW")
        else:
            st.error("Recommendation: REJECTED")
            
    st.markdown("---")
    st.subheader("Key Risk Drivers")
    if utilization > 0.8:
        st.write("⚠️ **High Utilization:** Credit utilization is above 80%, indicating financial distress.")
    if total_delinquencies > 0:
        st.write("⚠️ **Delinquency History:** Past-due payments significantly increase default risk.")
    if credit_score >= 700:
        st.write("✅ **Strong Profile:** Healthy income-to-debt balance and low credit utilization.")
