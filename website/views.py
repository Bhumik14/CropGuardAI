from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if not current_user.is_authenticated:  # Check if the user is not authenticated
        return redirect(url_for('auth.login'))  # Redirect to login page
    return render_template("index.html", user=current_user)  # Serve index.html for authenticated users

@views.route('/about')
@login_required
def about():
    return render_template("About.html", user=current_user)

@views.route('/services')
@login_required
def services():
    return render_template("Services.html", user=current_user)

@views.route('/contact')
@login_required
def contact():
    return render_template("Contact.html", user=current_user)
