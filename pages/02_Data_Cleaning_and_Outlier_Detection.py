import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats

st.title("Data Cleaning, Preprocessing, and Outlier Detection")
st.write("Here you can put each of your key results.")

df = pd.read_csv('data/involved_data_final.csv')

# Streamlit app
def main():
    st.title('Distribution of Latitude and Longitude')
    st.write('This app visualizes the distribution of latitude and longitude.')

    # Extract numerical columns
    numerical_cols = ['Latitude', 'Longitude']
    self_accident_quant = df[numerical_cols]

    # Set Seaborn style and color palette
    sns.set_style("whitegrid")
    sns.set_palette(["#7ABAFF", "#1D2371"])


    # Plotting the distributions
    fig, ax = plt.subplots(1, 2, figsize=(16, 4))
    fig.suptitle('Distribution', fontsize=16)

    # Distribution of Latitude
    sns.histplot(self_accident_quant["Latitude"], ax=ax[0], kde=True)  # Light blue histogram
    #sns.kdeplot(self_accident_quant["Latitude"], ax=ax[0], color="#1D2371", linewidth=2)  # Dark blue KDE curve
    ax[0].set_title('Distribution of Latitude')

    # Distribution of Longitude
    sns.histplot(self_accident_quant["Longitude"], ax=ax[1])  # Light blue histogram
    #sns.kdeplot(self_accident_quant["Longitude"], ax=ax[1], color="#1D2371", linewidth=2)  # Dark blue KDE curve
    ax[1].set_title('Distribution of Longitude')

    # Show the plot
    st.pyplot(fig)

if __name__ == '__main__':
    main()
