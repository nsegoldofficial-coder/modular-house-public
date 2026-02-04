import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import os

# Page Config
st.set_page_config(
    page_title="Katalog Produk - Modular House",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar - Contact Info
with st.sidebar:
    st.title("Hubungi Kami")
    st.info(
        """
        **Admin Modular**
        
        📱 WhatsApp:  
        [081244566790](https://wa.me/6281244566790)
        
        📧 Email:  
        admin@modularhouse.com
        
        📍 Alamat:  
        Jl. Kyai Kathi Desa No.168, Ngesong,  
        Kecapi, Kec. Tahunan,  
        Kabupaten Jepara, Jawa Tengah 5942
        """
    )

# Main Content
st.title("🏠 Katalog Produk Modular House 2026")
st.markdown("#### Solusi Hunian & Kantor Modular Berkualitas")

catalog_file = "Revisi_Katalog_Modular_2026.pdf"

if os.path.exists(catalog_file):
    # Download Button
    with open(catalog_file, "rb") as f:
        st.download_button(
            label="📄 Download Katalog Lengkap (PDF)",
            data=f,
            file_name="Katalog_Modular_House_2026.pdf",
            mime="application/pdf",
            type="primary"
        )
    
    st.divider()
    
    # PDF Viewer (Image based)
    st.subheader("Preview Katalog")
    
    try:
        doc = fitz.open(catalog_file)
        # Display all pages
        for i, page in enumerate(doc):
            pix = page.get_pixmap(dpi=150) # Higher DPI for better quality
            img_data = pix.tobytes("png")
            
            st.image(img_data, caption=f"Halaman {i+1}", use_container_width=True)
            st.divider()
            
    except Exception as e:
        st.error(f"Gagal memuat preview katalog: {e}")
        
else:
    st.error("File katalog tidak ditemukan. Harap hubungi administrator.")

st.caption("© 2026 Modular House. All Rights Reserved.")
