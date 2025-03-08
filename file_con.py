import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# Title of the app
st.title("CSV Data Cleaning and Visualization")

# File uploader allows user to upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the original DataFrame
    st.write("Original CSV data:")
    st.write(df)
    
    # Clean the data by removing rows with NaN values
    cleaned_df = df.dropna()
    
    # Display the cleaned DataFrame
    st.write("Cleaned CSV data (rows with NaN values removed):")
    st.write(cleaned_df)
    
    # Visualize the cleaned data
    st.write("Data Visualization:")
    
    # Example: Plot a histogram of the first numeric column
    if not cleaned_df.empty:
        numeric_columns = cleaned_df.select_dtypes(include=['float64', 'int64']).columns
        if len(numeric_columns) > 0:
            selected_column = st.selectbox("Select a column to visualize:", numeric_columns)
            fig, ax = plt.subplots()
            ax.hist(cleaned_df[selected_column], bins=20, edgecolor="black")
            ax.set_xlabel(selected_column)
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
        else:
            st.write("No numeric columns found for visualization.")
    else:
        st.write("No data left after cleaning.")
    
    # Convert the cleaned DataFrame to an XLSX file in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        cleaned_df.to_excel(writer, index=False)
    
    # Provide a download link for the cleaned XLSX file
    st.download_button(
        label="Download Cleaned XLSX file",
        data=output.getvalue(),  # Get the byte data from BytesIO
        file_name="cleaned_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.write("Please upload a CSV file to get started.")