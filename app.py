import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Modular House - Modern Catalog",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- IMAGES (DUMMY / CONCEPT) ---
# Using Unsplash images for demonstration
IMG_HERO = "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80" # Modern Office Interior
IMG_MODULAR = "https://images.unsplash.com/photo-1517502884422-41e157d4433c?auto=format&fit=crop&w=800&q=80" # Container/Modular Concept
IMG_TOILET = "https://images.unsplash.com/photo-1584622050111-993a426fbf0a?auto=format&fit=crop&w=600&q=80" # Modern Bathroom
IMG_STAIRS = "https://images.unsplash.com/photo-1505330622279-bf7d7fc918f4?auto=format&fit=crop&w=600&q=80" # Industrial Stairs
IMG_TERRACE = "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=600&q=80" # Terrace/Balcony
IMG_PLAN = "https://images.unsplash.com/photo-1536895058696-a69b1c7be473?auto=format&fit=crop&w=800&q=80" # Blueprints/Plan

# --- CUSTOM CSS STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Fix Streamlit default padding to make Hero look better */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 5rem !important;
    }
    
    .main {
        background-color: #f4f6f9;
    }
    
    /* Hero Section */
    .hero-container {
        position: relative;
        background-image: linear-gradient(rgba(26, 35, 126, 0.85), rgba(13, 71, 161, 0.85)), url('https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80');
        background-size: cover;
        background-position: center;
        color: white;
        padding: 4rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.95;
        font-weight: 300;
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Cards */
    .product-card {
        background: white;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 2rem;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        transition: transform 0.3s ease;
        border: 1px solid #eee;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.12);
    }
    
    /* Flexbox Layout for Main Product */
    .main-product-layout {
        display: flex;
        flex-wrap: wrap;
    }
    .main-product-image {
        flex: 1;
        min-width: 300px;
        background-image: url('https://images.unsplash.com/photo-1517502884422-41e157d4433c?auto=format&fit=crop&w=800&q=80');
        background-size: cover;
        background-position: center;
        min-height: 300px;
    }
    .main-product-content {
        flex: 1;
        padding: 2rem;
        min-width: 300px;
    }
    
    .card-title {
        color: #1a237e;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .price-badge {
        background: #e8f5e9;
        color: #2e7d32;
        font-weight: 700;
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 1.1rem;
        display: inline-block;
        margin-bottom: 1rem;
    }
    
    /* Add-on Items */
    .addon-item {
        display: flex;
        align-items: center;
        padding: 15px;
        border-bottom: 1px solid #f0f0f0;
        transition: background 0.2s;
    }
    .addon-item:last-child {
        border-bottom: none;
    }
    .addon-item:hover {
        background: #fafafa;
    }
    .addon-img {
        width: 80px;
        height: 80px;
        border-radius: 10px;
        object-fit: cover;
        margin-right: 15px;
    }
    .addon-details {
        flex: 1;
    }
    .addon-title {
        font-weight: 600;
        color: #333;
        font-size: 1.1rem;
    }
    .addon-price {
        color: #2e7d32;
        font-weight: 700;
    }
    
    /* Contact Box */
    .contact-box {
        background: linear-gradient(135deg, #1a237e 0%, #283593 100%);
        color: white;
        padding: 3rem;
        border-radius: 20px;
        text-align: center;
        margin-top: 4rem;
        box-shadow: 0 10px 30px rgba(26, 35, 126, 0.2);
    }
    .whatsapp-btn {
        background: #25D366;
        color: white !important;
        text-decoration: none;
        padding: 12px 30px;
        border-radius: 50px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        margin-top: 15px;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
        transition: 0.3s;
    }
    .whatsapp-btn:hover {
        background: #128C7E;
        transform: scale(1.05);
        text-decoration: none;
    }
    
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-container">
    <div class="hero-title">MODULAR HOUSE</div>
    <div class="hero-subtitle">Membangun Masa Depan dengan Solusi Konstruksi Cepat, Hemat, dan Estetik.</div>
</div>
""", unsafe_allow_html=True)

# --- MAIN CONTENT ---
st.markdown("## ✨ Koleksi Produk Unggulan")

# MAIN PRODUCT CARD (Refactored for better alignment)
st.markdown(f"""
<div class="product-card">
    <div class="main-product-layout">
        <div class="main-product-image" style="background-image: url('{IMG_MODULAR}');"></div>
        <div class="main-product-content">
            <div class="card-title">1. Modul Utama (Standard)</div>
            <div class="price-badge">Rp 15.000.000 / unit</div>
            <p style="color: #666; line-height: 1.6; margin-bottom: 1.5rem;">
                Solusi ruang kerja instan berukuran <b>3 x 6 meter</b>. Dirancang khusus untuk kebutuhan kantor proyek, mess karyawan, atau ruang serbaguna. Menggunakan material sandwich panel berkualitas tinggi yang tahan panas dan suara.
            </p>
            <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 15px; border-left: 4px solid #1a237e;">
                <h5 style="color: #1a237e; margin-top: 0; margin-bottom: 10px;">Spesifikasi Premium:</h5>
                <ul style="padding-left: 1.2rem; margin-bottom: 0; color: #555;">
                    <li><b>Dimensi:</b> 3x6m (18 m²)</li>
                    <li><b>Struktur:</b> Baja Ringan Galvanis</li>
                    <li><b>Dinding:</b> Sandwich Panel EPS</li>
                    <li><b>Lantai:</b> Vinyl Wood Texture</li>
                    <li><b>Pintu/Jendela:</b> Steel Door & Sliding Glass</li>
                    <li><b>Listrik:</b> Full Instalasi (Lampu LED, Stop Kontak)</li>
                </ul>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- GRID LAYOUT FOR ADDONS & DOWNLOADS ---
col_left, col_right = st.columns([3, 2], gap="large")

with col_left:
    st.markdown("### 🛠️ Paket & Aksesoris Tambahan")
    
    st.markdown("""
    <div class="product-card">
        <div class="card-content">
            <h4 style="color: #1a237e; margin-bottom: 1.5rem;">Pilihan Upgrade Proyek</h4>
    """, unsafe_allow_html=True)
    
    # Add-on 1
    st.markdown(f"""
    <div class="addon-item">
        <img src="{IMG_TOILET}" class="addon-img">
        <div class="addon-details">
            <div class="addon-title">Paket Toilet Full Set</div>
            <div style="font-size: 0.9rem; color: #666;">Kloset duduk, shower, wastafel, partisi & instalasi</div>
        </div>
        <div class="addon-price">Rp 5.000.000</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add-on 2
    st.markdown(f"""
    <div class="addon-item">
        <img src="{IMG_STAIRS}" class="addon-img">
        <div class="addon-details">
            <div class="addon-title">Tangga Baja Outdoor</div>
            <div style="font-size: 0.9rem; color: #666;">Akses lt. 2, plat bordes kokoh, railing safety</div>
        </div>
        <div class="addon-price">Rp 5.000.000</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add-on 3
    st.markdown(f"""
    <div class="addon-item">
        <img src="{IMG_TERRACE}" class="addon-img">
        <div class="addon-details">
            <div class="addon-title">Teras & Selasar Baja (Per 3m)</div>
            <div style="font-size: 0.9rem; color: #666;">Lantai plat bordes & railing pengaman</div>
        </div>
        <div class="addon-price">Rp 1.000.000</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

with col_right:
    st.markdown("### 📥 Dokumen Proyek")
    
    # Visualization Card
    st.markdown(f"""
    <div class="product-card" style="padding: 0;">
        <img src="{IMG_PLAN}" style="width: 100%; height: 250px; object-fit: cover;">
        <div style="padding: 1.5rem;">
            <div style="font-weight: bold; color: #333; margin-bottom: 0.5rem;">Visualisasi Denah</div>
            <div style="font-size: 0.9rem; color: #666; margin-bottom: 1rem;">Ilustrasi layout standar untuk unit modular 3x6m.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Downloads
    if os.path.exists("Desain_Katalog_Modular_Baru.pdf"):
        with open("Desain_Katalog_Modular_Baru.pdf", "rb") as f:
            st.download_button(
                label="📄 Download Katalog PDF",
                data=f,
                file_name="Katalog_Modular_2026.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.warning("File Katalog tidak ditemukan.")
    
    if os.path.exists("Rincian_Anggaran_Kantor_Modular_v3.pdf"):
        with open("Rincian_Anggaran_Kantor_Modular_v3.pdf", "rb") as f:
            st.download_button(
                label="💰 Download RAB Detail PDF",
                data=f,
                file_name="RAB_Modular_Proyek.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.warning("File RAB tidak ditemukan.")

# --- CONTACT CTA ---
st.markdown("""
<div class="contact-box">
    <h2 style="margin-bottom: 10px;">Siap Memulai Proyek Anda?</h2>
    <p style="font-size: 1.1rem; opacity: 0.9;">Konsultasikan kebutuhan ruang modular Anda bersama tim ahli kami.</p>
    
    <div style="margin-top: 30px;">
        <p style="font-size: 1.3rem; margin-bottom: 5px;">📞 <b>Admin Modular</b></p>
        <p style="margin-bottom: 20px;">Jl. Kyai Kathi Desa No.168, Ngesong, Jepara, Jawa Tengah</p>
        
        <a href="https://wa.me/6281244566790" target="_blank" class="whatsapp-btn">
            Chat WhatsApp Sekarang
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 4rem; padding-bottom: 2rem; color: #888; border-top: 1px solid #eee; padding-top: 2rem;">
    <small>© 2026 Modular House. All Rights Reserved.</small>
</div>
""", unsafe_allow_html=True)
