from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import os

def create_catalog(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=1*cm, leftMargin=1*cm,
                            topMargin=1*cm, bottomMargin=2*cm)
    
    styles = getSampleStyleSheet()
    
    # Custom Styles
    style_title = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=32,
        textColor=colors.HexColor('#1a237e'), # Navy Blue
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica-Bold'
    )
    
    style_subtitle = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=16,
        textColor=colors.HexColor('#ff6f00'), # Amber/Orange
        alignment=TA_CENTER,
        spaceAfter=40,
        fontName='Helvetica'
    )
    
    style_heading = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#1a237e'),
        borderPadding=5,
        borderWidth=0,
        spaceBefore=20,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )
    
    style_price = ParagraphStyle(
        'PriceTag',
        parent=styles['Heading3'],
        fontSize=24,
        textColor=colors.HexColor('#2e7d32'), # Green
        alignment=TA_RIGHT,
        fontName='Helvetica-Bold'
    )
    
    style_desc = ParagraphStyle(
        'Description',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.darkgrey,
        leading=16,
        alignment=TA_LEFT
    )

    story = []

    # --- COVER PAGE ---
    story.append(Spacer(1, 4*cm))
    story.append(Paragraph("MODULAR HOUSE", style_title))
    story.append(Paragraph("CATALOG 2026", style_title))
    story.append(Paragraph("Solusi Konstruksi Cepat, Hemat & Modern", style_subtitle))
    
    story.append(Spacer(1, 2*cm))
    
    # Decorative Line
    story.append(Table([['']], colWidths=[18*cm], style=TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 2, colors.HexColor('#1a237e'))
    ])))
    
    story.append(Spacer(1, 5*cm))
    
    # Contact Info on Cover
    contact_data = [
        ["Hubungi Kami:"],
        ["Admin Modular"],
        ["WA: 081244566790"],
        ["Email: admin@modularhouse.com"],
        ["Alamat: Jl. Kyai Kathi Desa No.168, Ngesong, Jepara"]
    ]
    t_contact = Table(contact_data, style=TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.darkgrey),
        ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
    ]))
    story.append(t_contact)
    
    story.append(PageBreak())

    # --- PRODUCT PAGE 1: MODUL UTAMA ---
    story.append(Paragraph("1. Modul Utama (Standard)", style_heading))
    
    # Layout: Description Left, Price Right
    desc_text = """
    <b>Spesifikasi:</b><br/>
    - Ukuran: 3 x 6 Meter (18 m²)<br/>
    - Struktur: Baja Ringan Galvanis<br/>
    - Dinding: Sandwich Panel (Peredam Panas & Suara)<br/>
    - Lantai: Semen Board + Vinyl/PVC<br/>
    - Jendela: Aluminium Sliding Glass<br/>
    - Pintu: Steel Door (Anti Maling)<br/>
    - Kelistrikan: 2 Lampu LED, 1 Saklar, 2 Stop Kontak<br/>
    <br/>
    Cocok untuk kantor proyek (direksi keet), mess karyawan, atau gudang.
    """
    
    p_desc = Paragraph(desc_text, style_desc)
    p_price = Paragraph("Rp 15.000.000<br/><font size=12 color=grey>/ unit</font>", style_price)
    
    # Table for Layout
    data_modul = [[p_desc, p_price]]
    t_modul = Table(data_modul, colWidths=[12*cm, 6*cm])
    t_modul.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BACKGROUND', (0,0), (-1,-1), colors.whitesmoke),
        ('BOX', (0,0), (-1,-1), 1, colors.lightgrey),
        ('TopPadding', (0,0), (-1,-1), 15),
        ('BottomPadding', (0,0), (-1,-1), 15),
        ('LeftPadding', (0,0), (-1,-1), 15),
        ('RightPadding', (0,0), (-1,-1), 15),
    ]))
    story.append(t_modul)
    story.append(Spacer(1, 1*cm))

    # --- PRODUCT PAGE 2: ADD-ONS ---
    story.append(Paragraph("2. Opsi Tambahan (Add-ons)", style_heading))
    
    # Table Header
    addon_data = [
        ["Item", "Deskripsi", "Harga"]
    ]
    
    # Add-on Items
    items = [
        ("Paket Toilet Full Set", "Kloset Duduk, Shower, Wastafel, Partisi, Instalasi Air", "Rp 5.000.000"),
        ("Tangga Baja", "Tangga akses lt. 2, Bordes plat bordes, Railing aman", "Rp 5.000.000"),
        ("Teras Baja (Per 3m)", "Selasar jalan lt. 2, Railing pengaman, Lantai plat bordes", "Rp 1.000.000")
    ]
    
    for name, desc, price in items:
        p_name = Paragraph(f"<b>{name}</b>", style_desc)
        p_desc_item = Paragraph(desc, style_desc)
        p_price_item = Paragraph(f"<b>{price}</b>", ParagraphStyle('subprice', parent=style_desc, alignment=TA_RIGHT, textColor=colors.HexColor('#2e7d32')))
        addon_data.append([p_name, p_desc_item, p_price_item])
        
    t_addon = Table(addon_data, colWidths=[5*cm, 9*cm, 4*cm])
    t_addon.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a237e')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 10),
        ('TOPPADDING', (0,0), (-1,0), 10),
        
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.whitesmoke])
    ]))
    story.append(t_addon)
    
    # Footer function for every page
    def add_footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(colors.grey)
        canvas.drawString(1*cm, 1*cm, "Modular House Catalog 2026")
        canvas.drawRightString(20*cm, 1*cm, "Hubungi: 081244566790")
        canvas.restoreState()

    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"Catalog created: {filename}")

if __name__ == "__main__":
    create_catalog("Desain_Katalog_Modular_Baru.pdf")
