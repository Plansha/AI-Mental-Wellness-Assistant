import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_wellness_advice(user_input):

    prompt = f"""
    You are a helpful mental wellness assistant.

    Give supportive, practical wellness advice.

    User:
    {user_input}

    Keep the response under 150 words.
    """

    response = model.generate_content(prompt)

    return response.text