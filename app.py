import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import os

# Page Config
st.set_page_config(
    page_title="Modular House Catalog",
    page_icon="🏠",
    layout="wide"
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
st.title("🏠 Modular House Catalog & Budget Plan")
st.markdown("### Solusi Kantor Modular Cepat, Efisien, dan Berkualitas")

st.divider()

# Section 1: Catalog
st.header("1. Katalog Produk 2026")
st.write("Unduh katalog terbaru kami yang berisi spesifikasi lengkap dan harga modul.")

catalog_file = "Revisi_Katalog_Modular_2026.pdf"
if os.path.exists(catalog_file):
    with open(catalog_file, "rb") as f:
        st.download_button(
            label="📄 Download Katalog Revisi (PDF)",
            data=f,
            file_name=catalog_file,
            mime="application/pdf"
        )
else:
    st.error(f"File {catalog_file} tidak ditemukan. Harap upload file ini ke repository.")

st.divider()

# Section 2: Budget Plan
st.header("2. Rincian Anggaran (RAB)")
st.write("Estimasi biaya untuk proyek **Kantor Keet Standart (2 Lantai)**.")

budget_file = "Rincian_Anggaran_Kantor_Modular_v3.pdf"

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Ringkasan Biaya")
    st.dataframe(
        {
            "Item Pekerjaan": ["Modul Utama (20 Unit)", "Paket Toilet (2 Set)", "Tangga Baja (2 Unit)", "Teras Baja (10 Unit)"],
            "Harga Satuan": ["Rp 15.000.000", "Rp 5.000.000", "Rp 5.000.000", "Rp 1.000.000"],
            "Total": ["Rp 300.000.000", "Rp 10.000.000", "Rp 10.000.000", "Rp 10.000.000"]
        },
        hide_index=True
    )
    st.metric(label="Total Estimasi Anggaran", value="Rp 330.000.000")

    if os.path.exists(budget_file):
        with open(budget_file, "rb") as f:
            st.download_button(
                label="📥 Download RAB Detail (PDF)",
                data=f,
                file_name=budget_file,
                mime="application/pdf"
            )

with col2:
    st.subheader("Preview Denah")
    # Try to extract image from PDF for preview
    if os.path.exists(budget_file):
        try:
            doc = fitz.open(budget_file)
            page = doc.load_page(0) 
            pix = page.get_pixmap()
            img_data = pix.tobytes("png")
            st.image(img_data, caption="Preview Dokumen Anggaran", use_container_width=True)
        except Exception as e:
            st.warning("Preview gambar tidak tersedia.")
    else:
        st.warning("File anggaran belum tersedia.")

st.divider()
st.caption("© 2026 Modular House. All Rights Reserved.")
