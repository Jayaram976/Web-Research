from flask import Flask, request, render_template
from research_agent import generate_report
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    report_html = ""
    if request.method == 'POST':
        query = request.form.get('query', '')
        if query:
            report_md = generate_report(query)
            report_html = markdown.markdown(report_md, extensions=['fenced_code', 'tables'])
    return render_template('index.html', report=report_html)

if __name__ == '__main__':
    app.run(debug=True)






