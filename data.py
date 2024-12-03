import streamlit as st
import pandas as pd


def show_data():
    st.title("Explorasi Dataset")

    file_path = "Food_Nutrition.csv"  # Pastikan file ini ada di direktori yang sama
    try:
        # Mencoba memuat dataset dengan berbagai delimiter
        try:
            data = pd.read_csv(file_path, delimiter=',')  # Coba menggunakan koma sebagai delimiter
        except pd.errors.ParserError:
            data = pd.read_csv(file_path, delimiter=';')  # Coba menggunakan titik koma jika gagal

        st.subheader("Dataset yang Dimuat:")
        st.write(data)

        st.subheader("Informasi Dataset:")
        
        # Cek integritas dataset
        if data.shape[1] > 1:  # Pastikan ada lebih dari satu kolom
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

    except pd.errors.ParserError:
        st.error(f"Terdapat kesalahan saat membaca file CSV. Periksa format dan delimiter file '{file_path}'.")
