import streamlit as st

st.title("Model Interpretability")
st.write("Since the final model chosen was GradientBoosting, Tree SHAP algorithms were used to interpret the results since SHAP is normally used to explain the output of ensemble tree models.")

st.image("images/shap_feature_importance.png", width=550)
st.caption("SHAP Feature Importance")
st.write("Feature importance is visualized here in the bar graph using the mean absolute shapley values. This shows the contribution of each feature to the model prediction. It can be observed that the top contributing features to our model are Sum, acc_hour, involved_motorcycle, while the the least contributing features are the involved_taxi, lanes_blocked, involved_pickup, involved_pedestrian and involved_rallyist, while the least contributing features are the involved_taxi, lanes_blocked, involved_pickup, involved_pedestrian and involved_rallyist.")
st.write("---")

st.image("images/beeswarm.png")
st.caption("SHAP Beeswarm Plot")
st.write("The Beeswarm Plot shows that high values of SUM contribute to the negative values of SHAP, meaning this will cause the prediction to be not_self_accident. If the values shown are low, this indicates that these features contribute to the prediction to be self_accident.")
st.write("---")

st.image("images/FP1.png")
st.caption("Force Plot for Datapoint 1 That Is a self_accident with One Involved Vehicle")
st.write("Sum feature is shown to havethe most substantial positive impact, pushing the prediction value to be significantly high. Involved_motorcycle also contributes positively but to a lesser extent than SUM.")
st.write("---")

st.image("images/FP2.png")
st.caption("Force Plot for Datapoint 2 That Is a non_self_accident with One Involved Vehicle")
st.write("acc_year, acc_month, and acc_day: Contribute positively but only slightly, countering the negative contributions to a small extent.")
st.write("---")

st.image("images/FP3.png")
st.caption("Force Plot for Datapoint 3 That Is a non_self_accident with Multiple Involved Vehicles")
st.write("---")
st.write("Involved_elf and Sum have nearly the same magnitude, almost cancelling it out, but more features with greater magnitudes of postive value bring down the SHAP value to ultimately result in a negative score, or predicted non_self_accident.")

st.title("Recommendations")
st.write("We recommend assessing high-risk areas by analyzing their physical and environmental conditions, such as road design, signage, traffic signals, pedestrian crossings, and weather. This evaluation identifies risk factors and enables targeted safety interventions, which are crucial for mitigating hazards and improving overall safety.")
st.write("Secondly, investigate top vehicles involved in self-accidents to gain further insights. For instance, there is a high occurrence of motorcycle self-accidents during the daytime on Commonwealth and C5, and buses at night on EDSA. Analyzing these patterns helps in understanding specific risk factors and developing targeted safety measures.")
st.write("Finally, we recommend checking for proper lighting in areas with high nighttime self-accident rates. Adequate illumination is crucial for visibility and can significantly reduce the risk of accidents. Ensuring well-lit streets helps improve safety for all road users.")
