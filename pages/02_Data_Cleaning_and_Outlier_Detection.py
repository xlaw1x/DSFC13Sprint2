import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats

st.title("Data Cleaning, Preprocessing, and Outlier Detection")
st.write("Here you can put each of your key results.")

df = pd.read_csv('data/involved_data_final.csv')

# LATITUDE AND LONGITUDE OUTLIER PLOT
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

# LATITUDE OUTLIERS
def main():
    st.title('Outlier Detection for Latitude')
    st.write('This app detects outliers in the Latitude column.')

    # Outlier detection
    z_scores = stats.zscore(df['Latitude'])
    df['lat_zscore'] = abs(z_scores)

    # Filter outliers
    outliers = df[df['lat_zscore'] > 3]

    # Display outliers
    if not outliers.empty:
        st.write('Outliers Detected:')
        st.write(outliers['Latitude'])
    else:
        st.write('No outliers detected.')

if __name__ == '__main__':
    main()


#LONGITUDE OUTLIERS
# Streamlit app for outlier detection for Longitude
def main():
    st.title('Outlier Detection for Longitude')
    st.write('This app detects outliers in the Longitude column.')

    # Outlier detection
    z_scores = stats.zscore(df['Longitude'])
    df['lon_zscore'] = abs(z_scores)

    # Filter outliers
    outliers = df[df['lon_zscore'] > 3]

    # Display outliers
    if not outliers.empty:
        st.write('Outliers Detected in Longitude:')
        st.write(outliers['Longitude'])
    else:
        st.write('No outliers detected in Longitude.')

if __name__ == '__main__':
    main()





# ACCIDENTS PER YEAR AND MONTH OUTLIER PLOT
def main():
    st.title('Distribution of Accidents per Year or per Month')
    st.write('This app visualizes the distribution of accidents in timeframe.')

    # Extract numerical columns
    numerical_cols = ['acc_year', 'acc_month']
    self_accident_quant = df[numerical_cols]

    # Set Seaborn style and color palette
    sns.set_style("white")
    sns.set_palette(["#1D2371"])


    # Plotting the distributions
    fig, ax = plt.subplots(1, 2, figsize=(16, 4))
    fig.suptitle('Distribution', fontsize=16)

    # Distribution of Latitude
    sns.histplot(self_accident_quant["acc_year"], ax=ax[0], kde=True)
    ax[0].set_title('Distribution of Accidents per Year')

    # Distribution of Longitude
    sns.histplot(self_accident_quant["acc_month"], ax=ax[1], kde=True)
    ax[1].set_title('Distribution of Accidents per Month')

    # Show the plot
    st.pyplot(fig)

if __name__ == '__main__':
    main()
