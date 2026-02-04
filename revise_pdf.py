import fitz

def revise_catalog(pdf_path, output_path):
    doc = fitz.open(pdf_path)

    # New Contact Info
    new_info = {
        "name": "Admin Modular",
        "wa": "081244566790",
        "address_line1": "Jl. Kyai Kathi Desa No.168, Ngesong,",
        "address_line2": "Kecapi, Kec. Tahunan, Jepara,",
        "address_line3": "Jawa Tengah 5942",
        "email": "admin@modularhouse.com"
    }

    # Terms to redact
    redact_terms = ["Sindi", "+62813-3031-6119", "Kecapi, Jepara, Jawa Tengah", "0813-3031-6119"]

    for page in doc:
        # 1. Search and Redact Old Info
        for term in redact_terms:
            quads = page.search_for(term)
            if quads:
                for quad in quads:
                    # Expand rect slightly to cover surroundings if needed      
                    rect = fitz.Rect(quad)
                    # Add redaction
                    page.add_redact_annot(rect, fill=(1, 1, 1)) # White fill    

        # Apply redactions
        page.apply_redactions()

        # 2. Insert New Info (at the bottom or specific location)
        # Based on previous coord analysis, the contact info is mostly at the bottom
        # y > 900

        # We'll place a clean white box at the bottom to ensure clean background for new text
        # The typical footer area seems to be around y=950 to y=1000+
        footer_rect = fitz.Rect(0, page.rect.height - 100, page.rect.width, page.rect.height)

        # Draw white rectangle over footer area to clear old complex layouts if any
        # shape = page.new_shape()
        # shape.draw_rect(footer_rect)
        # shape.finish(color=(1, 1, 1), fill=(1, 1, 1))
        # shape.commit()

        # Instead of clearing everything (which might remove logos), let's just write new text
        # clearly at the bottom center/left

        text_writer = fitz.TextWriter(page.rect)

        # Font settings
        font_size = 10
        # font = fitz.Font("helv") # Default Helvetica

        # Calculate positions
        start_y = page.rect.height - 80
        left_margin = 50

        # Draw New Info
        # Name & WA
        page.insert_text((left_margin, start_y), f"Hubungi: {new_info['name']} | WA: {new_info['wa']}", fontsize=12, color=(0, 0, 0))

        # Address
        page.insert_text((left_margin, start_y + 15), new_info['address_line1'], fontsize=9, color=(0.2, 0.2, 0.2))
        page.insert_text((left_margin, start_y + 27), new_info['address_line2'], fontsize=9, color=(0.2, 0.2, 0.2))
        page.insert_text((left_margin, start_y + 39), new_info['address_line3'], fontsize=9, color=(0.2, 0.2, 0.2))

        # Email
        page.insert_text((left_margin, start_y + 55), f"Email: {new_info['email']}", fontsize=10, color=(0, 0, 1)) # Blue for email

    doc.save(output_path)
    print(f"Revised catalog saved to: {output_path}")

input_pdf = r"katalog modular/2026 Katalog Modular House PT Pingan Struktur Baja_Sindi.pdf"
output_pdf = "Revisi_Katalog_Modular_2026.pdf"

revise_catalog(input_pdf, output_pdf)
