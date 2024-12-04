import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score

def show_machine():
# Memuat dataset
    data = pd.read_csv('Food_and_Nutrition__.csv')

    # Menyimpan label asli
    original_genders = data['Gender'].unique()
    original_activity_levels = data['Activity Level'].unique()
    original_dietary_preferences = data['Dietary Preference'].unique()

    # Mengonversi kolom string menjadi angka
    label_encoder_gender = LabelEncoder()
    label_encoder_activity = LabelEncoder()
    label_encoder_diet = LabelEncoder()

    data['Gender'] = label_encoder_gender.fit_transform(data['Gender'])
    data['Activity Level'] = label_encoder_activity.fit_transform(data['Activity Level'])
    data['Dietary Preference'] = label_encoder_diet.fit_transform(data['Dietary Preference'])

    # Memisahkan fitur dan target
    X = data[['Ages', 'Gender', 'Height', 'Weight', 'Activity Level', 
            'Dietary Preference', 'Daily Calorie Target', 'Protein', 
            'Sugar', 'Sodium', 'Calories', 'Carbohydrates', 'Fiber', 'Fat']]
    y = data['Disease']

    # Membagi data menjadi data pelatihan dan pengujian
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Melatih model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluasi model (di belakang layar tanpa mencetak laporan ke pengguna)
    scores = cross_val_score(model, X, y, cv=5)

    # Antarmuka pengguna Streamlit untuk input
    st.title("Prediksi Penyakit Berdasarkan Data Kesehatan")

    # Menggunakan st.form untuk mengelompokkan input
    with st.form(key='input_form'):
        # Input dari pengguna
        ages = st.number_input("Usia (Ages)", min_value=0, key="ages")
        gender = st.selectbox("Jenis Kelamin (Gender)", options=original_genders, key="gender")
        height = st.number_input("Tinggi Badan (Height) dalam cm", min_value=0, key="height")
        weight = st.number_input("Berat Badan (Weight) dalam kg", min_value=0, key="weight")
        activity_level = st.selectbox("Tingkat Aktivitas (Activity Level)", options=original_activity_levels, key="activity_level")
        dietary_preference = st.selectbox("Preferensi Diet (Dietary Preference)", options=original_dietary_preferences, key="dietary_preference")
        daily_calorie_target = st.number_input("Target Kalori Harian (Daily Calorie Target)", min_value=0, key="daily_calorie_target")
        protein = st.number_input("Protein dalam gram", min_value=0, key="protein")
        sugar = st.number_input("Gula dalam gram", min_value=0, key="sugar")
        sodium = st.number_input("Sodium dalam mg", min_value=0, key="sodium")
        calories = st.number_input("Kalori dalam kalori", min_value=0, key="calories")
        carbohydrates = st.number_input("Karbohidrat dalam gram", min_value=0, key="carbohydrates")
        fiber = st.number_input("Serat dalam gram", min_value=0, key="fiber")
        fat = st.number_input("Lemak dalam gram", min_value=0, key="fat")

        # Tombol untuk memprediksi
        submit_button = st.form_submit_button(label='Prediksi')

    # Melakukan prediksi jika tombol ditekan
    if submit_button:
        # Mengencode input untuk prediksi
        gender_encoded = label_encoder_gender.transform([gender])[0]
        activity_level_encoded = label_encoder_activity.transform([activity_level])[0]
        dietary_preference_encoded = label_encoder_diet.transform([dietary_preference])[0]
        
        # Membuat input untuk prediksi
        input_data = np.array([[ages, gender_encoded, height, weight, activity_level_encoded,
                                dietary_preference_encoded, daily_calorie_target, protein,
                                sugar, sodium, calories, carbohydrates, fiber, fat]])
        
        # Melakukan prediksi
        prediction = model.predict(input_data)
        
        # Menampilkan hasil
        st.success(f"Prediksi Penyakit: {prediction[0]}")
