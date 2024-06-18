from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data
courses = [
    {"id": 1, "name": "Course 1", "description": "Description of Course 1"},
    {"id": 2, "name": "Course 2", "description": "Description of Course 2"},
    {"id": 3, "name": "Course 3", "description": "Description of Course 3"},
]

@app.route('/')
def index():
    return render_template('courses.html', courses=courses)

@app.route('/api/courses')
def get_courses():
    return jsonify(courses)

if __name__ == '__main__':
    app.run(debug=True)
