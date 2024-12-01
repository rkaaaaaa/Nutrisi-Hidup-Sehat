import streamlit as st
import importlib

st.set_page_config(
    page_title="Analisis Makanan yang Bernutrisi untuk Hidup Sehat",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Home", "Data", "Visualization", "Machine Learning", "Contact"])
if page == "Data":
    Data = importlib.import_module("niken")
    Data.show_niken()

# Home Page
if page == "Home":
    st.title("Analisis Data Nutrisi Makanan :heart:")
    st.image("header.jpg", caption="Makanan Bernutrisi", use_container_width=True)  
    st.markdown("Selamat datang di Aplikasi Web Kelompok Data Analysis Makanan Bernutrisi! Explore and discover insights about Nutrition Food.")

    # poster gambar
    st.header("Nutrisi Diet")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("food.jpeg", caption="Gambar 1") 
    with col2:
        st.image("food2.jpeg", caption="Gambar 2") 
    with col3:
        st.image("food3.jpeg", caption="Gambar 3") 