from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the About page
@app.route('/about')
def about():
    return render_template('About.html')

# Route for the Services page
@app.route('/services')
def services():
    return render_template('Services.html')

# Route for the Contact page
@app.route('/contact')
def contact():
    return render_template('Contact.html')

# Route to start the Streamlit app

@app.route('/streamlit')
def run_streamlit():
    subprocess.Popen(["streamlit", "run", "main.py"])
    return redirect("http://localhost:8501")

if __name__ == "_main_":
    app.run(debug=True)