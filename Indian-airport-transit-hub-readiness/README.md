
# Indian Airports as Global Transit Hubs – A Data Science Analysis  

## Project Overview  
This project analyzes passenger reviews to assess whether Indian airports are prepared to compete as global transit hubs. Using web scraping, sentiment analysis, and predictive modeling, the study identifies key strengths and areas for improvement in Indian airports compared to leading international hubs.  

The key findings and insights have been documented in a blog post: [Read here](your-medium-blog-link)  

# Project Folder Structure  
📂 Indian_Airports_Transit_Hubs
├── 📂 src
│ ├── scraping_reviews.py # Web scraping Skytrax reviews
│ ├── data_preprocessing.py # Cleaning & preprocessing data
│ ├── sentiment_analysis.py # Sentiment analysis & predictive modeling
│
├── 📂 data
│ ├── airport_reviews.csv # Raw scraped data
│ ├── cleaned_df.csv # Preprocessed & cleaned dataset
│ ├── sentiment_analysis_results.csv # Sentiment scores & final analysis results
│

## Key Steps  
1. **Data Collection:**  
   - Web scraped passenger reviews from Skytrax for major Indian and global transit hubs.  
   - Extracted key information such as ratings, review text, and passenger categories.  

2. **Data Preprocessing:**  
   - Cleaned textual data (removed noise, stopwords, and irrelevant information).  
   - Extracted key features such as sentiment scores and frequent terms.  

3. **Sentiment Analysis & Modeling:**  
   - Applied Natural Language Processing (NLP) techniques to classify reviews as positive, neutral, or negative.  
   - Built predictive models (Logistic Regression & Random Forest) to identify key factors influencing passenger recommendations.  

4. **Key Findings & Insights:**  
   - Indian airports like Bengaluru and Hyderabad received better transit reviews than Delhi and Mumbai.  
   - Global hubs like Singapore and Hong Kong consistently outperformed Indian airports in passenger satisfaction.  
   - Correlation analysis revealed strong links between terminal cleanliness, seating, and overall experience.  

## Next Steps & Future Improvements  
- Expand the analysis with a larger dataset from multiple review sources.  
- Explore time-series sentiment trends to track airport improvements over time.  
- Investigate additional external factors such as layover tourism, hotel availability, and visa policies.  

## How to Use  
- Run `scraping_reviews.py` to collect fresh review data.  
- Use `data_preprocessing.py` to clean and preprocess the dataset.  
- Execute `sentiment_analysis.py` for sentiment classification and predictive modeling.  

## Contact  
For any questions or collaboration opportunities, feel free to connect via [LinkedIn](https://www.linkedin.com/in/krishnan-s-7b8ba4a9/) or check out my [Blog](aviationdatabykrishnan.medium.com)  for more insights.  
