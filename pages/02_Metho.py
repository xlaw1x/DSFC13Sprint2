import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st

st.title("Hello world YAY!")

df = pd.read_csv('data/cc_rfm.csv')
st.dataframe(df)

# Add some matplotlib code !
fig, ax = plt.subplots()
df.hist(
  bins=8,
  column="recency",
  grid=False,
  figsize=(8, 8),
  color="#86bf91",
  zorder=2,
  rwidth=0.9,
  ax=ax,
)
st.write(fig)

