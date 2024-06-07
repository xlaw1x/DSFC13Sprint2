import streamlit as st

st.title("Modelling and Model Performance")
st.write("Given the imbalanced dataset, the group 5 resampling methods to see if these would improve the model's performance.")

st.title("Data Retrieval, Cleaning, and Preprocessing")
st.write("The dataset used in this project was obtained from the Kaggle website found at: https://www.kaggle.com/datasets/esparko/mmda-traffic-incident-data.")
st.write("This data from Kaggle was webscraped from the Metropolitan Manila Development Authority's (MMDA) official Twitter.") 

st.write("The initial dataset has 17,312 rows and 13 columns as shown below.")
st.image('images/dfinfo1.png')
