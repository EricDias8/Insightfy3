from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary_and_save(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Analise o texto: {text}"}
        ]
    )
    result = response.choices[0].message.content
    return {
        "summary": result,
        "category": "Tipo do texto",
        "label": "Código criativo",
    }
