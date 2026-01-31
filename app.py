import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="dosbing.ai - Partner Skripsi Kamu", layout="wide")

# Custom CSS untuk Floating WA dan Styling
st.markdown("""
    <style>
    /* Floating WhatsApp Button */
    .float-wa {
        position: fixed;
        width: 60px;
        height: 60px;
        bottom: 40px;
        right: 40px;
        background-color: #25d366;
        color: #FFF;
        border-radius: 50px;
        text-align: center;
        font-size: 30px;
        box-shadow: 2px 2px 3px #999;
        z-index: 100;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
    }
    .float-wa:hover {
        background-color: #128C7E;
        color: white;
    }
    
    /* Card Style */
    .product-card {
        border: 1px solid #e6e6e6;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        background-color: white;
        transition: 0.3s;
    }
    .product-card:hover {
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    </style>
    
    <a href="https://wa.me/6281234567890?text=Halo%20Admin%20dosbing.ai,%20saya%20tertarik%20dengan%20produknya" class="float-wa" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35">
    </a>
""", unsafe_allow_html=True) # Ganti unsafe_allow_index menjadi unsafe_allow_html

# --- HEADER ---
st.title("🎓 dosbing.ai")
st.subheader("Solusi Cerdas Penulisan Skripsi & Karya Ilmiah")

# --- SOSIAL MEDIA NAVIGATION ---
cols_sosmed = st.columns(6)
with cols_sosmed[0]:
    st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com/dosbing.ai)")
with cols_sosmed[1]:
    st.markdown("[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://youtube.com/@DosenSkripsi)")
with cols_sosmed[2]:
    st.markdown("[![TikTok](https://img.shields.io/badge/TikTok-%23000000.svg?style=for-the-badge&logo=TikTok&logoColor=white)](https://tiktok.com/)")

st.write("---")

# --- PRODUK KATEGORI (Data Produk) ---
# Kamu bisa mengubah data di bawah ini sesuai keinginan
products = [
    {
        "nama": "AI Paraphraser Pro",
        "harga": "Rp 45.000",
        "gambar": "https://via.placeholder.com/300x300.png?text=AI+Paraphraser",
        "desc": "Ubah kalimat skripsi agar bebas plagiasi dalam hitungan detik."
    },
    {
        "nama": "Cek Plagiasi Turnitin",
        "harga": "Rp 15.000",
        "gambar": "https://via.placeholder.com/300x300.png?text=Cek+Plagiasi",
        "desc": "Cek skor plagiasi dengan akun instruktur resmi."
    },
    {
        "nama": "Konsultasi Judul AI",
        "harga": "Rp 75.000",
        "gambar": "https://via.placeholder.com/300x300.png?text=Konsultasi+Judul",
        "desc": "Temukan 10 ide judul skripsi yang langsung disetujui dospem."
    },
    {
        "nama": "Template Skripsi Full",
        "harga": "Rp 25.000",
        "gambar": "https://via.placeholder.com/300x300.png?text=Template+Skripsi",
        "desc": "Format otomatis tinggal isi, sesuai standar universitas."
    }
]

# --- DISPLAY PRODUK DALAM GRID ---
cols = st.columns(2) # Membuat 2 kolom seperti tampilan Lazada/e-commerce mobile

for i, p in enumerate(products):
    with cols[i % 2]:
        st.image(p["gambar"], use_container_width=True)
        st.subheader(p["nama"])
        st.write(f"### {p['harga']}")
        st.write(p["desc"])
        if st.button(f"Beli {p['nama']}", key=i):
            st.success(f"Mengarahkan ke WhatsApp untuk {p['nama']}...")
            # Link WA otomatis sesuai nama produk
            wa_link = f"https://wa.me/6281234567890?text=Halo%20Admin,%20saya%20ingin%20beli%20{p['nama']}"
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{wa_link}\'" />', unsafe_allow_index=True)
        st.write("---")

# --- FOOTER ---

st.caption("© 2026 dosbing.ai | Vixelboy Digital Product")
