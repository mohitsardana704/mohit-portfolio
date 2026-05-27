from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html' , current_path=request.path)


# About Page
@app.route('/about')
def about():
    return render_template('about.html' , current_path=request.path)


# Experience Page
@app.route('/experience')
def experience():
    return render_template('experience.html' , current_path=request.path)


# Skills Page
@app.route('/skills')
def skills():
    return render_template('skills.html' , current_path=request.path)


# Projects Page
@app.route('/projects')
def projects():
    return render_template('projects.html' , current_path=request.path)


# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html' , current_path=request.path)


# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)