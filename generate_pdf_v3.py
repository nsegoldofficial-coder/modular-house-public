import fitz  # PyMuPDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from datetime import datetime
import os

def extract_first_page_as_image(pdf_path, output_image_path):
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)  # first page
        pix = page.get_pixmap()
        pix.save(output_image_path)
        return True
    except Exception as e:
        print(f"Error extracting image: {e}")
        return False

def generate_budget_pdf(filename):
    # 1. Extract Floor Plan Image
    source_pdf = r"katalog modular/KANTOR KEET STANDART STRATEK[1]-Model1.pdf"  
    image_path = "temp_floor_plan.png"

    has_image = extract_first_page_as_image(source_pdf, image_path)

    # 2. Create PDF
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Rincian Anggaran Pembangunan Kantor Modular")

    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, f"Tanggal: {datetime.now().strftime('%d %B %Y')}")
    c.drawString(50, height - 85, "Proyek: Kantor Keet Standart (2 Lantai)")    

    # Floor Plan Image
    image_y_pos = height - 400 # Adjust position
    if has_image:
        # Scale image to fit width
        img_width = width - 100
        img_height = 300 # Max height
        c.drawImage(image_path, 50, image_y_pos, width=img_width, height=img_height, preserveAspectRatio=True)
    else:
        # Fallback placeholder
        c.setStrokeColor(colors.black)
        c.rect(50, image_y_pos, width - 100, 250)
        c.drawCentredString(width / 2, image_y_pos + 125, "[Gagal Memuat Gambar Denah]")

    # Table Data
    data = [
        ["No", "Item Pekerjaan", "Vol", "Harga Satuan", "Total Harga"]
    ]

    items = [
        {"name": "Modul Utama (3x6m)", "vol": 20, "price": 15000000},
        {"name": "Paket Toilet Full Set", "vol": 2, "price": 12000000 - 7000000},
        {"name": "Tangga Baja", "vol": 2, "price": 12000000 - 7000000},
        {"name": "Teras Baja (Lt. 2 per 3m)", "vol": 10, "price": 8000000 - 7000000}
    ]

    total_budget = 0

    for i, item in enumerate(items, 1):
        total = item["vol"] * item["price"]
        total_budget += total

        f_price = f"Rp {item['price']:,}".replace(",", ".")
        f_total = f"Rp {total:,}".replace(",", ".")

        data.append([str(i), item["name"], f"{item['vol']} Unit", f_price, f_total])

    # Table Style
    table = Table(data, colWidths=[30, 200, 60, 100, 100])
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Draw Table BELOW the image
    table_y_pos = image_y_pos - 150
    table.wrapOn(c, width, height)
    table.drawOn(c, 50, image_y_pos - 130)

    # Total
    c.setFont("Helvetica-Bold", 12)
    c.drawString(350, image_y_pos - 150, f"TOTAL ANGGARAN: Rp {total_budget:,}".replace(",", "."))

    # Price Details (Rincian Harga)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, image_y_pos - 180, "Rincian Harga:")
    c.setFont("Helvetica", 10)
    c.drawString(60, image_y_pos - 195, "1. Harga Modul Utama: Rp 15.000.000 / unit")
    c.drawString(60, image_y_pos - 210, "2. Harga Paket Toilet: Rp 5.000.000 / paket")
    c.drawString(60, image_y_pos - 225, "3. Harga Tangga Baja: Rp 5.000.000 / unit")
    c.drawString(60, image_y_pos - 240, "4. Harga Teras Baja: Rp 1.000.000 / 3m")

    c.save()
    print(f"PDF Generated: {filename}")

    # Cleanup temp image
    if has_image and os.path.exists(image_path):
        os.remove(image_path)

if __name__ == "__main__":
    generate_budget_pdf("Rincian_Anggaran_Kantor_Modular_v3.pdf")
