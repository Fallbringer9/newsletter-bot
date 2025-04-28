from openai_utils import get_weekly_news
from html_generator import save_text_to_html
from s3_utils import upload_to_s3  # ou directement dans html_generator

def main():
    print("📥 Récupération de l’actu...")
    news = get_weekly_news()
    if news:
        print("🧾 Génération du HTML...")
        html_path = "/tmp/newsletter.html"  # Enregistre le fichier dans un répertoire temporaire
        save_text_to_html(news, html_path)

        print("☁️ Upload vers S3...")
        upload_to_s3(html_path, "newsletter-pdf-manu", "newsletter.html")  # Upload en S3
    else:
        print("❌ Actu non récupérée")

if __name__ == "__main__":
    main()



