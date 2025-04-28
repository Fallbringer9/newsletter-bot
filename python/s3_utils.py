import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def upload_to_s3(file_path, bucket_name, s3_key):
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_DEFAULT_REGION")
        )

        with open(file_path, "rb") as f:
            s3.upload_fileobj(f, bucket_name, s3_key)

        print(f"✅ Fichier uploadé sur S3 : s3://{bucket_name}/{s3_key}")
    except boto3.exceptions.S3UploadFailedError as e:
        print(f"❌ Erreur d'upload sur S3 : {e}")
    except boto3.exceptions.S3DownloadError as e:
        print(f"❌ Erreur lors du téléchargement depuis S3 : {e}")
    except Exception as e:
        print(f"❌ Erreur générale lors de l'upload sur S3 : {e}")

