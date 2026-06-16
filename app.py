import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="IDRA Research Dashboard",
    layout="wide"
)

st.title("IDRA Research Dashboard")

st.write("Welcome to IDRA Research Dashboard")

uploaded_files = st.file_uploader(
    "Upload IDRA PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded")

    df = pd.DataFrame({
        "Filename": [f.name for f in uploaded_files]
    })

    st.dataframe(df)
