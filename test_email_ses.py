import boto3

# Adresse mail vérifiée sur SES
SENDER = "test_mail@gmail.com"
RECIPIENT = "test_mail@gmail.com"

# Sujet et corps
SUBJECT = "Test Amazon SES"
BODY_TEXT = "Ceci est un test d’envoi avec Amazon SES via Boto3."

# Init du client SES (région à adapter si nécessaire)
ses = boto3.client('ses', region_name="eu-west-3")

# Envoi du mail
response = ses.send_email(
    Source=SENDER,
    Destination={'ToAddresses': [RECIPIENT]},
    Message={
        'Subject': {'Data': SUBJECT},
        'Body': {'Text': {'Data': BODY_TEXT}}
    }
)

print("E-mail envoyé ! Message ID:", response['MessageId'])
