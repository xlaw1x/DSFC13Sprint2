import streamlit as st

st.title("Would you like to try predicting a self-accident?")
#st.header("Head on over to the following link: https://social-gifts-sink.loca.lt/!")

# Display the local image
st.image("images/ml_app.png", caption="Image Caption", use_column_width=True)

# Display the local image as a clickable link button
st.markdown("[![Self-accident Detection ML App](st.image("images/ml_app.png")](https://social-gifts-sink.loca.lt/)")
