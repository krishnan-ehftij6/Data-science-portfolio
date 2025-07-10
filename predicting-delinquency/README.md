# 🧠 Credit Card Delinquency Predictor (FastAPI + ML Pipeline)

This project predicts **credit card delinquency** using a trained Random Forest model. It exposes a **real-time API** using **FastAPI**, built for practical use cases like banking tools, fintech products, or ML service integration.

---

## 🚀 Why This Project Matters

- Trained a **machine learning pipeline** using scikit-learn and best practices (scaling, imputation, class imbalance handling).
- Deployed a **real-time API** using FastAPI and Uvicorn — not just a notebook.
- Shows capability **beyond data analysis** — working with APIs, deployment logic, and production-ready ML.

If you're hiring for ML/DS roles, this isn’t just exploratory work — it’s **usable code**.

---

## 🔍 Features

- 📈 **Random Forest classifier** trained on real-world-style data
- ⚖️ Handles **class imbalance** (delinquency is rare)
- 🧼 Clean pipeline with `SimpleImputer`, `StandardScaler`, and `ColumnTransformer`
- 🔮 Outputs both prediction (0/1) and **delinquency probability**
- 🧪 Interactive testing via Swagger UI at `/docs`

---

## 🛠️ Tech Stack

- Python, Pandas, scikit-learn
- FastAPI, Uvicorn
- Joblib (for model serialization)

---

## 🧪 How to Run Locally

### 1. Install requirements

```bash
pip install -r requirements.txt

