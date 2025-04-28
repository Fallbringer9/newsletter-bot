from openai_utils import get_weekly_news
from html_generator import save_text_to_html
import boto3
import os

def lambda_handler(event, context):
    try:
        print("🔍 Récupération des actus tech/cloud/dev en cours...")
        news = get_weekly_news()

        if not news:
            print("❌ Impossible de générer le contenu de la newsletter.")
            return

        # Enregistrement du fichier HTML dans le répertoire temporaire de Lambda
        file_path = "/tmp/newsletter.html"
        save_text_to_html(news, file_path)

        # Connexion à S3 et upload du fichier
        s3 = boto3.client("s3")
        bucket_name = os.getenv("S3_BUCKET_NAME")
        s3.upload_file(file_path, bucket_name, "newsletter.html")

        print(f"✅ Newsletter HTML uploadée sur S3: {bucket_name}/newsletter.html")

    except Exception as e:
        print(f"❌ Erreur Lambda : {e}")


