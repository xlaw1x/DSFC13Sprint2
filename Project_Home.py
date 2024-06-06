import streamlit as st

st.image('images/title.png')
st.title ('HELLO, :red[RISKS], GOODBYE.') 
st.header('Profiling Churn Risk of Customers for Cost Optimization', divider='red')
st.caption('Group 1 Exp1orers - Francesca Panga | Jacob Fuentebella | Jersy Carino | Leonard Inciso | Lester Covarrubias II')

st.subheader("The Challenge:")
st.markdown("Adobo Credit Card (ACC) strives to optimize sales, boost business performance, and drive customer satisfaction.")
st.subheader("The Goal:")
st.markdown("Develop sales and marketing strategies that will further increase customers' card usage.")
st.markdown("---")

st.subheader("Risk-Profiling Objectives:")
st.markdown("In classifying the clients of Adobo Credit Card according to their churn risk, valuable insights on the clients can be obtained based on the following areas.")

st.markdown("Spending Behavior:")
st.caption("Spending frequency - how often is this customer making a transaction?, Seasonal spending trends - are there any abrupt changes in spending habits across the year?, Categorical budget allocation - what are the customers spending on?, Payment mode preferences - does this client prefer to transact online or purchase in-store?")
st.markdown("Customer Demographic:")
st.caption("Customer age groups - is this customer a Boomer? a Gen X?, Geographical location - what regions are these customers from?, Gender, Industry of work, Profession")
st.markdown("---")

st.image('methodology.png')
st.caption("The scope of the problem is that there is a category of customers who are at high risk of churning. The goal is to propose strategies to encourage these users to be more active credit card users, while ensuring the continued customer satisfaction of loyal customers.")
st.caption("Data Cleaning and Preprocessing involved removing duplicates, turning number strings into numerical data types, and extracting data from other columns and creating new columns with a more usable format.")
st.caption("EDA, Customer Segmentation, Clustering, and Insights will be discussed in the next pages.")
st.markdown("---")

st.image('adobo_clients.png')
st.caption("Who are the Adobo clients? Based on 100,000 transaction data points obtained from January 2020 to December 2021, ACC was observed to have 94 unique clients. The majority of these customers are male, making up 93.6%, and range from 51-95 years old. They live in 60 cities across the Philippines, with the greatest percentage in Luzon, followed by Mindanao then Visayas.")
st.markdown("---")
