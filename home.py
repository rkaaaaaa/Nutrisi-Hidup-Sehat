import streamlit as st
import random
from streamlit_image_select import image_select

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
    .divider {
        height: 2px;
        background: linear-gradient(to right, #FF6B6B, #4ECDC4);
        margin: 40px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Smart Nutrition</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Prediksi Kesehatan Melalui Analisis Gizi</div>', unsafe_allow_html=True)

    st.image("images/header.jpg", caption="Makanan Bernutrisi", use_container_width=True)

    st.markdown("""
    <div style="color: #4CAF50; font-size: 2rem; font-weight: bold; margin-top: 40px; margin-bottom: 20px">
        🌟 Selamat Datang di Dunia Nutrisi Cerdas!
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
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
        "🍗 Diet seimbang kunci utama kesehatan dan kebugaran optimal!"
    ]
    st.markdown(f'<div style="background: linear-gradient(to right, #FF6B6B, #4ECDC4); color: #FFFFFF; padding: 20px; border-radius: 10px; text-align: center;">🔬 Fakta Nutrisi: {random.choice(nutrition_facts)}</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="color: #4CAF50; font-size: 2rem; font-weight: bold; margin-top: 40px; margin-bottom: 20px">
        🍽️ Galeri Menu Sehat
    </div>
    """, unsafe_allow_html=True)

    # Mengelola status untuk kategori Breakfast dan Dinner
    if 'active_category' not in st.session_state:
        st.session_state.active_category = None  # Menyimpan kategori yang aktif untuk menampilkan resep

    if 'selected_image' not in st.session_state:
        st.session_state.selected_image = None  # Menyimpan gambar yang dipilih

    categories = {
        "🥗Breakfast Suggestion": [
            {"image": "images/Breakfast/berries.jpeg", "caption": "Oatmeal with Berries and Nuts", "recipe": """
                - 1/2 cangkir rolled oats
                - 1 cangkir air atau susu
                - 1/4 cangkir berry segar atau beku
                - 2 sendok makan kacang cincang
                - 1 sendok teh madu atau sirup maple (opsional)
                - 1/4 sendok teh kayu manis bubuk (opsional)
            """, "steps": """
                1. Gabungkan oats dan air atau susu dalam panci kecil. Didihkan dengan api besar.
                2. Kurangi api ke rendah dan didihkan selama 5 menit, atau sampai oats matang sempurna.
                3. Aduk berry, kacang, madu atau sirup maple (jika menggunakan), dan kayu manis (jika menggunakan).
                4. Sajikan panas dan nikmati!
            """},

            {"image": "images/Breakfast/tofus.jpeg", "caption": "Tofu Scramble with Veggies", "recipe": """
                - 1 bawang bombay kecil (atau setengah bawang bombay sedang)
                - 1 paprika, warna apa saja (disarankan paprika manis seperti merah, oranye, atau kuning)
                - 6 - 8 ons jamur, jenis apa saja (biasanya menggunakan baby Bella atau jamur kancing putih)
                - 1 blok tofu 16 ons (396g) keras atau medium (beberapa orang menggunakan tofu silken, tapi lebih disukai tofu keras atau medium)
                - 1 sendok teh bawang putih bubuk
                - ½ sendok teh kunyit (sesuaikan dengan warna yang diinginkan)
                - ¼ sendok teh merica hitam (sesuaikan dengan selera)
                - ½ sendok teh garam laut (sesuaikan dengan selera)
                - ¼ sendok teh kala namak / garam hitam (opsional, memberikan rasa mirip telur)
                - 2 - 3 sendok makan nutritional yeast (memberikan rasa gurih)
                - 1 cangkir bayam bayi (atau sayuran bayi lainnya, seperti baby kale)
                - Untuk penyajian: roti panggang, tomat, alpukat (opsional)
            """, "steps": """
                1. Tumis bawang bombay di wajan anti lengket besar dengan api sedang-tinggi, aduk sering. Jika mulai menempel, tambahkan 1 sendok makan air. Ulangi selama 2-3 menit.
                2. Tambahkan paprika dan jamur, tumis selama beberapa menit.
                3. Remukkan tofu yang sudah tiris ke dalam wajan. Bisa juga dipotong-potong dan diaduk dengan alat masak.
                4. Tambahkan bumbu (tidak termasuk nutritional yeast).
                5. Aduk rata, masak beberapa menit, lalu tambahkan nutritional yeast dan bayam (jika digunakan), aduk lagi.
                6. Sajikan dengan roti panggang, sandwich, atau wrap.
                7. Simpan sisa makanan dalam wadah kedap udara (disarankan wadah kaca agar kunyit tidak mewarnai plastik) di kulkas selama 3-4 hari.
            """},

            {"image": "images/Breakfast/tofu.jpeg", "caption": "Tofu and Veggie Breakfast Burrito", "recipe": """
                - TOFU
                    - 1 bungkus (12 ons) tofu keras/ekstra keras
                    - 1 sdt minyak atau 1 sdm air
                    - 3 siung bawang putih (cincang)
                    - 1 sdm hummus
                    - 1/2 sdt bubuk cabai
                    - 1/2 sdt jintan
                    - 1 sdt nutritional yeast
                    - 1/4 sdt garam laut
                    - Sejumput bubuk cabai rawit (opsional)
                    - 1/4 cangkir peterseli cincang
                - SAYURAN
                    - 5 kentang kecil (potong kecil)
                    - 1 paprika merah sedang (iris tipis)
                    - 1 sdt minyak atau 1 sdm air
                    - Sejumput garam laut
                    - 1/2 sdt jintan bubuk
                    - 1/2 sdt bubuk cabai
                    - 2 cangkir kale cincang
                - PELENGKAP
                    - 3-4 tortilla besar (pastikan vegan)
                    - 1 alpukat matang (cincang atau haluskan)
                    - Daun ketumbar
                    - Salsa merah/hijau atau saus pedas
            """, "steps": """
                1. Panaskan oven ke 400°F (204°C).
                2. Bungkus tofu dengan handuk bersih, beri beban di atasnya untuk menghilangkan kelembapan, lalu remukkan dengan garpu. Sisihkan.
                3. Tata kentang dan paprika di loyang, tambahkan minyak/air, bumbu, dan aduk rata. Panggang 15-22 menit hingga empuk dan kecokelatan. Masukkan kale 5 menit terakhir untuk layu.               
                4. Panaskan wajan, tambahkan minyak/air, bawang putih, dan tofu. Tumis 7-10 menit hingga agak kecokelatan.
                5. Campur hummus, bumbu, dan air hingga menjadi saus. Tambahkan ke tofu, masak 3-5 menit lagi.
                6. Ambil tortilla, tambahkan sayuran panggang, tofu, alpukat, ketumbar, dan salsa. Gulung rapat.
                7. Sajikan langsung atau simpan di kulkas hingga 4 hari atau freezer hingga 1 bulan.
            """},

            {"image": "images/Breakfast/greek.jpeg", "caption": "Greek Yogurt with Granola and Fruit", "recipe": """
                - Plain Greek yogurt:
                    - Dari segi nutrisi, Greek yogurt memiliki sekitar dua kali lipat protein dan setengah karbohidrat dibandingkan yogurt biasa, menjadikannya pilihan tinggi protein yang cerdas. Saya lebih suka Greek yogurt dengan kadar lemak 2% atau 5% karena lebih creamy dan kandungan lemaknya membantu kenyang lebih lama.
                - Fresh berries:
                    - Tambahkan buah segar favorit Anda di atas mangkuk granola yogurt. Favorit saya adalah kombinasi blueberry, raspberry, dan stroberi yang kaya serat! Saat musim gugur, saya juga suka menggunakan apel rebus dengan kayu manis. 😊
                - Honey:
                    - Madu dan Greek yogurt adalah kombinasi yang lezat! Sedikit madu membantu mengurangi rasa asam dari yogurt.
            """, "steps": """
                1. Persiapan Granola:
                    - Campurkan bahan kering, lalu aduk dengan bahan basah hingga merata.
                    - Sebarkan granola di atas loyang yang sudah dilapisi kertas roti. Panggang tanpa diaduk hingga berwarna kecokelatan, biarkan dingin, lalu pecahkan menjadi gumpalan kecil dengan tangan.
                2. Penyusunan Mangkuk:
                    - Mulailah dengan yogurt Yunani sebagai dasar.
                    - Tambahkan buah segar di atas yogurt.
                    - Taburkan satu atau dua genggam granola di atasnya.
                    - Siram dengan madu dan nikmati dengan sendok!
            """},
        ],
        "🥗Lunch Suggestion": [
            {"image": "images/Lunch/chicken.jpeg", "caption": "Grilled Chicken Salad with Mixed Greens", "recipe": """
                - 2 cangkir campuran daun hijau segar (berbagai jenis selada)
                - 1 mentimun
                - 1 paprika
                - 3 tomat ceri
                - 1 wortel
                - 1 sdm jagung kalengan
                - 50 g ayam panggang (dada/filet)
                - Parmesan
                - 1 irisan roti basi
                - Cuka balsamic
                - Minyak zaitun
                - Lemon
                - Garam, merica secukupnya
            """, "steps": """
                1. Ayam Panggang: Jika Anda tidak menggunakan filet ayam yang sudah dipanggang, bumbui ayam terlebih dahulu lalu panggang di wajan panas selama beberapa menit di kedua sisi. Angkat dari api, biarkan dingin, lalu potong-potong kecil.
                2. Roti Crouton: Potong roti basi menjadi kubus, lalu panggang di wajan selama beberapa menit hingga renyah. Angkat dan biarkan dingin.
                3. Sayuran: Cuci dan tiriskan daun hijau campuran. Gunakan selada apa pun sesuai selera. Kupas dan iris mentimun. Cuci dan iris paprika (saya menggunakan jenis hijau muda dari kebun). Kupas wortel dan iris tipis (atau parut). Belah tomat ceri menjadi dua.
                4. Dressing: Dalam mangkuk atau toples kecil, campurkan minyak zaitun dan cuka balsamic (rasio 1:3), tambahkan perasan jus lemon atau sedikit air, sejumput garam, dan merica. Aduk rata dengan whisk atau kocok dalam toples hingga tercampur.
                5. Penyajian Salad: Dalam mangkuk, susun daun hijau yang sudah dicuci, irisan mentimun dan paprika, tomat ceri, stik wortel, dan satu sendok makan jagung kalengan. Tambahkan potongan ayam dan crouton roti.
                6. Finishing: Taburi salad dengan keju parmesan parut dan dressing balsamic. Nikmati!
            """},
        ]
    }

    # Menampilkan kategori dan mengelola tampilan resep
    for category, items in categories.items():
        selected_image = image_select(
            label=f"{category}:",
            images=[item["image"] for item in items],
            captions=[item["caption"] for item in items],
            use_container_width=False,
        )

        # Menyimpan kategori aktif dan gambar yang dipilih
        if selected_image:
            st.session_state.active_category = category
            st.session_state.selected_image = selected_image

        # Menampilkan resep hanya jika kategori ini adalah kategori aktif
        if st.session_state.active_category == category:
            selected_recipe = next(item for item in items if item["image"] == st.session_state.selected_image)
            
            with st.container():
                col1, col2, col3 = st.columns([1, 2.2, 2.5])
                with col1:
                    st.image(st.session_state.selected_image, caption=selected_recipe["caption"], width=200)
                with col2:
                    st.subheader(f"🍴 Resep {selected_recipe['caption']}:")
                    st.write(selected_recipe["recipe"])
                with col3:
                    st.subheader("🔧 Cara Membuat:")
                    st.write(selected_recipe["steps"])

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("<div class='footer'>© 2024 Asisten Nutrisi. Kelompok_5 All Rights Reserved.</div>", unsafe_allow_html=True)
