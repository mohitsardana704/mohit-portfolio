from flask import Flask, render_template, request, send_from_directory
from datetime import datetime
import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets Connection

import os
import json

scope = [
"https://spreadsheets.google.com/feeds",
"https://www.googleapis.com/auth/drive"
]

if os.path.exists("portfolio-leads-123.json"):

 creds = ServiceAccountCredentials.from_json_keyfile_name(
    "portfolio-leads-123.json",
    scope
 )

else:

 google_creds = json.loads(
    os.environ.get("GOOGLE_CREDS")
 )

 creds = ServiceAccountCredentials.from_json_keyfile_dict(
    google_creds,
    scope
)

client = gspread.authorize(creds)

sheet = client.open("Resume Leads").sheet1


# Home Page

@app.route('/')
def home():
    return render_template('index.html')

# About Page

@app.route('/about')
def about():
    return render_template('about.html')

# Experience Page

@app.route('/experience')
def experience():
    return render_template('experience.html')

# Skills Page

@app.route('/skills')
def skills():
    return render_template('skills.html')

# Projects Page

@app.route('/projects')
def projects():
    return render_template('projects.html')

# Contact Page

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Resume Download + Lead Capture

@app.route('/download-resume', methods=['POST'])
def download_resume():

    name = request.form.get('name')
    email = request.form.get('email')
    company = request.form.get('company')

    sheet.append_row([
    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    name,
    email,
    company
    ])
    print("Lead saved")
    return send_from_directory(
    'static/resume',
    'Mohit_Sardana_Resume.pdf',
    as_attachment=True
)

# Run App

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)