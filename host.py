# main.py
from flask import Flask
#from app import login_bp
from home import home_bp
from courses import course_bp

app = Flask(__name__)

# Register blueprints
#app.register_blueprint(login_bp)
app.register_blueprint(home_bp)
app.register_blueprint(course_bp)

if __name__ == '__main__':
    app.run(debug=True)
