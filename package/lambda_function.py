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

        save_text_to_html(news, "newsletter.html")

        s3 = boto3.client("s3")
        bucket_name = os.getenv("S3_BUCKET_NAME")
        s3.upload_file("newsletter.html", bucket_name, "newsletter.html")

        print(f"✅ Newsletter HTML uploadée sur S3: {bucket_name}/newsletter.html")

    except Exception as e:
        print(f"❌ Erreur Lambda : {e}")

