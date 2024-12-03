import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def show_visualisasi():
    # Memuat file CSV langsung
    DATA_PATH = "Food_Nutrition.csv"

    # Pastikan delimiter sesuai dengan file Anda
    try:
        df = pd.read_csv(DATA_PATH, delimiter=',', encoding='utf-8')
    except pd.errors.ParserError:
        # Jika gagal, coba delimiter lain
        df = pd.read_csv(DATA_PATH, delimiter=';', encoding='utf-8')

    # Judul Aplikasi
    st.title("Visualisasi Data Nutrisi")

    # Dropdown untuk memilih visualisasi
    visualization_option = st.selectbox(
        "Pilih Visualisasi",
        ["Pilih", "Distribusi Usia", "Hubungan Berat dan Tinggi Badan", "Scatter Plot Interaktif", "Word Cloud"]
    )

    # Visualisasi berdasarkan pilihan
    if visualization_option == "Distribusi Usia":
        st.subheader("Histogram Distribusi Usia")
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.hist(df['Ages'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
        ax.set_xlabel('Usia', fontsize=14)
        ax.set_ylabel('Jumlah', fontsize=14)
        ax.set_title('Distribusi Usia', fontsize=16, fontweight='bold')
        ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
        st.pyplot(fig)

    elif visualization_option == "Hubungan Berat dan Tinggi Badan":
        st.subheader("Scatter Plot Berat vs Tinggi Badan")
        fig, ax = plt.subplots(figsize=(12, 8))
        scatter = ax.scatter(
            df['Weight'], df['Height'],
            c=df['Daily Calorie Target'], cmap='viridis', alpha=0.7, edgecolor='k'
        )
        ax.set_xlabel('Berat Badan (kg)', fontsize=14)
        ax.set_ylabel('Tinggi Badan (cm)', fontsize=14)
        ax.set_title('Hubungan Berat Badan dan Tinggi Badan', fontsize=16, fontweight='bold')
        ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
        
        # Tambahkan colorbar
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Target Kalori Harian', fontsize=12)
        st.pyplot(fig)

    elif visualization_option == "Scatter Plot Interaktif":
        st.subheader("Scatter Plot Interaktif")
        
        # Dropdown untuk memilih sumbu X dan Y
        x_axis = st.selectbox("Pilih Kolom untuk Sumbu X:", df.columns)
        y_axis = st.selectbox("Pilih Kolom untuk Sumbu Y:", df.columns)
        
        if st.button("Tampilkan Scatter Plot"):
            fig, ax = plt.subplots(figsize=(12, 8))
            scatter = ax.scatter(
                df[x_axis], df[y_axis], 
                alpha=0.7, edgecolor='k', color='purple'
            )
            ax.set_xlabel(x_axis, fontsize=14)
            ax.set_ylabel(y_axis, fontsize=14)
            ax.set_title(f"Scatter Plot {y_axis} vs {x_axis}", fontsize=16, fontweight='bold')
            ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
            st.pyplot(fig)

    elif visualization_option == "Word Cloud":
        st.subheader("Word Cloud dari Preferensi Diet")
        
        # Menggabungkan semua teks dari kolom Dietary Preference
        text = " ".join(df["Dietary Preference"].dropna().astype(str))
        
        # Membuat Word Cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        
        # Menampilkan Word Cloud
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        ax.set_title("Word Cloud: Preferensi Diet", fontsize=16, fontweight='bold')
        st.pyplot(fig)
