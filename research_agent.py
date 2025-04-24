from bs4 import BeautifulSoup
from googlesearch import search
from summarizer import summarize_text
import requests
from fpdf import FPDF
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
    save_as_pdf("reports/report.pdf", summarized)
    return summarized

#def save_as_pdf(filepath, text):
    # Ensure the directory exists
#    os.makedirs(os.path.dirname(filepath), exist_ok=True)

#    pdf = FPDF()
#    pdf.set_auto_page_break(auto=True, margin=15)
#    pdf.add_page()
#    pdf.set_font("Arial", size=12)

#    max_width = 180  # Width limit for the cell

#    for line in text.split("\n"):
#        words = line.split(' ')
#        current_line = ""
#        for word in words:
#            if pdf.get_string_width(current_line + word + ' ') > max_width:
#                pdf.multi_cell(0, 10, current_line.strip())
#                current_line = word + ' '
#            else:
#                current_line += word + ' '
#        if current_line.strip():  # print remaining
#            pdf.multi_cell(0, 10, current_line.strip())

#    pdf.output(filepath)


#from fpdf import FPDF
#import os

#def save_as_pdf(filepath, text):
    # Ensure the directory exist
#    os.makedirs(os.path.dirname(filepath), exist_ok=True)

#    pdf = FPDF()
#    pdf.set_auto_page_break(auto=True, margin=15)
#    pdf.add_page()

    # Add a Unicode-compatible font (DejaVu Sans or any TTF font you like)
#    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
#    pdf.set_font('DejaVu', size=10)

    # Maximum width for the line to avoid overflow
#    max_width = 180  # Adjust this as needed for your page

    # Split the text into lines, then process each line
#    for line in text.split("\n"):
        # Use multi_cell to handle word wrapping automatically
#        pdf.multi_cell(max_width, 10, line)

    # Output the PDF to the specified file
#
#    pdf.output(filepath)


def save_as_pdf(filepath, text):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # ✅ Correct font path
    font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'DejaVuSans.ttf')
    pdf.add_font('DejaVu', '', font_path, uni=True)
    pdf.set_font('DejaVu', size=10)

    max_width = 180

    for line in text.split("\n"):
        pdf.multi_cell(max_width, 10, line)

    pdf.output(filepath)






