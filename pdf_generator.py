from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

def save_text_to_pdf(text, output_path="newsletter.pdf"):
    try:
        doc = SimpleDocTemplate(output_path, pagesize=A4,
                                rightMargin=2*cm, leftMargin=2*cm,
                                topMargin=2*cm, bottomMargin=2*cm)

        styles = getSampleStyleSheet()
        style = styles["Normal"]

        flowables = []
        for line in text.split("\n"):
            if line.strip() != "":
                flowables.append(Paragraph(line.strip(), style))
                flowables.append(Spacer(1, 0.4*cm))

        doc.build(flowables)
        print(f"✅ PDF généré avec succès → {output_path}")

    except Exception as e:
        print(f"❌ Erreur lors de la génération du PDF : {e}")



