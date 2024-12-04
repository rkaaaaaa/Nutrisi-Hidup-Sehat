import streamlit as st

# Fungsi utama
def show_about():
    # Header utama
    st.markdown("<h1 style='text-align: center; color: white;'>🍎 About the Application</h1>", unsafe_allow_html=True)

    # Deskripsi aplikasi
    with st.expander("Deskripsi Aplikasi", expanded=True):
        st.markdown("""
            Aplikasi **Asisten Nutrisi untuk Kesehatan Pribadi** dirancang untuk memberikan rekomendasi diet yang disesuaikan 
            dengan kondisi kesehatan pengguna. Dengan memanfaatkan dataset nutrisi yang komprehensif, aplikasi ini 
            bertujuan untuk meningkatkan kualitas perawatan kesehatan dan kesejahteraan melalui perencanaan makanan yang 
            dipersonalisasi.
        """, unsafe_allow_html=True)

    # Fitur utama
    with st.expander("✨ Fitur Utama", expanded=True):
        st.markdown("""
            - **Rencana Diet Pribadi**  
              Memberikan rekomendasi makanan berdasarkan kondisi kesehatan seperti diabetes, hipertensi, atau penyakit kardiovaskular.  
              Menyediakan opsi makanan seimbang yang sesuai dengan pembatasan diet seperti rendah karbohidrat, rendah lemak, atau tinggi protein.

            - **Wawasan Nutrisi**  
              Menampilkan informasi rinci tentang makronutrien (karbohidrat, protein, lemak) dan mikronutrien (vitamin dan mineral).  
              Memberikan konten kalori dan ukuran porsi untuk setiap makanan, membantu pengguna mencapai tujuan diet mereka.

            - **Rekomendasi Berdasarkan Penyakit**  
              Menghubungkan makanan dengan penyakit tertentu untuk membantu mengelola atau mengurangi gejala secara efektif.  
              Memberikan wawasan tentang pola makan umum untuk kondisi kesehatan tertentu untuk mendorong pilihan makanan yang lebih baik.

            - **Klasifikasi Makanan**  
              Mengkategorikan makanan berdasarkan jenis (sarapan, makan siang, makan malam, camilan) untuk memudahkan perencanaan makan sepanjang hari.
        """, unsafe_allow_html=True)

    # Metode yang digunakan
    with st.expander("📊 Metode yang Digunakan", expanded=True):
        st.markdown("""
        - **Algoritma yang Digunakan:** Random Forest Classifier  
          - **Tipe Metode:**  
            Supervised Learning: Random Forest digunakan untuk masalah klasifikasi dan regresi. Dalam aplikasi ini, algoritma digunakan untuk klasifikasi penyakit berdasarkan fitur kesehatan.  
          - **Deskripsi:**  
            Random Forest adalah ensemble learning method yang menggabungkan banyak decision trees untuk memberikan hasil yang lebih akurat dan stabil. Setiap tree dilatih pada subset acak dari data, dan prediksi akhir diambil berdasarkan voting dari semua tree.  
          - **Langkah-langkah Implementasi:**  
            1. **Pengolahan Data:** Data dibaca, kemudian fitur dan target dipisahkan.  
            2. **Pembagian Data:** Data dibagi menjadi set pelatihan dan pengujian menggunakan `train_test_split`.  
            3. **Pelatihan Model:** Model `RandomForestClassifier` dilatih dengan data pelatihan.  
            4. **Evaluasi Model:** Model dievaluasi menggunakan cross-validation untuk mendapatkan skor akurasi.  
        """, unsafe_allow_html=True)

    # Pengguna target
    with st.expander("🎯 Pengguna Target", expanded=True):
        st.markdown("""
        <ul style="list-style-type: none; padding-left: 0;">
            <li><strong>Pasien</strong> yang ingin mengelola kondisi kesehatan mereka melalui diet.</li>
            <li><strong>Tenaga kesehatan</strong> yang ingin memberikan saran nutrisi berbasis data.</li>
            <li><strong>Ahli gizi dan dietisien</strong> yang melakukan penilaian nutrisi.</li>
            <li><strong>Peneliti</strong> yang mempelajari peran diet dalam pencegahan dan pengelolaan penyakit.</li>
        </ul>
        """, unsafe_allow_html=True)

    # Kesimpulan
    with st.expander("Kesimpulan", expanded=True):
        st.markdown("""
            Dengan fokus pada peningkatan kebiasaan makan dan mendukung pengelolaan kesehatan, aplikasi <strong>Asisten Nutrisi untuk Kesehatan Pribadi</strong> 
            bertujuan untuk merevolusi cara individu mendekati nutrisi demi kesejahteraan mereka.
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("<p style='text-align: center; color: #888888;'>© 2024 Asisten Nutrisi. All Rights Reserved.</p>", unsafe_allow_html=True)
