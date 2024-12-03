import pickle
import streamlit as st
import numpy as np

# Load model prediksi nutrisi
model = pickle.load(open('model_prediksi_nutrisi.sav', 'rb'))

# Set title of the page
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Prediksi Nutrisi dan Penyakit</h1>", unsafe_allow_html=True)

# Form Input untuk prediksi
st.markdown("<h2 style='color: #009688;'>Masukkan Data untuk Prediksi Nutrisi</h2>", unsafe_allow_html=True)
st.write("Masukkan nilai variabel berikut untuk melakukan prediksi.")

# Input variabel independent berdasarkan dataset nutrisi
ages = st.number_input('Usia (Ages)', min_value=1, max_value=100, value=25)
gender = st.selectbox('Gender', options={0: 'Female', 1: 'Male'}, format_func=lambda x: 'Female' if x == 0 else 'Male')
activity_level = st.selectbox(
    'Activity Level', 
    options={0: 'Sedentary', 1: 'Lightly Active', 2: 'Moderately Active', 3: 'Very Active'}, 
    format_func=lambda x: ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active'][x]
)
height = st.number_input('Tinggi Badan (Height, cm)', min_value=50, max_value=250, value=170)
weight = st.number_input('Berat Badan (Weight, kg)', min_value=20, max_value=200, value=65)
protein = st.number_input('Protein (gram)', min_value=0, max_value=500, value=100)
sugar = st.number_input('Gula (gram)', min_value=0, max_value=500, value=50)
sodium = st.number_input('Sodium (mg)', min_value=0, max_value=5000, value=200)
calories = st.number_input('Kalori (Calories)', min_value=0, max_value=5000, value=2000)
carbohydrates = st.number_input('Karbohidrat (gram)', min_value=0, max_value=500, value=250)
fiber = st.number_input('Serat (gram)', min_value=0, max_value=100, value=25)
fat = st.number_input('Lemak (gram)', min_value=0, max_value=500, value=70)

# Fungsi untuk menghitung BMR (Basal Metabolic Rate) menggunakan rumus Mifflin-St Jeor
def calculate_bmr(gender, weight, height, age):
    if gender == 0:  # Female
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:  # Male
        return 10 * weight + 6.25 * height - 5 * age + 5

# Fungsi untuk menghitung TDEE (Total Daily Energy Expenditure)
def calculate_tdee(bmr, activity_level):
    if activity_level == 0:  # Sedentary
        return bmr * 1.2
    elif activity_level == 1:  # Lightly Active
        return bmr * 1.375
    elif activity_level == 2:  # Moderately Active
        return bmr * 1.55
    else:  # Very Active
        return bmr * 1.725

# Pemetaan untuk Suggestions (Makanan) dan Disease (Penyakit)
def map_suggestion(disease):
    if disease == "Diabetes":
        return "Makanan tinggi serat, rendah gula, seperti salad, ayam panggang tanpa kulit, sayuran hijau, dan quinoa."
    elif disease == "Hipertensi":
        return "Makanan rendah sodium, seperti ikan bakar, sayuran rebus, dan nasi merah."
    elif disease == "Kolesterol Tinggi":
        return "Makanan rendah lemak jenuh dan tinggi serat, seperti oatmeal, kacang-kacangan, dan salmon."
    elif disease == "Obesitas":
        return "Makanan rendah kalori dan tinggi protein, seperti telur rebus, ayam tanpa kulit, dan sayuran hijau."
    else:
        return "Makanan sehat secara umum, seperti salad, ayam panggang, ikan, dan nasi merah."

def map_disease(value):
    if value < 10:
        return "Sehat"
    elif 10 <= value < 50:
        return "Diabetes"
    elif 50 <= value < 100:
        return "Hipertensi"
    elif 100 <= value < 200:
        return "Kolesterol Tinggi"
    elif 200 <= value < 300:
        return "Obesitas"
    else:
        return "Gizi Buruk"

# Prediksi berdasarkan input
if st.button('Prediksi!'):
    # Menghitung BMR dan TDEE berdasarkan input
    bmr = calculate_bmr(gender, weight, height, ages)
    tdee = calculate_tdee(bmr, activity_level)

    # Menampilkan hasil perhitungan TDEE (Target Kalori Harian)
    st.markdown("<h3 style='color: #FF5722;'>Hasil Perhitungan Target Kalori Harian</h3>", unsafe_allow_html=True)
    st.write(f"**BMR (Basal Metabolic Rate)**: {bmr:.2f} kalori/hari")
    st.write(f"**TDEE (Total Daily Energy Expenditure)**: {tdee:.2f} kalori/hari (Target Kalori Harian)")

    # Menyusun rekomendasi kalori untuk tujuan penurunan atau penambahan berat badan
    st.markdown("<h3 style='color: #795548;'>Rekomendasi Kalori Harian</h3>", unsafe_allow_html=True)
    st.write("""
    Jika tujuan Anda adalah **menurunkan berat badan**, disarankan untuk mengurangi asupan kalori sekitar 500 kalori dari TDEE Anda. 
    Jadi, jika TDEE Anda adalah **{:.2f} kalori**, Anda dapat mengonsumsi sekitar **{:.2f} kalori** per hari untuk penurunan berat badan yang aman.

    Jika tujuan Anda adalah **menambah berat badan**, Anda dapat meningkatkan kalori sekitar 300-500 kalori dari TDEE Anda. 
    Jadi, jika TDEE Anda adalah **{:.2f} kalori**, Anda dapat mengonsumsi sekitar **{:.2f} kalori** per hari untuk kenaikan berat badan yang sehat.
    """.format(tdee, tdee - 500, tdee + 300, tdee))

    # Menyiapkan data untuk prediksi
    input_data = np.array([
        ages, gender, activity_level, height, weight, tdee,
        protein, sugar, sodium, calories, carbohydrates, fiber, fat
    ]).reshape(1, -1)
    
    # Melakukan prediksi
    prediksi = model.predict(input_data)

    # Menampilkan hasil prediksi
    st.markdown("<h3 style='color: #3F51B5;'>Hasil Prediksi</h3>", unsafe_allow_html=True)

    # Asumsi hasil prediksi pertama adalah suggestion makanan dan kedua adalah disease
    disease_value = float(prediksi[0][1])  # Misalnya, hasil kedua untuk penyakit

    # Mendapatkan hasil deskripsi penyakit
    disease = map_disease(disease_value)

    # Mendapatkan rekomendasi makanan berdasarkan penyakit yang diprediksi
    suggestion = map_suggestion(disease)

    # Menyusun penjelasan untuk hasil prediksi
    st.write(f"**Penyakit/ Kondisi Kesehatan**: {disease}")
    st.write(f"**Rekomendasi Makanan**: {suggestion}")

    st.write("<p style='color: #607D8B;'>Terima kasih telah menggunakan aplikasi prediksi nutrisi!</p>", unsafe_allow_html=True)
