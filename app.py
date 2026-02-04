import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Modular House Catalog",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (Minimal & Clean) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Remove default top padding */
    .block-container {
        padding-top: 2rem !important;
    }
    
    /* Custom Headers */
    h1, h2, h3 {
        color: #0f172a;
        font-weight: 700;
    }
    
    /* Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
    }
    
    /* Custom Button Style */
    .custom-btn {
        display: inline-block;
        background-color: #2563eb;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        transition: background-color 0.2s;
        text-align: center;
    }
    .custom-btn:hover {
        background-color: #1d4ed8;
        color: white;
    }
    
    .whatsapp-float {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #25D366;
        color: white;
        padding: 12px 24px;
        border-radius: 50px;
        font-weight: bold;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 1000;
        text-decoration: none;
    }
    .whatsapp-float:hover {
        background-color: #128C7E;
        color: white;
    }
    
</style>
""", unsafe_allow_html=True)

# --- HEADER / HERO ---
col_logo, col_title = st.columns([1, 5])
with col_title:
    st.title("Modular House")
    st.markdown("##### Solusi Ruang Cepat, Hemat & Modern")

st.divider()

# --- MAIN PRODUCT SHOWCASE ---
st.markdown("### 🏢 Produk Unggulan: Modul Standart")

# Container for Main Product
with st.container():
    col_img, col_info = st.columns([1.2, 1], gap="large")
    
    with col_img:
        # High quality architectural placeholder
        st.image("https://images.unsplash.com/photo-1496417263034-38ec4f0d665a?auto=format&fit=crop&w=1000&q=80", 
                 caption="Ilustrasi Unit Modular 3x6m", 
                 use_container_width=True)
    
    with col_info:
        st.subheader("Modul Serbaguna 3x6m")
        st.markdown("""
        Unit modular prefabrikasi yang dirancang untuk kecepatan konstruksi dan kenyamanan. 
        Ideal untuk kantor proyek, mess, atau ruang usaha.
        """)
        
        # Price
        st.markdown("""
        <div style="background-color: #eff6ff; padding: 15px; border-radius: 8px; border-left: 4px solid #2563eb; margin: 15px 0;">
            <p style="margin:0; font-size: 0.9rem; color: #64748b;">Harga Satuan</p>
            <p style="margin:0; font-size: 1.5rem; font-weight: 700; color: #2563eb;">Rp 15.000.000</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Specs
        with st.expander("📝 Lihat Spesifikasi Lengkap", expanded=True):
            st.markdown("""
            - **Dimensi:** 600 x 300 x 280 cm
            - **Struktur:** Rangka Baja Galvanis Anti Karat
            - **Dinding:** Sandwich Panel EPS (Insulasi Panas)
            - **Lantai:** Fiber Cement + Vinyl Motif Kayu
            - **Pintu & Jendela:** Pintu Baja & Jendela Sliding Aluminium
            - **Elektrikal:** Sudah termasuk instalasi (Lampu, Saklar, Stop Kontak)
            """)

st.divider()

# --- ADD-ONS SECTION ---
st.markdown("### 🛠️ Opsi Tambahan (Add-ons)")
st.markdown("Lengkapi unit modular Anda dengan paket tambahan berikut:")

# Using columns for cards look
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.image("https://images.unsplash.com/photo-1584622050111-993a426fbf0a?auto=format&fit=crop&w=500&q=80", use_container_width=True)
    st.markdown("**🚿 Paket Toilet Full Set**")
    st.caption("Termasuk kloset, shower, wastafel, & partisi.")
    st.markdown("##### Rp 5.000.000")

with col_b:
    st.image("https://images.unsplash.com/photo-1505330622279-bf7d7fc918f4?auto=format&fit=crop&w=500&q=80", use_container_width=True)
    st.markdown("**🪜 Tangga Baja Outdoor**")
    st.caption("Akses aman ke lantai 2 dengan bordes plat.")
    st.markdown("##### Rp 5.000.000")

with col_c:
    st.image("https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=500&q=80", use_container_width=True)
    st.markdown("**🏞️ Teras & Selasar (Per 3m)**")
    st.caption("Lantai bordes dengan railing pengaman.")
    st.markdown("##### Rp 1.000.000")

st.divider()

# --- DOWNLOADS & CTA ---
col_dl, col_contact = st.columns([1, 1], gap="large")

with col_dl:
    st.subheader("📥 Download Katalog")
    st.write("Dapatkan penawaran lengkap dalam format PDF.")
    
    # Check files
    pdf_catalog = "Desain_Katalog_Modular_Baru.pdf"
    pdf_rab = "Rincian_Anggaran_Kantor_Modular_v3.pdf"
    
    if os.path.exists(pdf_catalog):
        with open(pdf_catalog, "rb") as f:
            st.download_button(
                label="📄 Download Brosur Produk (PDF)",
                data=f,
                file_name="Katalog_Modular_2026.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.warning("⚠️ File katalog sedang diperbarui.")

    if os.path.exists(pdf_rab):
        with open(pdf_rab, "rb") as f:
            st.download_button(
                label="💰 Download Estimasi RAB (PDF)",
                data=f,
                file_name="RAB_Modular_Proyek.pdf",
                mime="application/pdf",
                use_container_width=True
            )

with col_contact:
    st.subheader("📞 Hubungi Kami")
    st.write("Konsultasi gratis untuk kebutuhan proyek Anda.")
    
    st.markdown("""
    **Admin Modular**  
    Jl. Kyai Kathi Desa No.168, Ngesong, Jepara  
    Jawa Tengah, 5942
    """)
    
    st.markdown("""
    <a href="https://wa.me/6281244566790" class="custom-btn" style="width:100%;">
        Chat WhatsApp Sekarang
    </a>
    """, unsafe_allow_html=True)

# Floating Button
st.markdown("""
<a href="https://wa.me/6281244566790" class="whatsapp-float" target="_blank">
    💬 Hubungi Admin
</a>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>© 2026 Modular House Official.</div>", unsafe_allow_html=True)
