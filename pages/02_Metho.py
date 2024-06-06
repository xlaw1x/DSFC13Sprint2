import matplotlib as plt
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sn
# from wordcloud import WordCloud
# from nltk.corpus import stopwords
# import nltk

st.title("Hello world YAY!")

df = pd.read_csv('data/involved_data_final.csv')
#st.dataframe(df)

Add some matplotlib code !
fig, ax = plt.subplots()
df.hist(
  bins=8,
  column="Type",
  grid=False,
  figsize=(8, 8),
  color="#86bf91",
  zorder=2,
  rwidth=0.9,
  ax=ax,
)
st.write(fig)

# numerical_df=df
# #fig, ax = plt.subplots()
# fraud_map = {0: 'multiple_accident', 1: 'self_accident'}
# numerical_df_eda = numerical_df.copy()
# numerical_df_eda['Class'] = numerical_df_eda['is_self_accident'].map(fraud_map)

# fig, ax = plt.subplots(figsize=(8, 6))
# ax = sns.countplot(x=numerical_df_eda['Class'],
#               order=numerical_df_eda['Class'].value_counts().index,
#               color='skyblue')
# ax.set_xlabel(' ')
# ax.set_ylabel(' ')
# for spine in ['right', 'top']:
#     ax.spines[spine].set_visible(False)
# ax.set_title(f'Distribution of Vehicular Accidents in Metro Manila', size=15, y=1)
# display(numerical_df_eda['Class'].value_counts())
# plt.show()
#st.write(fig)
