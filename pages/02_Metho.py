import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
# from wordcloud import WordCloud
# from nltk.corpus import stopwords
# import nltk

st.title("Exploratory Data Analysis")

df = pd.read_csv('data/involved_data_final.csv')
# st.dataframe(df)


# SELF ACCIDENT VS NOT SELF ACCIDENT
fraud_map = {0: 'is_not_self_accident', 1: 'self_accident'}
df['Class'] = df['is_self_accident'].map(fraud_map)

# Plotting function
def plot_graph(data):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x=data['Class'],
                  order=data['Class'].value_counts().index,
                  color='#1D2371')
    plt.xlabel(' ')
    plt.ylabel(' ')
    for spine in ['right', 'top']:
        ax.spines[spine].set_visible(False)
    plt.title('Distribution of Vehicular Accidents in Metro Manila', size=15, y=1)
    st.pyplot(fig)

# Streamlit app
def main():
    st.header('Vehicular Accidents in Metro Manila')
    st.write('This app visualizes the distribution of vehicular accidents.')

    # Display the DataFrame
    st.write('Data:')
    st.write(df['Class'].value_counts())

    # Plot the graph
    st.write('Graph:')
    plot_graph(df)

if __name__ == '__main__':
    main()


# TOP CITIES WHERE ACCIDENTS OCCUR
# Function to plot bar chart
def plot_bar_chart(df):
    top_cities = df['City'].value_counts().head(8)
    df_sorted = df[df['City'].isin(top_cities.index)]

  # Create color list
    colors = ['lightgray'] * len(top_cities)  # Changed color to #1D2371
    for idx, city in enumerate(top_cities.index):
        if city in top_cities.index[:3]:
            colors[idx] = '#1D2371'

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_cities.index, top_cities.values, color=colors)
    ax.set_xlabel('Number of Accidents')
    ax.set_ylabel('City')
    ax.set_title('Top Cities Where Accidents Occur')
    ax.invert_yaxis()  # To display from highest to lowest
    for spine in ['right', 'top']:
        ax.spines[spine].set_visible(False)
    st.pyplot(fig)

# Streamlit app
def main():
    st.header('Accidents Occurrence by City')
    st.write('This app visualizes the top cities where accidents occur.')

    # Plot the bar chart
    st.write('Bar Chart:')
    plot_bar_chart(df)

if __name__ == '__main__':
    main()

# ACCIDENTS PER DIRECTION
# Function to plot bar chart
def plot_bar_chart(df):
    direction_counts = df['Direction'].value_counts()

    colors = ['lightgray'] * 5  # Default color of other directions
    colors[idx][:2] = ['#1D2371'] * 2  # Change color for NB and SB

    fig, ax = plt.subplots(figsize=(10, 6))
    direction_counts.plot(kind='bar', color=colors, ax=ax)

    # Customizing the plot
    ax.set_xlabel('Direction')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Direction')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)

# Streamlit app
def main():
    st.title('Accidents by Direction')
    st.write('This app visualizes the number of accidents by direction.')

    # Display the DataFrame
    st.write('Data:')
    st.write(df)

    # Plot the bar chart
    st.write('Bar Chart:')
    plot_bar_chart(df)

if __name__ == '__main__':
    main()
