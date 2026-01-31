import streamlit as st

# --- CONFIG ---
st.set_page_config(page_title="Skripsi 5K - Template Kerangka Skripsi", layout="wide")

# --- SIDEBAR UNTUK MODE GELAP/TERANG ---
with st.sidebar:
    st.title("Pengaturan Tema")
    theme_mode = st.radio("Pilih Mode Tampilan:", ["Terang", "Gelap"])

# --- PENENTUAN WARNA ---
if theme_mode == "Terang":
    bg_color = "#FFFFFF"     # Putih
    text_color = "#000000"   # Hitam
    card_bg = "#F0F8FF"      # Alice Blue (Biru sangat muda)
    accent_blue = "#007BFF"  # Biru Standar
else:
    bg_color = "#0E1117"     # Hitam Streamlit
    text_color = "#FFFFFF"   # Putih
    card_bg = "#1E1E1E"      # Abu-abu sangat gelap
    accent_blue = "#3399FF"  # Biru Muda Cerah

# --- CUSTOM CSS (TEMA DINAMIS) ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    /* Floating WhatsApp Button */
    .float-wa {{
        position: fixed; width: 60px; height: 60px; bottom: 40px; right: 40px;
        background-color: #25d366; color: #FFF; border-radius: 50px;
        text-align: center; font-size: 30px; box-shadow: 2px 2px 3px #999;
        z-index: 100; display: flex; align-items: center; justify-content: center;
        text-decoration: none;
    }}
    /* Card Style Dinamis */
    .product-box {{
        border: 2px solid {accent_blue};
        border-radius: 15px;
        padding: 20px;
        background-color: {card_bg};
        margin-bottom: 20px;
    }}
    </style>
    
    <a href="https://wa.me/628131709665?text=Halo%20Admin%20template,%20saya%20tertarik%20dengan%20produknya" class="float-wa" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35">
    </a>
""", unsafe_allow_html=True) 

# --- HEADER ---
st.title("🎓 Template Kerangka Skripsi")
st.subheader("Kerangka Skripsi Cuman Seharga Gorengan")

# --- SOSIAL MEDIA ---
cols_sosmed = st.columns(6)
with cols_sosmed[0]:
    st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com)")
with cols_sosmed[1]:
    st.markdown("[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@TemplateSkripsi)")
with cols_sosmed[2]:
    st.markdown("[![TikTok](https://img.shields.io/badge/TikTok-%23000000.svg?style=for-the-badge&logo=TikTok&logoColor=white)](https://www.tiktok.com/@templatkerangkaskripsiku)")

st.write("---")

# --- DATA PRODUK ---
products = [
    {"nama": "Template Kerangka Skripsi Umum", "harga": "Rp 5.000", "desc": "Kerangka Skripsi Umum di Indonesia", "gambar": "https://via.placeholder.com/300x300.png?text=Template+Umum"},
    {"nama": "Buat Judul", "harga": "Rp 5.000", "desc": "Kami Bantu buatkan Judul Skripsi", "gambar": "https://via.placeholder.com/300x300.png?text=Bantu+Judul"},
    {"nama": "Template Kerangka Sesuai Univ", "harga": "Rp 15.000", "desc": "Sesuai Pedoman Prodi & Kampusmu.", "gambar": "https://via.placeholder.com/300x300.png?text=Template+Kampus"},
    {"nama": "Cari Ide Penelitian", "harga": "Rp 25.000", "desc": "Kami bantu cari ide penelitianmu.", "gambar": "https://via.placeholder.com/300x300.png?text=Ide+Penelitian"}
]

# --- DISPLAY PRODUK ---
cols = st.columns(2) 

for i, p in enumerate(products):
    with cols[i % 2]:
        # Membungkus gambar dan teks dalam div bergaya kartu
        st.markdown(f'<div class="product-box">', unsafe_allow_html=True)
        st.image(p["gambar"], use_container_width=True)
        st.subheader(p["nama"])
        st.write(f"### {p['harga']}")
        st.write(p["desc"])
        
        wa_url = f"https://wa.me/628131709665?text=Halo%20Admin%20dosbing.ai,%20saya%20mau%20beli%20{p['nama']}"
        st.markdown(f'''
            <a href="{wa_url}" target="_blank" style="text-decoration: none;">
                <div style="background-color: {accent_blue}; color: white; padding: 12px; text-align: center; border-radius: 8px; font-weight: bold; cursor: pointer;">
                    Beli {p['nama']}
                </div>
            </a>
        ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True) # Tutup div kartu
        st.write("")

# --- FOOTER ---
st.caption("© 2026 Template Kerangka Skripsiku")
