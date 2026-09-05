import streamlit as st
import numpy as np
import pandas as pd

# Creating a title and heading
st.title(
    body = ":green[Weight] :blue[Wars]",
    text_alignment = "center"
)

st.divider()

# Manually inputing 
progress_df = pd.DataFrame(
        [["Eddy", 60],
        ["Don", 50]]
)

progress_df.columns = ["Player", "% to Goal"]


st.bar_chart(
    data = progress_df,
    x = "Player",
    y = "% to Goal",
    color = ["#FF0000"],
    horizontal = True,
    sort="-% to Goal", # putting a '-' in front of the column tells Streamlit to use descending order
    height=200
)