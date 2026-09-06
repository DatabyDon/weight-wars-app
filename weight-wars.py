import streamlit as st
import numpy as np
import pandas as pd

# branding assets
from branding import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    ACCENT_COLOR,
    SECONDARY_ACCENT,
    BACKGROUND_COLOR,
    FONT_FAMILY,
    FONT_SIZE_LARGE,
    PADDING_LARGE,
)

# Apply the background color to the entire app
st.markdown(
    f"""
    <style>
    .stApp {{
        font-family: {FONT_FAMILY};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Creating a title
st.title(
    body = ":color[WEIGHT WARS]{foreground="+SECONDARY_ACCENT+"}",
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
    color = PRIMARY_COLOR,
    horizontal = True,
    sort="-% to Goal", # putting a '-' in front of the column tells Streamlit to use descending order
    height=200
)