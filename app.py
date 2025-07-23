import streamlit as st
import math
import datetime
from streamlit import config as _config

# Force light theme at configuration level
_config.set_option("theme.base", "light")

# Custom CSS loader
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found!")

# Load CSS
local_css("style.css")

# --- Calculator Functions ---
def calculate_emi(principal, annual_rate, tenure_years):
    monthly_rate = annual_rate / 12 / 100
    tenure_months = tenure_years * 12
    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, tenure_months)) / (math.pow(1 + monthly_rate, tenure_months) - 1)
    return emi

def calculate_dscr(annual_income, annual_expenses, emi):
    net_operating_income = annual_income - annual_expenses
    total_debt_service = emi * 12
    dscr = net_operating_income / total_debt_service if total_debt_service != 0 else 0
    return dscr

def assess_risk(dscr):
    if dscr < 1.2:
        return "High Risk", f"DSCR of {dscr:.2f} → High risk: Cash flow covers only {dscr*100:.0f}% of debt"
    elif 1.2 <= dscr < 1.5:
        return "Caution", f"DSCR of {dscr:.2f} → Caution: Cash flow covers {dscr*100:.0f}% of debt"
    else:
        return "Healthy", f"DSCR of {dscr:.2f} → Healthy: Cash flow covers {dscr*100:.0f}% of debt"


# --- Main App ---
def main():
    st.image("https://via.placeholder.com/800x150?text=DSCR+EMI+Calculator", use_column_width=True)
    st.title("Loan Assessment Calculator")
    st.markdown("Professional DSCR and EMI calculator for Indian lenders")

    # Input Section
    with st.expander("Loan Parameters", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            principal = st.number_input(
                "Loan Amount (₹)", 
                min_value=1000, 
                max_value=1000000000, 
                value=1000000, 
                step=10000,
                key="loan_amount"
            )
        with col2:
            annual_rate = st.number_input(
                "Interest Rate (% p.a.)", 
                min_value=1.0, 
                max_value=30.0, 
                value=12.0, 
                step=0.25,
                key="interest_rate"
            )
        with col3:
            tenure_years = st.number_input(
                "Tenure (Years)", 
                min_value=1, 
                max_value=30, 
                value=5, 
                step=1,
                key="tenure"
            )
    
    with st.expander("Borrower Financials"):
        col1, col2 = st.columns(2)
        with col1:
            annual_income = st.number_input(
                "Annual Income (₹)", 
                min_value=0, 
                value=500000, 
                step=10000,
                key="income"
            )
        with col2:
            annual_expenses = st.number_input(
                "Annual Expenses (₹)", 
                min_value=0, 
                value=300000, 
                step=10000,
                key="expenses"
            )

    # Calculations
    if st.button("Calculate"):
        emi = calculate_emi(principal, annual_rate, tenure_years)
        dscr = calculate_dscr(annual_income, annual_expenses, emi)
        risk_assessment = assess_risk(dscr)
        
        # Display Results
        st.success("Calculation complete!")
        
        with st.expander("Results Summary", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Monthly EMI", f"₹{emi:,.2f}")
                st.metric("Annual Debt Service", f"₹{emi*12:,.2f}")
            with col2:
                st.metric("DSCR", f"{dscr:.2f}", risk_assessment[0])
                st.metric("Net Operating Income", f"₹{annual_income - annual_expenses:,.2f}")
            
            st.info(risk_assessment[1])
        
        # PDF Generation
        inputs = {
            'principal': principal,
            'annual_rate': annual_rate,
            'tenure_years': tenure_years,
            'annual_income': annual_income,
            'annual_expenses': annual_expenses
        }
        
        results = {
            'emi': emi,
            'annual_debt_service': emi * 12,
            'net_operating_income': annual_income - annual_expenses,
            'dscr': dscr,
            'risk_assessment': risk_assessment
        }
        
        st.success("Calculation complete! Use the results above.")

if __name__ == "__main__":
    main()