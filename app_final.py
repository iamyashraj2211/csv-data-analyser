import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CSV Data Analyser",
    layout="wide",
)
st.title("CSV Data Analyser")
st.write(
    "1. Upload a CSV file to analyze its data.",
    "2. Generate visualizations and insights from the uploaded data."
)
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    st.subheader("Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    total_rows, total_columns = df.shape
    missing_values = df.isnull().sum().sum()

    st.subheader("Data Summary")
    st.write(f"Total Rows: {total_rows}")
    st.write(f"Total Columns: {total_columns}")
    st.write(f"Missing Values: {missing_values}")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Column Names")
        st.write(df.columns.tolist())
    with col2:
        st.subheader("Data Types")
        st.write(df.dtypes)

    column_info = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str).values,
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(
        column_info,
        use_container_width=True,
        hide_index=True
    )