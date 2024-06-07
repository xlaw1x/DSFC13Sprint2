import streamlit as st

st.title("Summary")
st.write("Here you can provide a short summary and recommendations")

st.image("images/shap_feature_importance.png", width=550)
st.caption("SHAP Feature Importance")
st.write("---")

st.image("images/beeswarm.png")
st.caption("SHAP Beeswarm Plot")
st.write("---")

st.image("images/FP1.png")
st.caption("Force Plot for Datapoint 1 That Is a self_accident with One Involved Vehicle")
st.image("images/LIME1.png")
st.caption("LIME Prediction Probabilities for a Datapoint 1 That Is a self_accident with One Involved Vehicle")
st.write("---")

st.image("images/FP2.png")
st.caption("Force Plot for Datapoint 2 That Is a non_self_accident with One Involved Vehicle")
st.image("images/LIME2.png")
st.caption("LIME Prediction Probabilities for a Datapoint 2 That Is a non_self_accident with One Involved Vehicle")
st.write("---")

st.image("images/FP3.png")
st.caption("Force Plot for Datapoint 3 That Is a non_self_accident with Multiple Involved Vehicles")
st.image("images/LIME3.png")
st.caption("LIME Prediction Probabilities for a Datapoint 3 That Is a non_self_accident with Multiple Involved Vehicles")
st.write("---")
