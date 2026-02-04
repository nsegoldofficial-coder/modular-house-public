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

# --- CUSTOM DESIGN CATALOG ---
new_catalog_file = "Desain_Katalog_Modular_Baru.pdf"

if os.path.exists(new_catalog_file):
    st.success("✨ Desain Katalog Baru Tersedia!")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("Unduh katalog terbaru dengan desain modern dan harga spesial proyek.")
        with open(new_catalog_file, "rb") as f:
            st.download_button(
                label="📥 Download Desain Katalog Baru (PDF)",
                data=f,
                file_name="Katalog_Modular_House_Modern_2026.pdf",
                mime="application/pdf",
                type="primary"
            )
            
    with col2:
        # PDF Preview for New Catalog
        with st.expander("👁️ Lihat Preview Katalog Baru", expanded=True):
            try:
                doc = fitz.open(new_catalog_file)
                for i, page in enumerate(doc):
                    pix = page.get_pixmap(dpi=150)
                    img_data = pix.tobytes("png")
                    st.image(img_data, caption=f"Halaman {i+1}", use_container_width=True)
                    st.divider()
            except Exception as e:
                st.error(f"Error preview: {e}")

else:
    st.warning("Desain katalog baru belum di-generate. Silakan hubungi admin.")

st.caption("© 2026 Modular House. All Rights Reserved.")
