# home.py
from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
@home_bp.route('/home')
def homepage():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
