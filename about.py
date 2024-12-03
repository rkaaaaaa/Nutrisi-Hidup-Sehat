import streamlit as st

# Tambahkan CSS untuk styling
st.markdown("""
    <style>
        .header {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            color: #FF6F61;
            margin-bottom: 20px;
        }
        .subheader {
            font-size: 1.8rem;
            font-weight: bold;
            color: #4CAF50;
            margin-top: 30px;
        }
        .content-box {
            background: linear-gradient(to right, #FFDEE9, #B5FFFC);
            padding: 20px;
            margin: 10px 0;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            color: #333333;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 0.9rem;
            color: #888888;
        }
    </style>
""", unsafe_allow_html=True)

# Fungsi utama
def show_about():
    # Header
    st.markdown("<div class='header'>🍎 About the Application</div>", unsafe_allow_html=True)

    # Deskripsi aplikasi
    st.markdown("""
        Aplikasi **Asisten Nutrisi untuk Kesehatan Pribadi** dirancang untuk memberikan rekomendasi diet yang disesuaikan 
        dengan kondisi kesehatan pengguna. Dengan memanfaatkan dataset nutrisi yang komprehensif, aplikasi ini 
        bertujuan untuk meningkatkan kualitas perawatan kesehatan dan kesejahteraan melalui perencanaan makanan yang 
        dipersonalisasi.
    """)

    # Fitur utama
    st.markdown("<div class='subheader'>✨ Fitur Utama</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='content-box'>
            - Rencana Diet Pribadi  
              Memberikan rekomendasi makanan berdasarkan kondisi kesehatan seperti diabetes, hipertensi, atau penyakit kardiovaskular.  
              Menyediakan opsi makanan seimbang yang sesuai dengan pembatasan diet seperti rendah karbohidrat, rendah lemak, atau tinggi protein.

            - Wawasan Nutrisi  
              Menampilkan informasi rinci tentang makronutrien (karbohidrat, protein, lemak) dan mikronutrien (vitamin dan mineral).  
              Memberikan konten kalori dan ukuran porsi untuk setiap makanan, membantu pengguna mencapai tujuan diet mereka.

            - Rekomendasi Berdasarkan Penyakit 
              Menghubungkan makanan dengan penyakit tertentu untuk membantu mengelola atau mengurangi gejala secara efektif.  
              Memberikan wawasan tentang pola makan umum untuk kondisi kesehatan tertentu untuk mendorong pilihan makanan yang lebih baik.

            - Klasifikasi Makanan  
              Mengkategorikan makanan berdasarkan jenis (sarapan, makan siang, makan malam, camilan) untuk memudahkan perencanaan makan sepanjang hari.
        </div>
    """, unsafe_allow_html=True)

    # Using HTML for custom styling and layout
    st.markdown("<div class='subheader'>🎯 Pengguna Target</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='content-box'>
        <ul style="list-style-type: none; padding-left: 0;">
            <li><strong>Pasien</strong> yang ingin mengelola kondisi kesehatan mereka melalui diet.</li>
            <li><strong>Tenaga kesehatan</strong> yang ingin memberikan saran nutrisi berbasis data.</li>
            <li><strong>Ahli gizi dan dietisien</strong> yang melakukan penilaian nutrisi.</li>
            <li><strong>Peneliti</strong> yang mempelajari peran diet dalam pencegahan dan pengelolaan penyakit.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Deskripsi akhir
    st.markdown("""
        <div class='content-box'>
            Dengan fokus pada peningkatan kebiasaan makan dan mendukung pengelolaan kesehatan, aplikasi <strong>Asisten Nutrisi untuk Kesehatan Pribadi</strong> 
            bertujuan untuk merevolusi cara individu mendekati nutrisi demi kesejahteraan mereka.
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>© 2024 Asisten Nutrisi. All Rights Reserved.</div>", unsafe_allow_html=True)

# Menjalankan fungsi utama
#show_about()