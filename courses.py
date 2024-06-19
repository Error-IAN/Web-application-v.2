from flask import Flask, render_template, jsonify, Blueprint

app = Flask(__name__)

# Sample data
courses_data = [
    {"id": 1, "name": "Course 1", "description": "Description of Course 1"},
    {"id": 2, "name": "Course 2", "description": "Description of Course 2"},
    {"id": 3, "name": "Course 3", "description": "Description of Course 3"},
]

# Define the course blueprint
course_bp = Blueprint('course', __name__)

@course_bp.route('/courses')
def courses():
    return render_template('courses.html', courses=courses_data)

# Register the blueprint with the main Flask app
app.register_blueprint(course_bp)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/api/courses')
def get_courses():
    return jsonify(courses_data)

if __name__ == '__main__':
    app.run(debug=True)
