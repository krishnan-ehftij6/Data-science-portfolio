# 📌 BA Data Science Simulation Project

This project consists of two main tasks: **Web Scraping Customer Reviews** and **Predicting Customer Behavior**. The goal is to analyze customer sentiment from reviews and build a machine learning model to predict booking completion.

---

## 📂 Project Structure

```
BA-Data-Science-Simulation-Project/
│── Web-Scraping/
│   ├── data/            # Contains the web scraped dataset (CSV format)
│   ├── src/             # Jupyter Notebooks for web scraping & preprocessing
│   ├── presentation/    # Report with key insights and findings (PPT)
│
│── Predicting-Customer-Behaviour/
│   ├── data/            # Contains the dataset for model training
│   ├── src/             # Jupyter Notebooks for EDA, preprocessing & modeling
│   ├── presentation/    # Report with key insights and findings (PPT)
│
│── requirements.txt     # List of required Python packages
│── README.md            # This file
```

---

## 1️⃣ Web Scraping Customer Reviews

📌 **Objective:** Extract customer reviews from **Skytrax** to analyze sentiment and trends.

### 🔹 Key Steps:
- **Web Scraping:** Used `BeautifulSoup` & `Requests` to scrape **392 pages** of reviews.
- **Data Cleaning:** Converted dates, removed missing values, and structured the dataset.
- **Exploratory Data Analysis (EDA):** Visualized trends in customer sentiment.
- **Presentation:** Key insights summarized in the `presentation/` folder.

### 📁 Files:
- 📂 `data/` → Contains `scraped_reviews.csv` (final dataset).
- 📂 `src/` → Jupyter Notebooks for scraping (`code1.ipynb`) and preprocessing (`code2.ipynb`).
- 📂 `presentation/` → **Final report (PDF/PPT) summarizing key insights and visuals.**

---

## 2️⃣ Predicting Customer Behavior

📌 **Objective:** Build a **machine learning model** to predict whether customers complete their booking based on their choices during the booking process.

### 🔹 Key Steps:
- **EDA & Data Cleaning:** Explored key features, handled missing values, and encoded categorical variables.
- **Model Development:** Used a **Random Forest model** to predict booking completion.
- **Model Evaluation:** Assessed performance and identified key influencing factors.
- **Presentation:** Insights and model results in the `presentation/` folder.

### 📁 Files:
- 📂 `data/` → Contains `customer_booking_data.csv`.
- 📂 `src/` → Jupyter Notebooks for EDA (`eda.ipynb`), preprocessing (`preprocessing.ipynb`), and modeling (`model_training.ipynb`).
- 📂 `presentation/` → **Final report (PDF/PPT) summarizing model performance and insights.**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/krishnan-ehftij6/Data-science-portfolio.git
cd Data-science-portfolio/BA-Data-Science-Simulation-Project
```

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Jupyter Notebook
```bash
jupyter notebook
```
Then, navigate to the `src/` folder of each project and open the Jupyter Notebooks.

---

## 📌 Technologies Used
- **Python**: `BeautifulSoup`, `Requests`, `Pandas`, `Matplotlib`, `Seaborn`, `Scikit-learn`
- **Machine Learning**: `Random Forest`, `Train-Test Split`
- **Visualization**: `Seaborn`, `Matplotlib`
- **Development Environment**: `Jupyter Notebook`

---

## 📊 Results & Insights
- **Web Scraping:** Extracted insights on customer sentiment trends and flight experiences.
- **Machine Learning:** Achieved high accuracy in predicting booking completion.
- **Presentation:** Key findings, trends, and model results are available in the **presentation/** folders.

---

### 🚀 Future Improvements
- Expand web scraping to **multiple sources** for more diverse insights.
- Optimize the ML model with **hyperparameter tuning** and feature engineering.
- Deploy the predictive model using a **Flask API or Streamlit dashboard**.

---

## 📩 Contact
For questions or collaboration, feel free to reach out via **GitHub Issues** or email.
