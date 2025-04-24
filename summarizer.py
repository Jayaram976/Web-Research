# summarizer.py

#AIzaSyDQ6FqWzYYUo2umEG6t2-VC4z1yDGM3TD4

import google.generativeai as genai

genai.configure(api_key="AIzaSyDQ6FqWzYYUo2umEG6t2-VC4z1yDGM3TD4")

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def summarize_text(text):
    prompt = "Summarize the following web content into a clean research report with clear structure and sources:\n\n" + text
    response = model.generate_content(prompt)
    return response.text
