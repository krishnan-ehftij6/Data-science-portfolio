### Web Scraping Data – Customer Reviews
As part of this project, web scraping was conducted to collect customer reviews from the Skytrax website. The goal was to analyze customer feedback and extract key insights that contribute to understanding customer sentiment and behavior.

**Project Structure**
📂 data/ – Contains the web-scraped dataset

scraped_data.csv – The processed dataset in CSV format
📂 src/ – Contains the Python scripts for web scraping, data processing and data visualisation

code_1_BA_web_scraping_reviews.ipynb – Web scraping script that collects data and converts it into a Pandas DataFrame
code_2_BA_reviews_visualisations.ipynb – Data preprocessing, cleaning, and visualization script

**Data Collection Process**
Website Scraped: Skytrax
Number of Pages Scraped: 392
Tools Used:
BeautifulSoup and Requests for web scraping
Pandas for data processing and conversion to a structured CSV dataset

**Data Preprocessing & Exploratory Data Analysis (EDA)**
The following preprocessing steps were performed:
✅ Column Analysis: Understanding the dataset structure and key features
✅ Date Formatting: Converting Date Flown and Date Published columns into datetime format
✅ Index Ordering: Sorting the dataset by Date Published for chronological analysis

**Data Visualization & Insights**
Key Metrics Analyzed:
Customer sentiment
Review trends over time
Ratings distribution
Visualization Techniques:
Graphs and charts created to highlight patterns in customer reviews
Key insights summarized in presentation slides
