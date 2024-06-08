import streamlit as st

st.title("Modelling and Model Performance")
st.write("Given the imbalanced dataset, the group tested 5 resampling methods (SMOTE, SMOTEN, ADASYN, TomekLinks, EditedNearestNeighbors) and 5 Machine Learning models (LogisticRegressor, GaussianNB, RandomForestClassifier, DecisionTreeClassifier, GradientBoostingClassifier) to see which combination would give the highest precision score. After all iterations were concluded, the group discovered that the best model was the baseline (GradientBoosting, no hypertuning, no resampling) with a train precision of 84.47%, validation precision of 76.12%, and holdout precision of 80.85%.")

st.header("Baseline Model")
st.image('images/baseline.png')
#st.write

st.header("Oversampling Techniques") 
st.image('images/SMOTE.png')
st.caption("No Hypertuning, with SMOTE Oversampling")
st.image('images/ADASYN.png')
st.caption("No Hypertuning, with ADASYN Oversampling")
st.image('images/SMOTEN.png')
st.caption("No Hypertuning, with SMOTEN Oversampling")
st.image('images/oversampling_comparison.png')
st.caption("Comparison of Oversampling Methods")
st.image('images/oversampling.png')
st.caption("Comparison of Oversampling Methods")
st.write("Upon applying different oversampling techniques, accuracy and precision scores did not improve and even declined further. Notably, the LogisticRegressor's precision increased slightly with oversampling but remained low overall, while the RandomForestClassifier and GradientBoostingClassifier experienced significant drops in precision, indicating that these techniques were not effective in enhancing model performance.")
st.write("---")

st.header("Undersampling Techniques") 
st.image('images/EditedNearestNeighbors.png')
st.caption("No Hypertuning, with EditedNearestNeighbors Undersampling")
st.image('images/TomekLinks.png')
st.caption("No Hypertuning, with TomekLinks Undersampling")
st.image('images/undersampling_comparison.png')
st.caption("Comparison of Undersampling Methods")
st.image('images/undersampling.png')
st.caption("Comparison of Undersampling Methods")
st.write("Upon applying different undersampling techniques, accuracy and precision scores did not see significant improvements. However, TomekLinks stood out with the highest precision scores among the undersampling methods, even surpassing the results achieved with previous oversampling techniques.")
st.write("---")

st.image('images/final_comparison.png')
st.caption("Comparison of All Models")


