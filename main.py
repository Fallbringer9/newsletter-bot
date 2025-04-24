from openai_utils import get_weekly_news
from pdf_generator import save_text_to_pdf
from s3_utils import upload_to_s3  # ou direct dans pdf_generator

def main():
    print("📥 Récupération de l’actu...")
    news = get_weekly_news()
    if news:
        print("🧾 Génération du PDF...")
        pdf_path = "newsletter.pdf"
        save_text_to_pdf(news, pdf_path)

        print("☁️ Upload vers S3...")
        upload_to_s3(pdf_path, "newsletter-pdf-manu", "newsletter.pdf")
    else:
        print("❌ Actu non récupérée")

if __name__ == "__main__":
    main()


