import pandas as pd
import numpy as np
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score, precision_score, recall_score, confusion_matrix
from sklearn.calibration import CalibratedClassifierCV
from imblearn.over_sampling import SMOTE

from data_pipeline import load_data, feature_engineering, preprocess_features

def train_model(X, y):
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Handle class imbalance
    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

    # Logistic Regression with calibration
    base_model = LogisticRegression(C=0.1, class_weight='balanced', solver='liblinear', random_state=42)
    calibrated_model = CalibratedClassifierCV(base_model, cv=5)
    calibrated_model.fit(X_train_res, y_train_res)

    # Evaluate on test set
    y_proba = calibrated_model.predict_proba(X_test)[:, 1]
    y_pred = calibrated_model.predict(X_test)

    print("AUC Score:", roc_auc_score(y_test, y_proba))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    return calibrated_model, X_test, y_test

def save_model(model, scaler, model_path='model/model.pkl', scaler_path='model/scaler.pkl'):
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print(f"[✔] Model saved to {model_path}")
    print(f"[✔] Scaler saved to {scaler_path}")



