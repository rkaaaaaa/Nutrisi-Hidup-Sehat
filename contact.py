import streamlit as st
import webbrowser

# CSS untuk meningkatkan tampilan
st.markdown(
    """
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
        .card-box {
            background: rgba(255, 255, 255, 0.15);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.4);
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
    """,
    unsafe_allow_html=True,
)

# Fungsi utama
def show_contact():
    # Header utama
    st.markdown("<div class='header'>Contact and About</div>", unsafe_allow_html=True)

    # Membuat layout dua kolom untuk Anggota Kelompok dan Contact Information
    cols = st.columns(2)  # Membagi menjadi 2 kolom
    
    # Kotak untuk Anggota Kelompok di kolom pertama
    with cols[0]:
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>Anggota Kelompok 5</h2>", unsafe_allow_html=True)
        st.write("1. Bintang Raka Putra (233307097)")
        st.write("2. Hadziq Naufal Bagus (233307101)")
        st.write("3. Leni Novitasari (233307106)")
        st.write("4. Niken Setyo Ningrum (233307111)")
        st.markdown("</div>", unsafe_allow_html=True)

    # Kotak untuk Contact Information di kolom kedua
    with cols[1]:
        st.markdown("<div class='card-box'>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>Contact Information</h2>", unsafe_allow_html=True)
        st.write("**Email:** -")
        st.write("**GitHub:** [Link GitHub](https://github.com/rkaaaaaa/Nutrisi-Hidup-Sehat.git)")
        st.write("**Instagram:** -")
        st.write("**Nomor Admin:** +6281234567890")  # Tambahkan nomor admin
        st.markdown("</div>", unsafe_allow_html=True)

    # Feedback pengguna
    st.markdown("<div class='feedback-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Feedback</h2>", unsafe_allow_html=True)
    st.write("Seberapa suka Anda dengan aplikasi ini?")

    # Slider rating
    rating = st.slider("Geser untuk memberi rating", 0, 100, 50, key="feedback_slider")

    # Tambahan area teks untuk masukan feedback
    feedback = st.text_area(
        "Berikan komentar atau saran Anda di bawah ini:",
        placeholder="Tulis komentar Anda di sini...",
        key="feedback_textarea",
    )

    # Input nomor WhatsApp
    phone_number = st.text_input("Masukkan nomor WhatsApp tujuan (contoh: 6281234567890):", "")

    # Tombol submit
    if st.button("Submit", key="feedback_submit"):
        # Validasi input
        if not phone_number.isdigit() or not phone_number.startswith("62"):
            st.error("Nomor WhatsApp harus berupa angka dan diawali dengan 62.")
        elif not feedback:
            st.error("Masukan feedback tidak boleh kosong.")
        else:
            # Format URL WhatsApp
            whatsapp_url = f"https://wa.me/{phone_number}?text={feedback}"
            # Buka di browser
            webbrowser.open(whatsapp_url)
            st.success("Feedback Anda telah terkirim ke WhatsApp!")
            st.balloons()  # Animasi interaktif untuk pengguna
    st.markdown("</div>", unsafe_allow_html=True)