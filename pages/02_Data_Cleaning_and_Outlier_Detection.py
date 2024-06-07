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
    sns.set_palette(["#1D2371"])


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
        st.write('Number of Latitude Outliers Detected:', len(outliers))
        min_outlier = outliers['Latitude'].min()
        max_outlier = outliers['Latitude'].max()
        st.write('Range of Outlier Values: [{}, {}]'.format(round(min_outlier, 3), round(max_outlier, 3)))
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
        st.write('Number of Longitude Outliers Detected:', len(outliers))
        min_outlier = outliers['Longitude'].min()
        max_outlier = outliers['Longitude'].max()
        st.write('Range of Outlier Values: [{}, {}]'.format(round(min_outlier, 3), round(max_outlier, 3)))
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

#YEAR OUTLIERS
# Streamlit app for outlier detection for Longitude
def main():
    st.title('Outlier Detection for YEAR')
    st.write('This app detects outliers in the acc_year column.')

    # Outlier detection
    z_scores = stats.zscore(df['acc_year'])
    df['acc_year_zscore'] = abs(z_scores)

    # Filter outliers
    outliers = df[df['acc_year_zscore'] > 3]

    # Display outliers
    if not outliers.empty:
        st.write('Number of Outliers Detected in Year:', len(outliers))
        min_outlier = outliers['acc_year'].min()
        max_outlier = outliers['acc_year'].max()
        st.write('Range of Outlier Values: [{}, {}]'.format(round(min_outlier, 3), round(max_outlier, 3)))
        st.write(outliers['acc_year'])
    else:
        st.write('No outliers detected in Year.')

if __name__ == '__main__':
    main()

#MONTH OUTLIERS
# Streamlit app for outlier detection for Longitude
def main():
    st.title('Outlier Detection for Month')
    st.write('This app detects outliers in the Month column.')

    # Outlier detection
    z_scores = stats.zscore(df['acc_month'])
    df['acc_month_zscore'] = abs(z_scores)

    # Filter outliers
    outliers = df[df['acc_month_zscore'] > 3]

    # Display outliers
    if not outliers.empty:
        st.write('Number of Outliers Detected in Month:', len(outliers))
        min_outlier = outliers['acc_month'].min()
        max_outlier = outliers['acc_month'].max()
        st.write('Range of Outlier Values: [{}, {}]'.format(round(min_outlier, 3), round(max_outlier, 3)))
        st.write(outliers['acc_month'])
    else:
        st.write('No outliers detected in Month.')

if __name__ == '__main__':
    main()


# ACCIDENTS PER DAY AND WEEKDAY OUTLIER PLOT
def main():
    st.title('Distribution of Accidents per Day or per Weekday')
    st.write('This app visualizes the distribution of accidents in timeframe.')

    # Extract numerical columns
    numerical_cols = ['acc_day', 'acc_weekday']
    self_accident_quant = df[numerical_cols]

    # Set Seaborn style and color palette
    sns.set_style("white")
    sns.set_palette(["#1D2371"])


    # Plotting the distributions
    fig, ax = plt.subplots(1, 2, figsize=(16, 4))
    fig.suptitle('Distribution', fontsize=16)

    # Distribution of Latitude
    sns.histplot(self_accident_quant["acc_day"], ax=ax[0], kde=True)
    ax[0].set_title('Distribution of Accidents per Day of the Month')

    # Distribution of Longitude
    sns.histplot(self_accident_quant["acc_weekday"], ax=ax[1], kde=True)
    ax[1].set_title('Distribution of Accidents per Weekday')

    # Show the plot
    st.pyplot(fig)

if __name__ == '__main__':
    main()

# DAY OUTLIERS
def main():
    st.title('Outlier Detection for Day of the Month')

    # Outlier detection
    z_scores = stats.zscore(df['acc_day'])
    df['acc_day_zscore'] = abs(z_scores)

    # Filter outliers
    outliers = df[df['acc_day_zscore'] > 3]

    # Display outliers
    if not outliers.empty:
        st.write('Number Outliers Detected in Day of the Month:', len(outliers))
        min_outlier = outliers['acc_day'].min()
        max_outlier = outliers['acc_day'].max()
        st.write('Range of Outlier Values: [{}, {}]'.format(round(min_outlier, 3), round(max_outlier, 3)))
        st.write(outliers['acc_day'])
    else:
        st.write('No outliers detected.')

if __name__ == '__main__':
    main()

# WEEKDAY OUTLIERS
def main():
    st.title('Outlier Detection for Weekday')
    st.write('This app detects outliers in the Weekday column.')

    # Outlier detection
    z_scores = stats.zscore(df['acc_weekday'])
    df['acc_weekday_zscore'] = abs(z_scores)

    # Filter outliers
    outliers = df[df['acc_weekday_zscore'] > 3]

    # Display outliers
    if not outliers.empty:
        st.write('Number of Weekday Outliers Detected:', len(outliers))
        min_outlier = outliers['acc_weekday'].min()
        max_outlier = outliers['acc_weekday'].max()
        st.write('Range of Outlier Values: [{}, {}]'.format(round(min_outlier, 3), round(max_outlier, 3)))
        st.write(outliers['acc_weekday'])
    else:
        st.write('No outliers detected.')

if __name__ == '__main__':
    main()


# ACCIDENTS PER HOUR AND DIRECTION NUMERIC OUTLIER PLOT
def main():
    st.title('Distribution of Accidents per Hour or per Road Direction')

    # Extract numerical columns
    numerical_cols = ['acc_hour', 'Direction_Numeric']
    self_accident_quant = df[numerical_cols]

    # Set Seaborn style and color palette
    sns.set_style("white")
    sns.set_palette(["#1D2371"])


    # Plotting the distributions
    fig, ax = plt.subplots(1, 2, figsize=(16, 4))
    fig.suptitle('Distribution', fontsize=16)

    # Distribution of Latitude
    sns.histplot(self_accident_quant["acc_hour"], ax=ax[0], kde=True)
    ax[0].set_title('Distribution of Accidents per Hour')

    # Distribution of Longitude
    sns.histplot(self_accident_quant["Direction_Numeric"], ax=ax[1], kde=True)
    ax[1].set_title('Distribution of Accidents per Road Direction')

    # Show the plot
    st.pyplot(fig)

if __name__ == '__main__':
    main()

# HOUR OUTLIERS
def main():
    st.title('Outlier Detection for Hour')

    # Outlier detection
    z_scores = stats.zscore(df['acc_hour'])
    df['acc_hour_zscore'] = abs(z_scores)

    # Filter outliers
    outliers = df[df['acc_hour_zscore'] > 3]

    # Display outliers
    if not outliers.empty:
        st.write('Number Outliers Detected in Hour:', len(outliers))
        min_outlier = outliers['acc_hour'].min()
        max_outlier = outliers['acc_hour'].max()
        st.write('Range of Outlier Values: [{}, {}]'.format(round(min_outlier, 3), round(max_outlier, 3)))
        st.write(outliers['acc_hour'])
    else:
        st.write('No outliers detected.')

if __name__ == '__main__':
    main()

# DIRECTION OUTLIERS
def main():
    st.title('Outlier Detection for Road Direction')

    # Outlier detection
    z_scores = stats.zscore(df['Direction_Numeric'])
    df['Direction_Numeric_zscore'] = abs(z_scores)

    # Filter outliers
    outliers = df[df['Direction_Numeric_zscore'] > 3]

    # Display outliers
    if not outliers.empty:
        st.write('Number of Road Direction Outliers Detected:', len(outliers))
        min_outlier = outliers['Direction_Numeric'].min()
        max_outlier = outliers['Direction_Numeric'].max()
        st.write('Range of Outlier Values: [{}, {}]'.format(round(min_outlier, 3), round(max_outlier, 3)))
        st.write(outliers['Direction_Numeric'])
    else:
        st.write('No outliers detected.')

if __name__ == '__main__':
    main()


df_sum = pd.read_csv('data/involved_data_final_TEST.csv')

# ACCIDENTS PER LANES BLOCKED AND SUM OUTLIER PLOT
def main():
    st.title('Distribution of Accidents per Number of Lanes Blocked and per Sum of Vehicles Involved')

    # Extract numerical columns
    numerical_cols = ['Lanes_Blocked', 'Sum']
    self_accident_quant = df_sum[numerical_cols]

    # Set Seaborn style and color palette
    sns.set_style("white")
    sns.set_palette(["#1D2371"])


    # Plotting the distributions
    fig, ax = plt.subplots(1, 2, figsize=(16, 4))
    fig.suptitle('Distribution', fontsize=16)

    # Distribution of Lanes_Blocked
    sns.histplot(self_accident_quant["Lanes_Blocked"], ax=ax[0], kde=True)
    ax[0].set_title('Distribution of Accidents per Number of Lanes Blocked')

    # Distribution of Sum
    sns.histplot(self_accident_quant["Sum"], ax=ax[1], kde=True)
    ax[1].set_title('Distribution of Accidents per Sum of Vehicles Involved')

    # Show the plot
    st.pyplot(fig)

if __name__ == '__main__':
    main()

# LANES BLOCKED OUTLIERS
def main():
    st.title('Outlier Detection for Day of the Month')

    # Outlier detection
    z_scores = stats.zscore(df_sum['Lanes_Blocked'])
    df_sum['Lanes_Blocked_zscore'] = abs(z_scores)

    # Filter outliers
    outliers = df_sum[df_sum['Lanes_Blocked_zscore'] > 3]

    # Display outliers
    if not outliers.empty:
        st.write('Number Outliers Detected in Number of Lanes Blocked:', len(outliers))
        min_outlier = outliers['Lanes_Blocked'].min()
        max_outlier = outliers['Lanes_Blocked'].max()
        st.write('Range of Outlier Values: [{}, {}]'.format(round(min_outlier, 3), round(max_outlier, 3)))
        st.write(outliers['Lanes_Blocked'])
    else:
        st.write('No outliers detected.')

if __name__ == '__main__':
    main()

# SUM OUTLIERS
def main():
    st.title('Outlier Detection for Sum of Vehicles Involved')

    # Outlier detection
    z_scores = stats.zscore(df_sum['Sum'])
    df_sum['Sum_zscore'] = abs(z_scores)

    # Filter outliers
    outliers = df_sum[df_sum['Sum_zscore'] > 3]

    # Display outliers
    if not outliers.empty:
        st.write('Number of Sum Outliers Detected:', len(outliers))
        min_outlier = outliers['Sum'].min()
        max_outlier = outliers['Sum'].max()
        st.write('Range of Outlier Values: [{}, {}]'.format(round(min_outlier, 3), round(max_outlier, 3)))
        st.write(outliers['Sum'])
    else:
        st.write('No outliers detected.')

if __name__ == '__main__':
    main()

