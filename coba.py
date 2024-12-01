import streamlit as st
import pandas as pd

# Title of the app
st.title("Explorasi Dataset")

# Load the dataset from a local file
file_path = "Food_and_Nutrition__.csv"  # Pastikan file ini berada di direktori yang sama dengan script
try:
    data = pd.read_csv(file_path)
    
    # Display the dataset
    st.subheader("Dataset yang Dimuat:")
    st.write(data)
    
    # Show basic information about the dataset
    st.subheader("Informasi Dataset:")
    st.write(f"Jumlah Baris dan Kolom: {data.shape}")
    st.write(f"Kolom dalam Dataset: {data.columns.tolist()}")
    
    # Show descriptive statistics
    st.subheader("Statistik Deskriptif:")
    st.write(data.describe(include="all"))

except FileNotFoundError:
    st.error(f"File '{file_path}' tidak ditemukan. Pastikan file tersebut berada di direktori yang sama dengan script.")
