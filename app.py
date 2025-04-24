from flask import Flask, request, render_template, send_file
from research_agent import generate_report

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    report = ""
    if request.method == 'POST':
        query = request.form['query']
        report = generate_report(query)
    return render_template('index.html', report=report)

@app.route('/download')
def download():
    return send_file("reports/report.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
