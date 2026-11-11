# Customer Analytics & Purchase Prediction

## Project Overview
This project uses Machine Learning to analyze customer purchasing behavior, group customers into segments, and predict whether a customer is likely to accept a marketing campaign.

## Objectives
- Analyze customer income and spending patterns.
- Perform Exploratory Data Analysis (EDA).
- Segment customers using K-Means clustering.
- Predict campaign responses using Logistic Regression.
- Evaluate the prediction model.
- Build an interactive dashboard using Streamlit.

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Google Colab

## Machine Learning Algorithms
**1. K-Means Clustering:** Groups customers based on income and total spending.

**2. Logistic Regression:** Predicts whether a customer will accept a marketing campaign.

## Project Features
- Customer data analysis
- Income and spending visualization
- Customer segmentation
- Campaign response prediction
- Interactive Streamlit dashboard

## Project Structure
```text
Customer-Analytics-AI-ML/
├── app.py
├── requirements.txt
├── cleaned_customer_data.csv
├── kmeans_model.pkl
├── kmeans_scaler.pkl
├── purchase_model.pkl
├── purchase_scaler.pkl
└── README.md
```

## How to Run the Project

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

## Dataset
Customer Personality Analysis dataset from Kaggle:

https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis

## Project Outcome
The project demonstrates how Machine Learning can be used to understand customer behavior, identify customer groups, and predict marketing campaign responses.

## Disclaimer
Predictions are based on the available dataset and trained model. They are estimates and not guarantees of customer behavior.