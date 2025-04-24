import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_weekly_news():
    prompt = (
        "Donne-moi un résumé structuré des 5 actus de la semaine dans le dev web, la tech et le cloud."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"Erreur OpenAI : {e}")
        return None
