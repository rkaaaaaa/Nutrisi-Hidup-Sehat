import streamlit as st
from streamlit_option_menu import option_menu
import importlib

st.set_page_config(
    page_title="Analisis Makanan yang Bernutrisi untuk Hidup Sehat",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🥗"
)

# Tambahkan CSS untuk menyesuaikan tampilan
st.markdown(
    """
    <style>
    .css-1y0tads {
        margin-left: 0 !important; /* Navbar mentok ke kiri */
        margin-right: 0 !important; /* Navbar mentok ke kanan */
    }
    .nav-item {
        width: 100%; /* Menyesuaikan lebar setiap item */
        text-align: center; /* Memusatkan teks dalam menu */
    }
    </style>
    """,
    unsafe_allow_html=True
)

selected =  option_menu(
    menu_title=None,
    options=["Home", "Data", "Visualization", "Machine Learning", "About", "Contact"],
    icons=["house-heart-fill","bar-chart-fill","graph-up","search-heart-fill","info-circle-fill","file-person-fill"],
    orientation="horizontal",
    menu_icon="cast",
    default_index=0
)
if selected == "Home":
    Home = importlib.import_module("home")
    Home.show_home()
if selected == "Data":
    Data = importlib.import_module("data")
    Data.show_data()
if selected == "Visualization":
    Visualization = importlib.import_module("visualisasi")
    Visualization.show_visualisasi()
if selected == "About":
    About = importlib.import_module("about")
    About.show_about()
if selected == "Contact":
    Contact = importlib.import_module("contact")
    Contact.show_contact()
if selected == "Machine Learning":
    MachineLearning = importlib.import_module("MachineLearning")
    MachineLearning.show_machine()