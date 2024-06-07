import streamlit as st

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
        background-color: #30D5C8; /* Change this to your desired background color */
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

# Your Streamlit code here
# For example:
st.title('Welcome to My Streamlit App!')
st.write('This is where you can write your Streamlit app content.')


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
