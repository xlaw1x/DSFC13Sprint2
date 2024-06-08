import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
# from wordcloud import WordCloud
# from nltk.corpus import stopwords
# import nltk

st.title("Exploratory Data Analysis")
st.subheader("In this section we will explore the")

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
    
    # Display the DataFrame
    st.write('Data:')
    st.write(df['Class'].value_counts())

    # Plot the graph
    st.write('Graph:')
    plot_graph(df)

if __name__ == '__main__':
    main()

st.write('The graph above shows the distribution of vehicular accidents between two categories: is_not_self_accident (98.47% majority) and is_self_accident (1.53% minority), a highly imbalanced dataset. So where do these accidents usually occur?')


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
    
    # Plot the bar chart
    plot_bar_chart(df)

if __name__ == '__main__':
    main()

st.write('When accounting for all accidents, we can see that Quezon City tops as the city with the most recorded accidents, followed by Mandaluyong and Makati City.')
st.image("images/distribution_of_vehicles.png")
st.write('However, when we filter this to self-accidents however, we can see that Quezon City still tops the list, but this time followed by Makati and Pasig City. I wonder which roads do these accidents occur most often?')
st.write('---')
         
# TOP LOCATIONS WHERE ACCIDENTS OCCUR
# Function to plot bar chart
def plot_bar_chart(df):
    top_cities = df['Location'].value_counts().head(10)

    colors = ['lightgray'] * len(top_cities)
    top_cities_index = top_cities.index[:3]
    for idx in range(len(colors)):
        if idx < 3:
            colors[idx] = '#1D2371'  # Change to #1D2371 for the top 3 cities

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_cities.index, top_cities.values, color=colors)
    for spine in ['right', 'top']:
        ax.spines[spine].set_visible(False)

    plt.xlabel('Number of Accidents')
    plt.ylabel('Location')
    plt.title('Top Locations Where Accidents Occur')
    plt.gca().invert_yaxis()  # To display from highest to lowest
    st.pyplot(fig)

# Streamlit app
def main():
    st.header('Top Accident Locations')

    # Plot the bar chart
    plot_bar_chart(df)

if __name__ == '__main__':
    main()

st.write('When it comes to identifying more specific road areas, we can observe that EDSA is a hotspot for accidents, specifically Shaw, Guadalupe, and Megamall.')
st.image("images/top_cities.png")
st.write('But when we check the road areas where self-accidents occur, we can see that most self-accidents actually occur along C5 Road.')
st.write('---')

# ACCIDENTS PER DIRECTION
# Function to plot bar chart
def plot_bar_chart(df):
    direction_counts = df['Direction'].value_counts()

    colors = ['lightgray'] * 5  # Default color of other directions
    colors[:2] = ['#1D2371'] * 2  # Change color for NB and SB

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
    st.header('Accidents by Direction')

    # Plot the bar chart
    plot_bar_chart(df)

if __name__ == '__main__':
    main()

st.write('The North-bound and South-bound lanes are found to have the most accident occurences, because these are the roads located in the cities with the most accidents, such as Commonwealth in Quezon City or EDSA in Mandaluyong.')

#ACCIDENTS PER TIME OF DAY
# Function to plot bar chart
def plot_bar_chart(df):
    part_of_day_counts = df['part_of_day'].value_counts().sort_values(ascending=False)

    colors = ['lightgray'] * 5  # Default color for all parts of the day
    colors[:1] = ['#1D2371'] * 1  # Change color for morning

    fig, ax = plt.subplots(figsize=(10, 6))
    part_of_day_counts.plot(kind='bar', color=colors, ax=ax)

    # Customizing the plot
    ax.set_xlabel('Time of Day')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Time of Day')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)

# Streamlit app
def main():
    st.header('Accidents by Time of Day')

    # Plot the bar chart
    plot_bar_chart(df)

if __name__ == '__main__':
    main()

st.write('The bar graph above shows that most accidents occur in the morning, but why is that? The succeeding graph showing the distribution of accidents throughout hours of the day can help shed more light on this.')

#ACCIDENTS THROUGHOUT THE DAY
# Function to plot line chart
def plot_line_chart(df):
    hour_counts = df['acc_hour'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    hour_counts.plot(kind='line', color='#1D2371', marker='o', ax=ax)  # Use #1D2371 as line color

    # Customizing the plot
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Hour of the Day')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticks(hour_counts.index)  # Set the tick positions to match the hour values
    ax.set_xticklabels(hour_counts.index)  # Set the tick labels to display the hour values
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)

# Streamlit app
def main():
    st.header('Accidents by Hour of the Day')

    # Plot the line chart
    plot_line_chart(df)

if __name__ == '__main__':
    main()
    
st.write('This time-series plot shows the spike in accidents between 5 and 10 am, which is commonly known as rush hour in the Philippines. Vehicles rushing to work are likely to speed or have less focus or patience on the road, resulting in accidents.')

# ACCIDENTS PER DAY OF THE WEEK
# Maps integer value to string value of trans_weekday
weekday_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
df['acc_weekday'] = df['acc_weekday'].map(weekday_map)

# Function to plot bar chart
def plot_bar_chart(df):
    weekday_counts = df['acc_weekday'].value_counts()

    colors_mc = ['lightgray'] * len(weekday_counts)
    colors_mc[:3] = ['#1D2371'] * 3  # Change color for top 3 weekdays

    fig, ax = plt.subplots(figsize=(10, 6))
    weekday_counts.plot(kind='bar', color=colors_mc, ax=ax)

    # Customizing the plot
    ax.set_xlabel('Day of the week')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Day of the week')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)

# Streamlit app
def main():
    st.header('Accidents by Day of the Week')

    # Plot the bar chart
    plot_bar_chart(df)

if __name__ == '__main__':
    main()

st.write('Accidents per day of the week are not too widely spread, with the exception of Sunday, which is when there is noticably less traffic and vehicles on the road, a factor that could contribute to less accidents occuring on Sundays.')

# ACCIDENTS PER MONTH
# Function to plot bar chart
def plot_bar_chart(df):
    accidents_per_month = df['acc_month'].value_counts().sort_index()

    colors = ['lightgray'] * 12  # Default color for all months
    colors[8:11] = ['#1D2371'] * 3  # Change color for September, October, and November

    fig, ax = plt.subplots(figsize=(10, 6))
    accidents_per_month.plot(kind='bar', color=colors, ax=ax)

    # Customizing the plot
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Month')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=0)
    st.pyplot(fig)

# Streamlit app
def main():
    st.header('Accidents by Month')
    st.write('This app visualizes the number of accidents by month.')

    # Plot the bar chart
    plot_bar_chart(df)

if __name__ == '__main__':
    main()


# ACCIDENTS PER YEAR
# Calculate accidents per month per year
accidents_per_month_year = df.groupby(['acc_year', 'acc_month']).size().unstack(fill_value=0)

# Define colors for each year
colors = ['#1D2371', '#7ABAFF', '#4D4DFF']  # Shades of blue

# Streamlit app
def main():
    st.header('Accidents by Month for Different Years')
    st.write('This app visualizes the number of accidents by month for different years.')

    # Plotting the data
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotting the line graph for each year
    for year, color in zip(accidents_per_month_year.index, colors):
        ax.plot(accidents_per_month_year.columns, accidents_per_month_year.loc[year], marker='o', label=year, color=color)

    # Customizing the plot
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Number of Accidents by Month for Different Years')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticks(accidents_per_month_year.columns)
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=0)

    plt.legend(title='Year')
    plt.grid(True)
    st.pyplot(fig)

if __name__ == '__main__':
    main()

st.title('All Road Accidents vs Self-accidents')
st.write('Now take a look at a side-by-side comparison of all road accidents to self-accidents.')



st.image("images/distribution_of_vehicles.png")
