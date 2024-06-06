import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats

st.title("Data Cleaning, Preprocessing, and Outlier Detection")
st.write("Here you can put each of your key results.")

df = pd.read_csv('data/involved_data_final.csv')

# LATITUDE & LONGITUDE
def main():
    st.title('Distribution of Latitude and Longitude')
    st.write('This app visualizes the distribution of latitude and longitude.')

    # Extract numerical columns
    numerical_cols = ['Latitude', 'Longitude']
    self_accident_quant = df[numerical_cols]

    # Set Seaborn style and color palette
    sns.set_style("white")
    sns.set_palette(["#7ABAFF", "#1D2371"])


    # Plotting the distributions
    fig, ax = plt.subplots(1, 2, figsize=(16, 4))
    fig.suptitle('Distribution', fontsize=16)

    # Distribution of Latitude
    sns.histplot(self_accident_quant["Latitude"], ax=ax[0], kde=True)
    ax[0].set_title('Distribution of Latitude')

    # Distribution of Longitude
    sns.histplot(self_accident_quant["Longitude"], ax=ax[1], kde=True)
    ax[1].set_title('Distribution of Longitude')

    # Show the plot
    st.pyplot(fig)

if __name__ == '__main__':
    main()

# Streamlit app
def main():
    st.title('Outlier Detection for Latitude and Longitude')
    st.write('This app detects outliers in the Latitude and Longitude columns.')

    # Display the DataFrame
    st.write('Data:')
    st.write(df)

    # Extract Latitude and Longitude columns
    lat_lon_df = df[['Latitude', 'Longitude']]

    # Outlier detection
    z_scores = stats.zscore(lat_lon_df)
    lat_lon_df['lat_zscore'] = abs(z_scores[:, 0])  # Z-scores for Latitude
    lat_lon_df['lon_zscore'] = abs(z_scores[:, 1])  # Z-scores for Longitude

    # Filter outliers
    outliers = lat_lon_df[(lat_lon_df['lat_zscore'] > 3) | (lat_lon_df['lon_zscore'] > 3)]

    # Display outliers
    if not outliers.empty:
        st.write('Outliers Detected:')
        st.write(outliers)
    else:
        st.write('No outliers detected.')

if __name__ == '__main__':
    main()
