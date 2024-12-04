import streamlit as st
# CSS untuk meningkatkan tampilan
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #283c86, #45a247); /* Gradasi warna */
            color: white;
            font-family: Arial, sans-serif;
        }
        .header {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            margin-top: 20px;
        }
        .sub-header {
            font-size: 1.8rem;
            margin-top: 40px;
        }
        .content-box {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
        }
        .feedback-container {
            background: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
        }
        a {
            color: #4cffff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        button {
            background-color: #4cffff;
            color: black;
            font-weight: bold;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #39cccc;
        }
    </style>
""", unsafe_allow_html=True)

# Fungsi utama
def show_contact():
    # Header utama
    st.markdown("<div class='header'>Contact and About</div>", unsafe_allow_html=True)

    # Tentang aplikasi
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>About</h2>", unsafe_allow_html=True)
    st.write("""
    Aplikasi web ini dibuat oleh **Kelompok 5**. 
    Aplikasi ini bertujuan untuk memvisualisasi dan menganalisis data Makanan Bernutrisi sebagai bagian dari program diet sehat.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Anggota kelompok
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Anggota Kelompok 5</h2>", unsafe_allow_html=True)
    st.write("""
    1. Bintang Raka Putra (233307000)  
    2. Hadziq Naufal Bagus (233307101)  
    3. Leni Novitasari (233307106)  
    4. Niken Setyo Ningrum (233307112)
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Kontak informasi
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Contact Information</h2>", unsafe_allow_html=True)
    st.write("**Email:** -")
    st.write("**GitHub:** [https://github.com/rkaaaaaa/Nutrisi-Hidup-Sehat.git](https://github.com/rkaaaaaa/Nutrisi-Hidup-Sehat.git)")
    st.write("**Instagram:** -")
    st.markdown("</div>", unsafe_allow_html=True)

    # Feedback pengguna
    st.markdown("<div class='feedback-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Feedback</h2>", unsafe_allow_html=True)
    st.write("Seberapa suka Anda dengan aplikasi ini?")
    
    # Slider rating
    rating = st.slider("Geser untuk memberi rating", 0, 100, 50, key="feedback_slider")

    # Tambahan area teks untuk masukan feedback
    st.text_area("Berikan komentar atau saran Anda di bawah ini:", placeholder="Tulis komentar Anda di sini...", key="feedback_textarea")

    # Tombol submit
    if st.button("Submit", key="feedback_submit"):
        st.success(f"Terima kasih atas feedback Anda! Rating Anda adalah **{rating}**.")
        st.balloons()  # Animasi interaktif untuk pengguna
    st.markdown("</div>", unsafe_allow_html=True)

# # Menjalankan fungsi show_contact
# show_contact()