from bs4 import BeautifulSoup
from googlesearch import search
from summarizer import summarize_text
import requests
import os

def fetch_content(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.text for p in paragraphs if len(p.text) > 50])
        return text[:3000]  # Limit text to avoid long input
    except:
        return ""

def generate_report(query):
    urls = list(search(query, num_results=5))
    raw_text = ""

    for url in urls:
        content = fetch_content(url)
        if content:
            raw_text += f"\n\n---\nSource: {url}\n\n{content}"

    summarized = summarize_text(raw_text)
#    save_as_pdf("reports/report.pdf", summarized)
    return summarized








