# summarizer.py

#AIzaSyDQ6FqWzYYUo2umEG6t2-VC4z1yDGM3TD4


from dotenv import load_dotenv
import google.generativeai as genai
import os


load_dotenv()  # Load values from .env

api_key = os.getenv("GEMINI_API_KEY")  # This is now your real key


genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def summarize_text(text):
    prompt = "Summarize the following web content into a clean research report with clear structure and sources:\n\n" + text
    response = model.generate_content(prompt)
    return response.text
