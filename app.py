import streamlit as st
import pandas as pd
import re
import pdfplumber

st.set_page_config(
    page_title="IDRA Research Dashboard",
    layout="wide"
)

st.title("IDRA Research Dashboard")

def extract_idra_data(uploaded_file):

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += "\n" + page_text

    filename = uploaded_file.name

    subject = ""
    visit = ""

    match = re.search(
        r"(CDT-\d+)\s+(V\d+)",
        filename,
        re.IGNORECASE
    )

    if match:
        subject = match.group(1)
        visit = match.group(2)

    result = {
        "Subject": subject,
        "Visit": visit,
        "Filename": filename
    }

    nibut_matches = re.findall(
        r'following time:\s*([\d.]+).*?average time:\s*([\d.]+)',
        text,
        re.DOTALL
    )

    if len(nibut_matches) >= 2:
        result["FNIBUT_OD"] = nibut_matches[0][0]
        result["ANIBUT_OD"] = nibut_matches[0][1]

        result["FNIBUT_OS"] = nibut_matches[1][0]
        result["ANIBUT_OS"] = nibut_matches[1][1]

    return result

uploaded_files = st.file_uploader(
    "Upload IDRA PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    rows = []

    for file in uploaded_files:
        rows.append(
            extract_idra_data(file)
        )

    df = pd.DataFrame(rows)

    st.subheader("Extracted IDRA Data")

    st.dataframe(
        df,
        use_container_width=True
    )
