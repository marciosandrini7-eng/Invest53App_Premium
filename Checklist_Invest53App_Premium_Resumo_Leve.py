from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas

def gerar_checklist():
    pdf_path = "Invest53App_Checklist.pdf"
    c = canvas.Canvas(pdf_path, pagesize=landscape(A4))

    # Fundo cinza grafite metálico
    c.setFillColorRGB(0.15, 0.15, 0.17)
    c.rect(0, 0, 842, 595, stroke=0, fill=1)

    # Título dourado metálico
    c.setFillColorRGB(0.85, 0.68, 0.25)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(421, 520, "💼 Prompts Oficiais – Invest.53App (Edição Premium)")

    # Seções principais
    c.setFont("Helvetica", 16)
    c.setFillColorRGB(0.8, 0.8, 0.8)
    seções = [
        "🧠 Desenvolvimento",
        "🎨 Design",
        "🔒 Segurança",
        "☁️ Deploy",
        "📜 Licenciamento"
    ]
    y = 460
    for seção in seções:
        c.drawString(80, y, seção)
        y -= 40

    # Créditos finais
    c.setFont("Helvetica-Oblique", 12)
    c.setFillColorRGB(0.7, 0.7, 0.7)
    c.drawCentredString(421, 60, "Desenvolvido por Investidor aos 50")

    c.save()

if __name__ == "__main__":
    gerar_checklist()
