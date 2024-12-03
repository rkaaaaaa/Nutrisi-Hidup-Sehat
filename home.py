import streamlit as st
import random

def show_home():
    st.markdown("""
                <style>
                .title {
                    color: #1ABC9C;
                    text-align: center;
                    font-size: 3.5rem;
                    font-weight: bold;
                    background: linear-gradient(to right, #FF6B6B, #4ECDC4);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }
                .subtitle {
                    color: #34495E;
                    text-align: center;
                    font-size: 1.2rem;
                    margin-bottom: 30px;
                }
                .fact {
                    background-color: #2C3E50;
                    padding: 15px;
                    border-radius: 5px;
                    font-style: italic;
                    margin: 20px 0;
                    text-align: center;
                }
                </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="title">Smart Nutrition</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Aplikasi Prediksi Kesehatan dengan Data Gizi</div>', unsafe_allow_html=True)
    st.image("images/header.jpg", caption="Makanan Bernutrisi", use_container_width=True)  
                
    st.markdown("""
    ### Selamat Datang di Aplikasi Web Kelompok Data Analysis Makanan Bernutrisi!

    Kami hadir untuk membantu Anda memahami dan mengeksplorasi data nutrisi makanan. 
    Dengan teknologi analisis data terkini, kami menyediakan wawasan mendalam tentang 
    komposisi dan nilai gizi berbagai jenis makanan.
    """)

    fakta = [
        "Tahukah Anda? Mengonsumsi buah-buahan yang kaya akan serat, seperti apel dan pir, dapat membantu meningkatkan pencernaan.",
        "Makan sayuran hijau setiap hari dapat menurunkan risiko penyakit jantung.",
        "Air kelapa adalah minuman elektrolit alami terbaik.",
        "Mengonsumsi ikan berlemak seperti salmon mendukung kesehatan otak.",
        "Kacang-kacangan adalah sumber protein nabati yang sangat baik.",
        "Tahukah Anda? Buah jeruk kaya akan vitamin C yang meningkatkan daya tahan tubuh.",
        "Konsumsi oatmeal dapat membantu menurunkan kadar kolesterol jahat.",
        "Air lemon di pagi hari membantu detoksifikasi tubuh.",
        "Kandungan omega-3 pada ikan sangat baik untuk otak dan jantung."
    ]
    st.markdown(f'<div class="fact"> 💡FYI : {random.choice(fakta)}</div>', unsafe_allow_html=True)

    st.header("Galeri Nutrisi Diet")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="nutrition-images">', unsafe_allow_html=True)
        st.image("images/food.jpeg", caption="Menu Seimbang") 
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="nutrition-images">', unsafe_allow_html=True)
        st.image("images/food3.jpeg", caption="Salad segar") 
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="nutrition-images">', unsafe_allow_html=True)
        st.image("images/food2.jpeg", caption="Hidangan Sehat") 
        st.markdown('</div>', unsafe_allow_html=True)
