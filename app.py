import streamlit as st


st.set_page_config(page_title="Skripsi 5K - Template Kerangka Skripsi", layout="wide")

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
    
    <a href="https://wa.me/628131709665?text=Halo%20Admin%20template,%20saya%20tertarik%20dengan%20produknya" class="float-wa" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35">
    </a>
""", unsafe_allow_html=True) 

# --- HEADER ---
st.title("🎓 Template Kerangka Skripsi")
st.subheader("Kerangka Skripsi Cuman Seharga Gorengan")

# --- SOSIAL MEDIA
cols_sosmed = st.columns(6)
with cols_sosmed[0]:
    st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com)")
with cols_sosmed[1]:
    st.markdown("[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@TemplateSkripsi)")
with cols_sosmed[2]:
    st.markdown("[![TikTok](https://img.shields.io/badge/TikTok-%23000000.svg?style=for-the-badge&logo=TikTok&logoColor=white)](https://www.tiktok.com/@templatkerangkaskripsiku)")

st.write("---")


products = [
    {
        "nama": "Template Kerangka Skripsi Umum",
        "harga": "Rp 5.000",
        "gambar": "https://via.placeholder.com/300x300.png?text=AI+Paraphraser",
        "desc": "Kerangka Skripsi Umum di Indonesia"
    },
    {
        "nama": "Buat Judul",
        "harga": "Rp 5.000",
        "gambar": "https://via.placeholder.com/300x300.png?text=Cek+Plagiasi",
        "desc": "Kami Bantu buatkan Judul Skripsi"
    },
    {
        "nama": "Template Kerangka Skripsi Sesuai Univ",
        "harga": "Rp 15.000",
        "gambar": "https://via.placeholder.com/300x300.png?text=Konsultasi+Judul",
        "desc": "Kerangka Skripsi Sesuai Pedoman Prodi, Fakultas, dan Kampusmu."
    },
    {
        "nama": "Cari Ide Penelitian",
        "harga": "Rp 25.000",
        "gambar": "https://via.placeholder.com/300x300.png?text=Template+Skripsi",
        "desc": "Kami bantu cari ide penelitianmu."
    }
]

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
          if st.button(f"Beli {p['nama']}", key=i):
            # Link WA dengan nomor kamu dan pesan otomatis sesuai nama produk
            wa_link = f"https://wa.me/628131709665?text=Halo%20Admin%20dosbing.ai,%20saya%20ingin%20beli%20{p['nama']}"
            
            # Gunakan st.markdown dengan parameter yang benar: unsafe_allow_html
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{wa_link}\'" />', unsafe_allow_html=True)
        st.write("---")

# --- FOOTER ---

st.caption("© 2026 Template Kerangka Skripsiku")




