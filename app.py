from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
app = Flask(__name__)
CORS(app)
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["college_management"]
# === STUDENTS ===
@app.route("/api/students", methods=["GET", "POST"])
def handle_students():
    students = db.students
    if request.method == "POST":
        data = request.json
        students.insert_one(data)
        return jsonify({"message": "Student added successfully!"})
    else:
        result = list(students.find({}, {"_id": 0}))
        return jsonify(result)
# === COURSES ===
@app.route("/api/courses", methods=["GET", "POST"])
def handle_courses():
    courses = db.courses
    if request.method == "POST":
        data = request.json
        courses.insert_one(data)
        return jsonify({"message": "Course added successfully!"})
    else:
        result = list(courses.find({}, {"_id": 0}))
        return jsonify(result)

# === FACULTIES ===
@app.route("/api/faculties", methods=["GET", "POST"])
def handle_faculties():
    faculties = db.faculties
    if request.method == "POST":
        data = request.json
        faculties.insert_one(data)
        return jsonify({"message": "Faculty added successfully!"})
    else:
        result = list(faculties.find({}, {"_id": 0}))
        return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)