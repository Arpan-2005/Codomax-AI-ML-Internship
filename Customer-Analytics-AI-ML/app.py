
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Customer Analytics Dashboard",
    layout="wide"
)

# Load dataset and saved models
df = pd.read_csv("cleaned_customer_data.csv")

kmeans = joblib.load("kmeans_model.pkl")
kmeans_scaler = joblib.load("kmeans_scaler.pkl")

purchase_model = joblib.load("purchase_model.pkl")
purchase_scaler = joblib.load("purchase_scaler.pkl")

# Dashboard title
st.title("Customer Analytics & Purchase Prediction")
st.write("Analyze customer spending, segments and campaign responses.")

# Calculate total spending
spending_columns = [
    "MntWines", "MntFruits", "MntMeatProducts",
    "MntFishProducts", "MntSweetProducts", "MntGoldProds"
]

df["Total_Spending"] = df[spending_columns].sum(axis=1)

# Dashboard metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("Average Income", f"{df['Income'].mean():,.0f}")
col3.metric("Average Spending", f"{df['Total_Spending'].mean():,.0f}")

st.divider()

# Customer segmentation chart
st.subheader("Customer Segmentation")

segment_counts = df["Customer_Segment"].value_counts().sort_index()

fig, ax = plt.subplots()
segment_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Customer Segment")
ax.set_ylabel("Number of Customers")
ax.set_title("Customers in Each Segment")

st.pyplot(fig)
plt.close(fig)

# Product spending chart
st.subheader("Spending by Product Category")

product_spending = df[spending_columns].sum()

fig, ax = plt.subplots()
product_spending.plot(kind="bar", ax=ax)
ax.set_xlabel("Product Category")
ax.set_ylabel("Total Spending")
ax.set_title("Product Category Analysis")

st.pyplot(fig)
plt.close(fig)

# Purchase prediction
st.divider()
st.subheader("Predict Campaign Response")

income = st.number_input("Customer Income", min_value=0.0, value=50000.0)
total_spending = st.number_input("Total Spending", min_value=0.0, value=1000.0)
recency = st.number_input("Days Since Last Purchase", min_value=0, value=30)
web_purchases = st.number_input("Web Purchases", min_value=0, value=3)
catalog_purchases = st.number_input("Catalog Purchases", min_value=0, value=2)
store_purchases = st.number_input("Store Purchases", min_value=0, value=5)
web_visits = st.number_input("Website Visits Per Month", min_value=0, value=5)
kidhome = st.number_input("Children at Home", min_value=0, value=0)
teenhome = st.number_input("Teenagers at Home", min_value=0, value=0)

if st.button("Predict Campaign Response"):

    customer = pd.DataFrame([[
        income,
        total_spending,
        recency,
        web_purchases,
        catalog_purchases,
        store_purchases,
        web_visits,
        kidhome,
        teenhome
    ]], columns=[
        "Income",
        "Total_Spending",
        "Recency",
        "NumWebPurchases",
        "NumCatalogPurchases",
        "NumStorePurchases",
        "NumWebVisitsMonth",
        "Kidhome",
        "Teenhome"
    ])

    customer_scaled = purchase_scaler.transform(customer)
    prediction = purchase_model.predict(customer_scaled)[0]

    if prediction == 1:
        st.success("Prediction: Customer is likely to accept the campaign!")
    else:
        st.warning("Prediction: Customer is unlikely to accept the campaign.")

# Footer
st.divider()
st.caption("AI/ML Final Project | Customer Analytics")
