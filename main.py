import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./data/day.csv", delimiter=",")

st.title("Demo Streamlit")

st.subheader("Streamlit Subheader")

st.table(df.head(10))

st.write(
    """
    # Test
    ## Test2
    ### Test3
    - List 1
    - List 2
    - List 3

    teks biasa aja
    """
)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
