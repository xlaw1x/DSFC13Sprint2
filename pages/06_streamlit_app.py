
# general libraries
import pickle
import pandas as pd

# model deployment
from flask import Flask
import streamlit as st

import os

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute file path to the pickle file
file_path = os.path.join(script_dir, 'data', 'baseline_model.pkl')

# Load the model from the pickle file
with open(file_path, 'rb') as f:
    model = pickle.load(f)

X_holdout = pd.read_csv('holdout.csv', index_col=0)
holdout_accidents = X_holdout.index.to_list()

st.title("Self-accident Detection")
html_temp = """
<div style="background:#025246 ;padding:10px">
<h2 style="color:white;text-align:center;"> Self-accident Detection ML App </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)

#adding a selectbox
choice = st.selectbox(
    "Select Accident Number:",
    options = holdout_accidents)


def predict_is_self_accident(index):
    accident = X_holdout.loc[index].values.reshape(1, -1)
    prediction_num = model.predict(accident)[0]
    pred_map = {1: 'is_self_accident', 0: 'is_not_self_accident'}
    prediction = pred_map[prediction_num]
    return prediction

if st.button("Predict"):
    output = predict_is_self_accident(choice)

    if output == 'is_self_accident':
        st.error('This accident may be a self-accident', icon="🚨")
    elif output == 'is_not_self_accident':
        st.success('This is not a self-accident!', icon="✅")
