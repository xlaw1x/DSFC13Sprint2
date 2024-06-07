import streamlit as st

st.title("Modelling and Model Performance")
st.write("Given the imbalanced dataset, the group 5 resampling methods to see if these would improve the model's performance.")

st.header("Oversampling Techniques")
st.image('images/baseline.png')

st.header("Oversampling Techniques") 
st.image('images/SMOTE.png')
st.caption("No Hypertuning, with SMOTE Oversampling")
st.image('images/ADASYN.png')
st.caption("No Hypertuning, with ADASYN Oversampling")
st.image('images/SMOTEN.png')
st.caption("No Hypertuning, with SMOTEN Oversampling")
st.image('images/oversampling_comparison.png')
st.caption("Comparison of Oversampling Methods")
st.image('images/bar_graph.png')
st.caption("Comparison of Oversampling Methods")

st.header("Undersampling Techniques") 
st.image('images/EditedNearestNeighbors.png')
st.caption("No Hypertuning, with EditedNearestNeighbors Undersampling")
st.image('images/TomekLinks.png')
st.caption("No Hypertuning, with TomekLinks Undersampling")
st.image('images/undersampling_comparison.png')
st.caption("Comparison of Undersampling Methods")
st.image('images/bar_graph_undersampling.png')
st.caption("Comparison of Undersampling Methods")

st.image('images/final_comparison.png')
st.caption("Comparison of All Models")


