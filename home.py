import streamlit as st
import random

def show_home():
    st.markdown("""
    <style>
    .title {
        font-size: 4rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(to right, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    .subtitle {
        color: #34495E;
        text-align: center;
        font-size: 1.8rem;
        font-weight: 300;
        margin-bottom: 30px;
    }             
    .footer {
        text-align: center;
        font-size: 0.9rem;
        margin-top: 50px;
        color: #888888;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Smart Nutrition</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Prediksi Kesehatan Melalui Analisis Gizi</div>', unsafe_allow_html=True)

    st.image("images/header.jpg", caption="Makanan Bernutrisi", use_container_width=True)
   
    st.markdown("""
    ### 🌟 Selamat Datang di Dunia Nutrisi Cerdas!

    Kami memadukan teknologi canggih dengan pengetahuan gizi untuk memberikan wawasan mendalam 
    tentang kesehatan Anda. Melalui analisis data komprehensif, kami membantu Anda membuat 
    keputusan diet yang lebih baik dan cerdas.
    """)

    nutrition_facts = [
        "💡 Konsumsi 5 porsi buah dan sayur setiap hari dapat mengurangi risiko penyakit kronis.",
        "🥦 Sayuran hijau mengandung antioksidan yang melindungi sel dari kerusakan.",
        "🥥 Air kelapa minuman alami kaya elektrolit dan nutrisi.",
        "🐟 Ikan berlemak adalah sumber omega-3 terbaik untuk kesehatan otak.",
        "🥜 Kacang-kacangan sumber protein nabati dengan lemak sehat.",
        "🍊 Vitamin C membantu sistem kekebalan tubuh dan produksi kolagen.",
        "🥣 Oatmeal membantu menurunkan kolesterol dan menjaga kesehatan jantung.",
        "🍋 Minum air lemon pagi hari mendukung metabolisme dan detoksifikasi.",
        "🥗 Diet seimbang kunci utama kesehatan dan kebugaran optimal!"
    ]
    st.markdown(f'<div style="background: linear-gradient(to right, #FF6B6B, #4ECDC4); color: #FFFFFF; padding: 20px; border-radius: 10px; text-align: center;">🔬 Fakta Nutrisi: {random.choice(nutrition_facts)}</div>', unsafe_allow_html=True)

    st.header("🍽️ Galeri Menu Sehat")
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

    st.markdown("<div class='footer'>© 2024 Asisten Nutrisi. All Rights Reserved.</div>", unsafe_allow_html=True)
