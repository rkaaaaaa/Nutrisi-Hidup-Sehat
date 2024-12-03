import streamlit as st
import pandas as pd

st.title("Explorasi Dataset")

file_path = "Food_and_Nutrition__.csv"  # Make sure this file exists in the same directory
try:
    # Load dataset
    data = pd.read_csv(file_path)

    st.subheader("Dataset yang Dimuat:")
    st.write(data)

    st.subheader("Informasi Dataset:")
    
    # Check dataset integrity
    if data.shape[1] > 1:  # Ensures there are multiple columns
        st.write(f"Jumlah Baris dan Kolom: {data.shape}")
        st.write(f"Kolom dalam Dataset: {data.columns.tolist()}")
    else:
        st.warning("Dataset tidak memiliki kolom yang valid atau data yang terpisah.")

    st.subheader("Statistik Deskriptif:")
    if not data.empty:
        st.write(data.describe(include="all"))
    else:
        st.error("Dataset kosong. Tidak ada data untuk dianalisis.")

except FileNotFoundError:
    st.error(f"File '{file_path}' tidak ditemukan. Pastikan file tersebut berada di direktori yang sama dengan script.")

except pd.errors.EmptyDataError:
    st.error("File CSV kosong. Mohon periksa isi file.")