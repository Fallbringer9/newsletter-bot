from openai_utils import get_weekly_news
from pdf_generator import save_text_to_pdf
import boto3


def lambda_handler(event, context):
    news = get_weekly_news()
    if news:
        save_text_to_pdf(news, "/tmp/newsletter.pdf")  # Lambda n'autorise que /tmp
        upload_to_s3("/tmp/newsletter.pdf", "newsletter-pdf-manu", "newsletter.pdf")
        return {
            "statusCode": 200,
            "body": "Newsletter générée et uploadée sur S3 avec succès."
        }
    else:
        return {
            "statusCode": 500,
            "body": "Erreur lors de la génération des actualités."
        }

def upload_to_s3(file_path, bucket_name, s3_key):
    s3 = boto3.client("s3")
    with open(file_path, "rb") as f:
        s3.upload_fileobj(f, bucket_name, s3_key)
