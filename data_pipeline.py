import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path):
    df = pd.read_csv(path)
    return df

def feature_engineering(df):
    # Only retain engineered features that are *not* leaking post-default data
    df['loan_to_income'] = df['loan_amt_outstanding'] / df['income']
    return df  # Important: return the modified DataFrame

def preprocess_features(df):
    # Safe, business-time-available features only
    features = [
        'loan_amt_outstanding',
        'income',
        'fico_score',
        'years_employed',
        'loan_to_income'
    ]
    X = df[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, df['default'], scaler
