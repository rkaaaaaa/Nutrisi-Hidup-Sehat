import streamlit as st

def show_contact():

    st.markdown("<h1 style='text-align: center;'>Contact and About</h1>", unsafe_allow_html=True)

    st.header("About")
    st.write("Aplikasi web ini dibuat oleh Kelompok 5")
    st.write("Aplikasi ini dibuat untuk mem-visualisasi dan menganalisis data dari Makanan Bernutrisi untuk Program Diet.")

    st.header("Anggota Kelompok 5")
    st.write("1. Bintang Raka Putra (233307000)")
    st.write("2. Hadziq Naufal Bagus (233307101)")
    st.write("3. Leni Novitasari (233307106)")
    st.write("4. Niken Setyo Ningrum (233307112)")

    st.header("Contact Information")
    st.write("Email:", "=")
    st.write("GitHub:", "https://github.com/rkaaaaaa/Nutrisi-Hidup-Sehat.git")
    st.write("Instagram:", "=")

    st.header("Feedback")
    st.write("Seberapa suka anda dengan aplikasi saya?")
    rating = st.slider("Geser untuk suka/tidak suka", 0, 100, 50)

    # Tombol Submit
    submitted = st.button("Submit")
    if submitted:
        st.write(f"Terima kasih atas feedback Anda! Rating Anda adalah {rating}.")

# # Menjalankan fungsi show_contact
# show_contact()