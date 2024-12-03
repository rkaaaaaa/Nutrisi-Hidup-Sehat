import streamlit as st

def show_about():
    st.title("About the Application")
    st.write(
        "Aplikasi **Asisten Nutrisi untuk Kesehatan Pribadi** dirancang untuk memberikan rekomendasi diet yang disesuaikan "
        "dengan kondisi kesehatan pengguna. Dengan memanfaatkan dataset nutrisi yang komprehensif, aplikasi ini "
        "bertujuan untuk meningkatkan kualitas perawatan kesehatan dan kesejahteraan melalui perencanaan makanan yang "
        "dipersonalisasi."
    )

    st.subheader("Fitur Utama")
    st.write("1. **Rencana Diet Pribadi**")
    st.write(
        "   - Memberikan rekomendasi makanan berdasarkan kondisi kesehatan seperti diabetes, hipertensi, atau penyakit kardiovaskular."
        "\n   - Menyediakan opsi makanan seimbang yang sesuai dengan pembatasan diet seperti rendah karbohidrat, rendah lemak, atau tinggi protein."
    )

    st.write("2. **Wawasan Nutrisi**")
    st.write(
        "   - Menampilkan informasi rinci tentang makronutrien (karbohidrat, protein, lemak) dan mikronutrien (vitamin dan mineral)."
        "\n   - Memberikan konten kalori dan ukuran porsi untuk setiap makanan, membantu pengguna mencapai tujuan diet mereka."
    )

    st.write("3. **Rekomendasi Berdasarkan Penyakit**")
    st.write(
        "   - Menghubungkan makanan dengan penyakit tertentu untuk membantu mengelola atau mengurangi gejala secara efektif."
        "\n   - Memberikan wawasan tentang pola makan umum untuk kondisi kesehatan tertentu untuk mendorong pilihan makanan yang lebih baik."
    )

    st.write("4. **Klasifikasi Makanan**")
    st.write(
        "   - Mengkategorikan makanan berdasarkan jenis (sarapan, makan siang, makan malam, camilan) untuk memudahkan perencanaan makan sepanjang hari."
    )

    st.subheader("Pengguna Target")
    st.write(
        "- **Pasien** yang ingin mengelola kondisi kesehatan mereka melalui diet."
        "\n- **Tenaga kesehatan** yang ingin memberikan saran nutrisi berbasis data."
        "\n- **Ahli gizi dan dietisien** yang melakukan penilaian nutrisi."
        "\n- **Peneliti** yang mempelajari peran diet dalam pencegahan dan pengelolaan penyakit."
    )

    st.write(
        "Dengan fokus pada peningkatan kebiasaan makan dan mendukung pengelolaan kesehatan, aplikasi **Asisten Nutrisi untuk Kesehatan Pribadi** "
        "bertujuan untuk merevolusi cara individu mendekati nutrisi demi kesejahteraan mereka."
    )