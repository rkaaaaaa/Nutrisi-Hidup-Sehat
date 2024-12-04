import streamlit as st
import pandas as pd

def show_data():
    st.title("Eksplorasi Dataset Nutrisi Makanan")
    
    file_path = "Food_Nutrition.csv"

    # Mengecek apakah data sudah ada di session state
    if "data" not in st.session_state:
        try:
            # Membaca file dengan penanganan otomatis untuk pemisah dan baris buruk
            data = pd.read_csv(file_path, sep=None, engine="python", on_bad_lines="skip")
            # Menyimpan data ke session state
            st.session_state.data = data
        except FileNotFoundError:
            st.error(f"File '{file_path}' tidak ditemukan. Pastikan file tersebut berada di lokasi yang benar.")
            return
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
            return

    # Menggunakan data dari session state
    data = st.session_state.data

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