import streamlit as st
from PIL import Image
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Modular House - Modern Catalog",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS STYLING ---
st.markdown("""
<style>
    /* Global Font & Colors */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background-color: #f8f9fa;
    }
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #1a237e 0%, #0d47a1 100%);
        color: white;
        padding: 4rem 2rem;
        border-radius: 0 0 20px 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 300;
    }
    
    /* Product Card */
    .product-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-left: 5px solid #1a237e;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    .card-title {
        color: #1a237e;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .price-tag {
        color: #2e7d32;
        font-size: 1.6rem;
        font-weight: 700;
        background: #e8f5e9;
        padding: 0.2rem 1rem;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 1rem;
    }
    
    .feature-list {
        list-style-type: none;
        padding: 0;
    }
    .feature-item {
        margin-bottom: 0.5rem;
        padding-left: 1.5rem;
        position: relative;
        color: #555;
    }
    .feature-item:before {
        content: "✓";
        color: #1a237e;
        position: absolute;
        left: 0;
        font-weight: bold;
    }
    
    /* Contact Section */
    .contact-box {
        background: #1a237e;
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 3rem;
    }
    .contact-btn {
        background: #25D366;
        color: white;
        text-decoration: none;
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
        transition: 0.3s;
    }
    .contact-btn:hover {
        background: #128C7E;
        color: white;
    }
    
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-container">
    <div class="hero-title">MODULAR HOUSE</div>
    <div class="hero-subtitle">Solusi Konstruksi Cepat, Hemat & Modern untuk Masa Depan</div>
</div>
""", unsafe_allow_html=True)

# --- PRODUCT SHOWCASE ---
st.markdown("## ✨ Produk Unggulan")

col1, col2 = st.columns([3, 2], gap="large")

with col1:
    # --- PRODUCT 1: MAIN MODULE ---
    st.markdown("""
    <div class="product-card">
        <div class="card-title">1. Modul Utama (Standard)</div>
        <div class="price-tag">Rp 15.000.000 / unit</div>
        <p>Unit modular serbaguna berukuran 3x6 meter. Ideal untuk kantor direksi keet, mess karyawan, atau gudang penyimpanan. Dibuat dengan struktur baja ringan yang kokoh dan sandwich panel yang nyaman.</p>
        <hr/>
        <h4>Spesifikasi Teknis:</h4>
        <ul class="feature-list">
            <li class="feature-item"><b>Dimensi:</b> 3 x 6 Meter (Luas 18 m²)</li>
            <li class="feature-item"><b>Struktur:</b> Baja Ringan Galvanis (Anti Karat)</li>
            <li class="feature-item"><b>Dinding:</b> Sandwich Panel EPS (Peredam Panas & Suara)</li>
            <li class="feature-item"><b>Lantai:</b> Semen Board dilapisi Vinyl/PVC Wood Texture</li>
            <li class="feature-item"><b>Pintu & Jendela:</b> Steel Door & Aluminium Sliding Window</li>
            <li class="feature-item"><b>Kelistrikan:</b> Termasuk Instalasi (2 Lampu, 1 Saklar, 2 Stop Kontak)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # --- PRODUCT 2: ADD-ONS ---
    st.markdown("""
    <div class="product-card" style="border-left-color: #ff6f00;">
        <div class="card-title" style="color: #e65100;">2. Paket Tambahan (Add-ons)</div>
        <p>Lengkapi kebutuhan modular Anda dengan opsi tambahan berikut:</p>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 10px;">
            <div>
                <b style="font-size: 1.1rem;">🚿 Paket Toilet Full Set</b><br/>
                <span style="font-size: 0.9rem; color: #666;">Kloset duduk, shower, wastafel, partisi, instalasi air</span>
            </div>
            <div style="color: #2e7d32; font-weight: bold; font-size: 1.2rem;">Rp 5.000.000</div>
        </div>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 10px;">
            <div>
                <b style="font-size: 1.1rem;">🪜 Tangga Baja</b><br/>
                <span style="font-size: 0.9rem; color: #666;">Akses lantai 2, bordes plat bordes, railing aman</span>
            </div>
            <div style="color: #2e7d32; font-weight: bold; font-size: 1.2rem;">Rp 5.000.000</div>
        </div>
        
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <b style="font-size: 1.1rem;">🏞️ Teras Baja (Per 3m)</b><br/>
                <span style="font-size: 0.9rem; color: #666;">Selasar jalan lt. 2, railing pengaman, lantai plat bordes</span>
            </div>
            <div style="color: #2e7d32; font-weight: bold; font-size: 1.2rem;">Rp 1.000.000</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # --- VISUALIZATION / IMAGE ---
    st.markdown("### 🖼️ Visualisasi Denah")
    
    # Check if temp image exists from previous extraction
    img_path = "temp_floor_plan.png"
    # Or try to get it from PDF if not exists
    if not os.path.exists(img_path):
        import fitz
        try:
            doc = fitz.open("Rincian_Anggaran_Kantor_Modular_v3.pdf") # Use the generated PDF as source if available
            # Wait, better to use the source catalog if possible or just placeholder
            # Let's try to extract from the generated PDF V3 which we know has the image
            page = doc.load_page(0)
            # This page has the image drawn on it, but extracting it back might be tricky as a raw image
            # Let's just render the page itself as the preview
            pix = page.get_pixmap()
            pix.save("preview_render.png")
            img_path = "preview_render.png"
        except:
            pass
            
    if os.path.exists(img_path):
        st.image(img_path, caption="Layout & Denah Modular", use_container_width=True)
    else:
        # Fallback Placeholder styling
        st.markdown("""
        <div style="background: #ddd; height: 300px; display: flex; align-items: center; justify-content: center; border-radius: 10px; color: #666;">
            [Visualisasi Denah Tidak Tersedia]
        </div>
        """, unsafe_allow_html=True)
    
    # --- DOWNLOAD SECTION ---
    st.markdown("### 📥 Download Dokumen")
    
    with open("Desain_Katalog_Modular_Baru.pdf", "rb") as f:
        st.download_button(
            label="📄 Download Katalog (PDF)",
            data=f,
            file_name="Katalog_Modular_2026.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        
    with open("Rincian_Anggaran_Kantor_Modular_v3.pdf", "rb") as f:
        st.download_button(
            label="💰 Download RAB Proyek (PDF)",
            data=f,
            file_name="RAB_Modular_Proyek.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# --- CONTACT CTA ---
st.markdown("""
<div class="contact-box">
    <h2>Tertarik dengan Produk Kami?</h2>
    <p>Hubungi kami sekarang untuk konsultasi gratis dan penawaran terbaik.</p>
    <div style="margin-top: 20px;">
        <p style="font-size: 1.2rem;">📞 <b>Admin Modular</b></p>
        <p>Jl. Kyai Kathi Desa No.168, Ngesong, Jepara</p>
        <a href="https://wa.me/6281244566790" target="_blank" class="contact-btn">
            Chat WhatsApp: 0812-4456-6790
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; color: #888; font-size: 0.8rem;">
    © 2026 Modular House. All Rights Reserved.
</div>
""", unsafe_allow_html=True)
