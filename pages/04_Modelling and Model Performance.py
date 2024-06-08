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
st.caption("Visual Comparison of Oversampling Methods")
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
st.caption("Visual Comparison of Undersampling Methods")
st.write("Upon applying different undersampling techniques, accuracy and precision scores did not see significant improvements. However, TomekLinks stood out with the highest precision scores among the undersampling methods, even surpassing the results achieved with previous oversampling techniques.")
st.write("---")

st.header("Effect of Resampling and Hyperparameter Tuning on Precision Scores")
st.image('images/final_comparison.png')
st.caption("Comparison of Best Models")
st.write("After implementing TomekLinks as the resampling method and conducting GridSearchCV, variations in precision scores were observed across different model configurations. The baseline model, without resampling or hyperparameter tuning, exhibited the highest precision, with scores of 84.47% for training and 76.12% for validation, along with a holdout precision of 80.85%. Introducing hyperparameter tuning without resampling resulted in a decline in precision, particularly in training, where it dropped to 61.23%, while validation precision remained steady at 76.12%, maintaining a holdout precision of 80.85%. Models employing TomekLinks resampling, whether with or without hyperparameter tuning, maintained relatively high precision, with scores ranging from 74.52% to 83.76% for validation, showcasing the efficacy of this resampling technique in preserving precision. Despite minor fluctuations, the baseline model consistently demonstrated the highest precision across different datasets, suggesting its suitability for deployment.")


