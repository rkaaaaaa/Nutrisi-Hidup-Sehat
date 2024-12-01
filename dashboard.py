import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer  

st.set_page_config(
    page_title="Analisis Makanan yang Bernutrisi untuk Hidup Sehat",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Home", "Data", "Visualization", "Machine Learning", "Contact"])

# Home Page
if page == "Home":
    st.title("Analisis Data Nutrisi Makanan :heart:")
    st.image("header.jpg", caption="Makanan Bernutrisi", use_container_width=True)  
    st.markdown("Selamat datang di Aplikasi Web Kelompok Data Analysis Makanan Bernutrisi! Explore and discover insights about Nutrition Food.")

#dashboard kami