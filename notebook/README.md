# 🏦 Fintech Credit Risk Scoring & Default Prediction Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://YOUR-STREAMLIT-APP-URL.streamlit.app](https://malaysia-credit-risk-scoring-9ktxq3khsmzcgncgd46x4p.streamlit.app/#key-risk-drivers))

## Executive Summary
This project builds an end-to-end machine learning credit risk engine designed for digital banks and BNPL (Buy-Now-Pay-Later) platforms. Built using financial borrower data (~150k records), the pipeline handles dirty real-world data, engineers domain-specific financial risk metrics, predicts 2-year default probability using **XGBoost**, and translates raw risk probabilities into a standard **300–850 Credit Score**.

To align with **Bank Negara Malaysia (BNM)** regulatory standards regarding model explainability in automated lending, the system integrates **SHAP (SHapley Additive exPlanations)** to provide transparent audit trails for every credit decision.

---

## 📊 Key Results & Business Impact
* **Model Performance:** Achieved an **AUC-ROC of ~0.86** and a **Gini Coefficient of ~0.72**, significantly outperforming traditional Logistic Regression scorecards.
* **Risk Identification:** Engineered features like `TotalDelinquencies` and `IsCreditMaxed` proved to be top predictors of default, showing >18% positive correlation with borrower default risk.
* **Deployment:** Interactive scoring dashboard deployed live via Streamlit Cloud for real-time risk assessment and automated approval workflows.

---

## 🛠️ Tech Stack & Methodology
* **Languages & Core:** Python, Pandas, NumPy, Scikit-Learn
* **Machine Learning:** XGBoost (handling class imbalance via `scale_pos_weight`), Logistic Regression (Baseline)
* **Model Explainability:** SHAP (TreeExplainer summary & waterfall plots)
* **Web Deployment:** Streamlit Framework
* **Metric Evaluation:** ROC-AUC, Gini Coefficient, Precision-Recall

---

## 💡 Machine Learning & Financial Scoring Pipeline

```text
[Raw Borrower Data] 
       │
       ▼
[Data Engineering & Cleaning] ────► (Age-group median income imputation, 99th percentile winsorization)
       │
       ▼
[Feature Engineering] ──────────► (Total Delinquency Index, Credit Max-out flags, DTI proxies)
       │
       ▼
[Model Training & Tuning] ──────► (XGBoost Classifier + Class Imbalance Calibration)
       │
       ▼
[Explainability & Scaling] ─────► (SHAP value extraction + PDO Credit Score Conversion: 300-850)
       │
       ▼
[Production Deployment] ────────► (Interactive Streamlit Dashboard)
```

## 📁 Repository Architecture
```text
malaysia-credit-risk-scoring/
├── app/
│   └── app.py               <- Streamlit interactive web application
├── notebooks/
│   └── credit_scoring.ipynb  <- Data cleaning, EDA, feature engineering & model training
├── requirements.txt         <- Project dependencies
└── README.md                <- Executive summary & technical documentation
```
