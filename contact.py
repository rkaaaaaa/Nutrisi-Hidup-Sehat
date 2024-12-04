import streamlit as st
import urllib.parse

# Memuat Bootstrap Icons melalui CDN
st.markdown("""
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
</head>
""", unsafe_allow_html=True)

# Fungsi utama untuk bagian Contact
def show_contact():
    # Header utama dengan ikon Bootstrap
    st.markdown("""
    <h1 style='text-align: center; color: white;'>
        <i class="bi bi-person-circle" style="font-size: 3rem;"></i> Contact
    </h1>
    """, unsafe_allow_html=True)

    # Membuat layout dua kolom untuk Anggota Kelompok dan Contact Information
    st.markdown("<h2 style='color: #4CAF50;'>🎯 Anggota Kelompok 5</h2>", unsafe_allow_html=True)
    
    # Kotak Anggota Kelompok
    with st.expander("Anggota Kelompok 5", expanded=True):
        st.markdown("""
            1. Bintang Raka Putra (233307097)<br>
            2. Hadziq Naufal Bagus (233307101)<br>
            3. Leni Novitasari (233307106)<br>
            4. Niken Setyo Ningrum (233307111)<br>
        """, unsafe_allow_html=True)

    st.markdown("<h2 style='color: #4CAF50;'>📞 Contact Information</h2>", unsafe_allow_html=True)
    
    # Kotak Contact Information
    with st.expander("Contact Information", expanded=True):
        st.markdown("""
            **Email:** kelasdteknologiinformasi@gmail.com<br>
            **GitHub:** [Link GitHub](https://github.com/rkaaaaaa/Nutrisi-Hidup-Sehat.git)<br>
            **Instagram:** @inftechd<br>
        """, unsafe_allow_html=True)

    # Feedback pengguna
    st.markdown("<h2 style='color: #4CAF50;'>💬 Feedback</h2>", unsafe_allow_html=True)
    st.markdown("""
        Kami sangat menghargai masukan Anda! Berikan komentar atau saran Anda untuk perbaikan aplikasi ini.
    """, unsafe_allow_html=True)

    # Slider rating
    rating = st.slider("Geser untuk memberi rating", 0, 100, 50, key="feedback_slider")

    # Tambahan area teks untuk masukan feedback
    feedback = st.text_area(
        "Berikan komentar atau saran Anda di bawah ini:",
        placeholder="Tulis komentar Anda di sini...",
        key="feedback_textarea",
    )

    # Input nomor WhatsApp
    phone_number = st.text_input("Masukkan nomor WhatsApp admin | Bintang Raka - 6285607053282 / Hadziq Naufal - 62895343028010 /Leni Novitasari - 6285334645836 /Niken Setyo Ningrum - 62895710617373")

    # Tombol submit
    if st.button("Submit", key="feedback_submit"):
        # Validasi input
        if not phone_number.isdigit() or not phone_number.startswith("62"):
            st.error("Nomor WhatsApp harus berupa angka dan diawali dengan 62.")
        elif not feedback:
            st.error("Masukan feedback tidak boleh kosong.")
        else:
            # Format pesan untuk WhatsApp
            message = f"Hello Admin,%0A%0ASaya ingin memberikan feedback:%0A{urllib.parse.quote(feedback)}%0A%0ARating: {rating}/100"
            # Format URL WhatsApp
            whatsapp_url = f"https://wa.me/{phone_number}?text={message}"
            
            # Menggunakan st.markdown dengan HTML untuk membuka WhatsApp di tab baru
            st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="btn btn-primary">Kirim Feedback ke WhatsApp</a>', unsafe_allow_html=True)
            st.success("Feedback Anda telah terkirim ke WhatsApp!")
            st.balloons()  # Animasi interaktif untuk pengguna

    # Footer
    st.markdown("<p style='text-align: center; color: #888888;'>© 2024 Asisten Nutrisi. All Rights Reserved.</p>", unsafe_allow_html=True)
