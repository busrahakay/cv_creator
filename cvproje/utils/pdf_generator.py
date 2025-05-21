from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Image
import os

def register_fonts():
    # Font dosyasının yolu
    font_path = os.path.join('static', 'fonts', 'DejaVuSans.ttf')
    
    # Fontu kaydet
    pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))

def create_pdf_with_turkish(text, output, cv_data=None):
    # Fontları kaydet
    register_fonts()
    
    # PDF oluştur
    c = canvas.Canvas(output, pagesize=letter)
    width, height = letter
    
    # Kenar boşlukları
    left_margin = 50
    right_margin = 50
    content_width = width - left_margin - right_margin
    
    # Şablon rengini belirle
    if cv_data and cv_data.template == 'template1':
        color = colors.HexColor('#0d6efd')
    elif cv_data and cv_data.template == 'template2':
        color = colors.HexColor('#198754')
    else:
        color = colors.HexColor('#6f42c1')
    
    def draw_header(y_position):
        # Arka plan şeridi
        c.setFillColor(color)
        # Şeridi sayfanın en üstünden başlat ve kişisel bilgilerin bittiği yerde bitir
        c.rect(0, y_position - 3.35*inch, width, y_position - 3.35*inch, fill=True)
        
        # Fotoğraf ekle
        if cv_data and cv_data.photo:
            try:
                img = Image(cv_data.photo.path, width=1.5*inch, height=1.5*inch)
                # Fotoğrafı sayfanın üst kısmına yerleştir
                img.drawOn(c, width/2 - 0.75*inch, y_position - 2*inch)
            except:
                pass
        
        # Başlık (İsim)
        c.setFont('DejaVuSans', 20)
        c.setFillColor(colors.white)  # İsim rengini beyaz yap
        c.drawCentredString(width/2, y_position - 2.8*inch, cv_data.name if cv_data else "CV")
        
        # İletişim bilgileri
        c.setFont('DejaVuSans', 10)
        c.setFillColor(colors.white)  # İletişim bilgilerini beyaz yap
        c.drawCentredString(width/2, y_position - 3.2*inch, f"Email: {cv_data.email}")
        c.drawCentredString(width/2, y_position - 3.35*inch, f"Telefon: {cv_data.phone}")
        
        return y_position - 3.8*inch  # Header sonrası y pozisyonunu döndür
    
    def draw_content(start_y, lines):
        y = start_y
        page_number = 1
        
        for line in lines:
            if line.strip():  # Boş satırları atla
                # Sayfa sonu kontrolü
                if y < 50:  # Alt kenar boşluğu
                    c.showPage()  # Yeni sayfa
                    page_number += 1
                    y = height - 50  # Yeni sayfanın üst kenar boşluğu
                    
                    # Yeni sayfada sayfa numarası
                    c.setFont('DejaVuSans', 8)
                    c.setFillColor(colors.gray)
                    c.drawCentredString(width/2, 30, f'Sayfa {page_number}')
                
                if line.isupper() and len(line) < 20:  # Başlık satırları
                    c.setFillColor(color)
                    c.setFont('DejaVuSans', 12)
                    c.drawString(left_margin, y, line)
                    y -= 20
                    c.setFillColor(colors.black)
                    c.setFont('DejaVuSans', 10)
                else:
                    # Uzun satırları kelime kelime böl
                    words = line.split()
                    current_line = ""
                    
                    for word in words:
                        test_line = current_line + " " + word if current_line else word
                        if c.stringWidth(test_line, 'DejaVuSans', 10) < content_width:
                            current_line = test_line
                        else:
                            c.drawString(left_margin, y, current_line)
                            y -= 15
                            current_line = word
                    
                    if current_line:
                        # Pozisyon bilgisi kontrolü
                        if " - " in current_line and not current_line.startswith("•"):
                            c.setFillColor(colors.black)  # Pozisyon bilgisini siyah yap
                        c.drawString(left_margin, y, current_line)
                        y -= 15
    
    # İlk sayfanın header'ını çiz
    current_y = draw_header(height)
    
    # İçeriği çiz
    lines = text.split('\n')
    draw_content(current_y, lines)
    
    # PDF'i kaydet
    c.save()

# Örnek kullanım
if __name__ == "__main__":
    sample_text = "Merhaba Dünya! Türkçe karakterler: ç, ğ, ı, ö, ş, ü"
    create_pdf_with_turkish(sample_text, "output.pdf") 