import fitz

def revise_catalog(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    
    # New Contact Info
    new_info = {
        "name": "Admin Modular",
        "wa": "081244566790",
        "email": "admin@modularhouse.com",
        "address": "Jl. Kyai Kathi Desa No.168, Ngesong, Kecapi, Kec. Tahunan, Jepara, Jawa Tengah 5942"
    }
    
    # Redact terms
    redact_terms = ["Sindi", "+62813-3031-6119", "0813-3031-6119", "Kecapi, Jepara, Jawa Tengah"]
    
    for page_num, page in enumerate(doc):
        # 1. Redact specific terms wherever found
        for term in redact_terms:
            quads = page.search_for(term)
            if quads:
                for quad in quads:
                    rect = fitz.Rect(quad)
                    # Add white redaction
                    page.add_redact_annot(rect, fill=(1, 1, 1))
        
        # Apply redactions to clear the text
        page.apply_redactions()
        
        # 2. Add New Footer Info
        # We'll draw a white rectangle at the bottom to ensure a clean slate for the footer area
        # typical footer height ~ 60-80 units from bottom
        footer_height = 80
        footer_rect = fitz.Rect(0, page.rect.height - footer_height, page.rect.width, page.rect.height)
        
        # Draw white background for footer
        shape = page.new_shape()
        shape.draw_rect(footer_rect)
        shape.finish(color=None, fill=(1, 1, 1)) # White fill, no border
        shape.commit()
        
        # 3. Write New Text
        # We will center the text for a professional look
        text_writer = fitz.TextWriter(page.rect)
        
        # Center X position
        center_x = page.rect.width / 2
        bottom_y = page.rect.height - 50
        
        # Style 1: Name & WA (Bold/Large)
        header_text = f"Hubungi: {new_info['name']} | WA: {new_info['wa']}"
        text_writer.append((center_x - (len(header_text)*3), bottom_y), header_text, fontsize=12, font=fitz.Font("Helvetica-Bold"))
        
        # Style 2: Address (Normal/Small)
        addr_text = new_info['address']
        text_writer.append((center_x - (len(addr_text)*2.2), bottom_y + 15), addr_text, fontsize=9, font=fitz.Font("Helvetica"))
        
        # Style 3: Email (Blue)
        email_text = f"Email: {new_info['email']}"
        # We use insert_text for color support easier than TextWriter sometimes for single lines
        page.insert_text((center_x - (len(email_text)*2.5), bottom_y + 30), email_text, fontsize=10, color=(0, 0, 1), fontname="Helvetica")
        
        text_writer.write_text(page)

    doc.save(output_path)
    print(f"Revised catalog saved to: {output_path}")

input_pdf = r"katalog modular/2026 Katalog Modular House PT Pingan Struktur Baja_Sindi.pdf"
output_pdf = "Revisi_Katalog_Modular_2026.pdf"

revise_catalog(input_pdf, output_pdf)
