import streamlit as st

def header(url):
     st.markdown(f'<p style="background-color:#F5F0E8;color:#1B1954;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
st.image('images/title.png')
st.caption('Group 1 Exp1orers - Francesca Panga | Jacob Fuentebella | Jersy Carino | Leonard Inciso | Lester Covarrubias II')

st.title ('Introduction')
st.subheader('Intro description')
st.image('images/mmda_geopandas.png')
st.write('---')

st.header('Case Study', divider='blue')
st.write('Sustainable Development Goal 3:')
st.write('Sustainable Development Goal 11:')
st.header('Scope', divider='blue')
st.header('Objectives', divider='blue')
st.image('images/objectives.png')
st.header('Methodology', divider='blue')
st.image('images/methodology.png')
