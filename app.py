import streamlit as st
import pandas as pd
import re

st.set_page_config(
    page_title="IDRA Research Dashboard",
    layout="wide"
)

st.title("IDRA Research Dashboard")

uploaded_files = st.file_uploader(
    "Upload IDRA PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    records = []

    for file in uploaded_files:

        filename = file.name

        match = re.search(
            r"(CDT-\d+)\s+(V\d+)",
            filename,
            re.IGNORECASE
        )

        if match:
            subject = match.group(1)
            visit = match.group(2)
        else:
            subject = ""
            visit = ""

        records.append({
            "Subject": subject,
            "Visit": visit,
            "Filename": filename
        })

    df = pd.DataFrame(records)

    st.subheader("Uploaded Files")

    st.dataframe(
        df,
        use_container_width=True
    )
