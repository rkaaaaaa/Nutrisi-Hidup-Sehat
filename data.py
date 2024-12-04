import streamlit as st
import pandas as pd

st.title("Explorasi Dataset")

file_path = "Food_and_Nutrition__.csv"  
try:
    data = pd.read_csv(file_path)
    
    st.subheader("Dataset yang Dimuat:")
    st.write(data)
    
    st.subheader("Informasi Dataset:")
    st.write(f"Jumlah Baris dan Kolom: {data.shape}")
    st.write(f"Kolom dalam Dataset: {data.columns.tolist()}")
    
    st.subheader("Statistik Deskriptif:")
    st.write(data.describe(include="all"))

except FileNotFoundError:
    st.error(f"File '{file_path}' tidak ditemukan. Pastikan file tersebut berada di direktori yang sama dengan script.")