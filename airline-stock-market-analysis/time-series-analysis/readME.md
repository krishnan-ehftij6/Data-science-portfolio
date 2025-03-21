# 📈 Flying High or Hitting Turbulence? A Time-Series Analysis of Airline Stocks

## ✈️ Project Overview
This project examines the volatility of airline stocks across different global regions, identifying key factors influencing stock price fluctuations. Using data science and machine learning models, we analyze how oil prices, market volatility, and moving averages affect airline stock movements.

## 📂 Repository Structure
├── data/ # 📊 Contains raw and processed datasets │ ├── airline_oil_prices_fixed.csv │ 
├── src/ # 📜 Contains source code for analysis & modeling │ ├── data_preprocessing.py │ 
yaml
Copy
Edit

---

## 🛠️ Setup Instructions
To run the analysis locally, follow these steps:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/krishnan-ehftij6/airline-stock-market-analysis.git
   cd time-series-analysis
Install Dependencies
It's recommended to use a virtual environment:

bash
Copy
Edit
pip install -r requirements.txt
Run Jupyter Notebook (For analysis & visualization)

bash
Copy
Edit
jupyter notebook

### Dataset Description
Data Sources
The dataset includes airline stock prices, oil prices, and the code file includes processing them to get market volatility indicators:

Feature	Description
Date	Trading date (YYYY-MM-DD)
Stock_Price	Closing stock price of each airline
Oil_Price	Brent Crude oil price (USD per barrel)
