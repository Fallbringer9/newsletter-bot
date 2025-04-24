# newsletter-bot

Script Python pour générer une newsletter hebdomadaire (PDF) contenant les 5 actualités les plus importantes dans les domaines suivants :
- Développement Web
- Technologies
- Cloud Computing

Le fichier est généré via l'API OpenAI, exporté en PDF, puis téléversé sur AWS S3.

---

## Description (EN)

Python script that automatically generates a weekly newsletter (PDF) covering 5 key updates in:
- Web development
- Technology
- Cloud computing

The content is generated using OpenAI's API, then converted to PDF and uploaded to AWS S3.

---

## Fonctionnalités / Features

- Résumé hebdomadaire généré avec l'API OpenAI
- Création automatique d’un fichier PDF avec `reportlab`
- Envoi du fichier sur un bucket AWS S3 via `boto3`
- Variables d’environnement sécurisées avec `python-dotenv`
- Prochaines étapes : automatisation via AWS Lambda et envoi par email via AWS SES

---

## Stack technique / Tech Stack

- Python 3.11
- openai==0.28.1
- boto3
- reportlab
- python-dotenv
- AWS S3

---

## Installation

Cloner le projet et installer les dépendances :

```bash
git clone https://github.com/Fallbringer9/newsletter-bot.git
cd newsletter-bot
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
