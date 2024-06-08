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


# general libraries
import pickle
import pandas as pd

# model deployment
import streamlit as st

# read model and holdout data
model = pickle.load(open('/baseline_model.pkl', 'rb'))
holdout_df = pd.read_csv('/holdout.csv', index_col=0)

st.title("Self-accident Detection")
html_temp = """
<div style="background:#025246 ;padding:10px">
<h2 style="color:white;text-align:center;"> Self-accident Detection ML App </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

# Adding a selectbox for choosing index
selected_index = st.selectbox("Select Index:", options=holdout_df.index)

# Display selected columns for the chosen index
st.write("Selected row:")
st.write("Latitude:", holdout_df.at[selected_index, 'Latitude'])
st.write("Longitude:", holdout_df.at[selected_index, 'Longitude'])
st.write("Motorcycle Involved:", holdout_df.at[selected_index, 'Involved_motorcycle'])
st.write("Involved_bus:", holdout_df.at[selected_index, 'Involved_bus'])
st.write("Involved_car:", holdout_df.at[selected_index, 'Involved_car'])
st.write("Involved_van:", holdout_df.at[selected_index, 'Involved_van'])
st.write("Involved_truck:", holdout_df.at[selected_index, 'Involved_truck'])

def predict_is_self_accident(index):
    # Select all columns for prediction
    row = holdout_df.loc[index]
    # Convert row data to array for prediction
    row_array = row.values.reshape(1, -1)
    prediction_num = model.predict(row_array)[0]
    pred_map = {1: 'is_self_accident', 0: 'is_not_self_accident'}
    prediction = pred_map[prediction_num]
    return prediction

if st.button("Predict"):
    output = predict_is_self_accident(selected_index)

    if output == 'is_self_accident':
        st.error('This accident may be a self-accident', icon="🚨")
    elif output == 'is_not_self_accident':
        st.success('This is not a self-accident!', icon="✅")
