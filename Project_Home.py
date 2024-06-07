import streamlit as st

# def header(url):
#      st.markdown(f'<p style="background-color:#F5F0E8;color:#1B1954;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

# Set page configuration
st.set_page_config(
    page_title="Your Page Title",
    page_icon="Your Page Icon URL",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6; /* Change this to your desired background color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set text color
st.markdown(
    """
    <style>
    body, label, .css-vfskoc, .st-ab, .st-ag {
        color: #333333; /* Change this to your desired text color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
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
