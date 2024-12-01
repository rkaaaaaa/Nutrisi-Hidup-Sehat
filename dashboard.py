import streamlit as st
import importlib

st.set_page_config(
    page_title="Analisis Makanan yang Bernutrisi untuk Hidup Sehat",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🥗"
)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Home", "Data", "Visualization", "Machine Learning", "About", "Contact"])
if page == "Home":
    Home = importlib.import_module("home")
    Home.show_home()
if page == "About":
    About = importlib.import_module("about")
    About.show_about()