def expected_loss(pd_score, loan_amount, lgd=0.9):
    """
    Calculate expected loss for a loan.
    EL = PD × LGD × Loan Amount
    """
    return pd_score * lgd * loan_amount

def assign_risk_band(pd_score):
    """
    Classify borrower into risk band based on predicted PD.
    Thresholds:
        - Low: < 0.3
        - Medium: 0.3 to < 0.7
        - High: >= 0.7
    """
    if pd_score < 0.3:
        return "Low"
    elif pd_score < 0.7:
        return "Medium"
    else:
        return "High"
