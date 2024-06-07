import streamlit as st

st.image('images/title.png')
st.caption('Group 1 Exp1orers - Francesca Panga | Jacob Fuentebella | Jersy Carino | Leonard Inciso | Lester Covarrubias II')

st.title ('Introduction')
st.subheader('Intro description')
st.image('images/mmda_geopandas.png')
st.write('---')

st.header('Case Study', divider='blue')
st.write('Sustainable Development Goal 3:')
st.write('Sustainable Development Goal 11:')
st.write('---')

st.header('Scope', divider='blue')
st.write('---')

st.header('Objectives', divider='blue')
st.image('images/objectives.png')
st.write('---')

st.header('Methodology', divider='blue')
st.image('images/methodology.png')
st.write('---')

%%writefile "/content/drive/MyDrive/Eskwelabs/Notebooks/Filled Notebooks/streamlit_app.py"
# general libraries
import pickle
import pandas as pd

# model deployment
from flask import Flask
import streamlit as st

from operator import index
%%writefile "/content/drive/MyDrive/eskwelabs_workspace/Sprint2_Group1/streamlit_app.py"
# general libraries
import pickle
import pandas as pd

# model deployment
from flask import Flask
import streamlit as st

# read model and holdout data
model = pickle.load(open('/content/drive/MyDrive/eskwelabs_workspace/Sprint2_Group1/Filled Notebooks/gb_tk.pkl', 'rb'))
X_holdout = pd.read_csv('/content/drive/MyDrive/Eskwelabs/Notebooks/Filled Notebooks/holdout.csv', index_col=0)
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
