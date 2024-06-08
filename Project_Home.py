import streamlit as st

st.image('images/title.png')
st.caption('Group 1 Exp1orers - Francesca Panga | Jacob Fuentebella | Jersy Carino | Leonard Inciso | Lester Covarrubias II')

st.title ('Introduction')

# Display justified text using HTML/CSS within markdown
st.markdown(
    """
    <div style="text-align: justify">
        Approximately 1.19 million people lose their lives each year due to road traffic crashes globally. This alarming statistic underscores the urgent need for effective measures to address road safety issues. 92% of global road deaths occur in low- and middle-income countries, which account for just 60% of the world's vehicles. This disparity highlights the critical importance of prioritizing road safety initiatives, particularly in regions with limited resources, including the Philippines. Over the past decade, our country has seen a rise in road traffic accidents. In 2023 alone, Metro Manila recorded around 86,000 accidents, a 20% increase from the previous year, with 14% resulting in fatalities. These incidents not only impact lives but also cost 2.6% of the country's GDP, highlighting the economic burden of road safety issues. Aligned with Sustainable Development Goal (SDG) #3, "Good Health and Well-being," and SDG #11, "Sustainable Cities and Communities", our study on enhancing road safety through machine learning is crucial, as road traffic accidents significantly threaten public health and well-being globally.
    </div>
    """,
    unsafe_allow_html=True
)

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
