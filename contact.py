import streamlit as st


def show_contact():
    st.title("Contact and About")

    st.header("About Me")
    st.write("Aplikasi web ini dibuat oleh Kelompok 5")
    st.write("Aplikasi ini dibuat untuk mem-visualisasi dan menganalisis data dari Makanan Bernutrisi untuk Program Diet.")

    st.header("Contact Information")
    st.write("Email:", "=")
    st.write("GitHub:", "https://github.com/rkaaaaaa/Nutrisi-Hidup-Sehat.git")
    st.write("Instagram:", "=")

    st.write("Seberapa suka anda dengan aplikasi saya?")
    st.slider("Geser untuk suka/tidak suka", 0, 100, 50)