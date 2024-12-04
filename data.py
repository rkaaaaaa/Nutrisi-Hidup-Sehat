import streamlit as st
import pandas as pd

def show_data():
    st.title("Eksplorasi Dataset Nutrisi Makanan")
    
file_path = "Food_Nutrition.csv"
    
try:
    # Membaca file dengan penanganan otomatis untuk pemisah dan baris buruk
    data = pd.read_csv(file_path, sep=None, engine="python", on_bad_lines="skip")
    
    # Menampilkan data yang dimuat
    st.subheader("Dataset yang Dimuat:")
    st.write(data)
    
    # Menampilkan informasi dataset
    st.subheader("Informasi Dataset:")
    st.write(f"Jumlah Baris dan Kolom: {data.shape}")
    st.write(f"Kolom dalam Dataset: {data.columns.tolist()}")
    
    # Statistik deskriptif
    st.subheader("Statistik Deskriptif:")
    st.write(data.describe(include="all"))
    
    # Preview kolom tertentu
    st.subheader("Preview Kolom Tertentu:")
    selected_columns = st.multiselect("Pilih Kolom:", data.columns.tolist())
    if selected_columns:
        st.write(data[selected_columns])
    else:
        st.info("Pilih kolom untuk melihat preview.")
    
    # Filter data
    st.subheader("Filter Data:")
    if data.select_dtypes(include="number").columns.any():
        numeric_columns = data.select_dtypes(include="number").columns.tolist()
        selected_filter_column = st.selectbox("Pilih Kolom Numerik:", numeric_columns)
        if selected_filter_column:
            min_val = float(data[selected_filter_column].min())
            max_val = float(data[selected_filter_column].max())
            filter_range = st.slider(
                f"Filter Nilai {selected_filter_column}:",
                min_value=min_val, max_value=max_val, value=(min_val, max_val),
            )
            filtered_data = data[
                (data[selected_filter_column] >= filter_range[0]) &
                (data[selected_filter_column] <= filter_range[1])
            ]
            st.write(filtered_data)
except FileNotFoundError:
    st.error(f"File '{file_path}' tidak ditemukan. Pastikan file tersebut berada di lokasi yang benar.")
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")