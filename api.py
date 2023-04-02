from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

STUDENT = {
    '1': {'name': 'sushi', 'age': 22, "spec": "math"},
    '2': {'name': 'shubzz', 'age': 30, "spec": "beiology"},
    '3': {'name': 'neha', 'age': 24, "spec": "science"},
    '4': {'name': 'sonal', 'age': 25, "spec": "history"},
}

parser = reqparse.RequestParser()

class StudentList(Resource):
    def get(self):
        return STUDENT

    def post(self):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("spec")
        args = parser.parse_args()
        student_id = int(max(STUDENT.keys())) + 1
        student_id = str(student_id)
        STUDENT[student_id] = {
            "name": args["name"],
            "age": args["age"],
            "spec": args["spec"],
        }
        return STUDENT[student_id], 201

class Student(Resource):
    def get(self, student_id):
        if student_id not in STUDENT:
            return "Not Found", 404
        else:
            return STUDENT[student_id]

    def put(self, student_id):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("spec")
        args = parser.parse_args()
        if student_id not in STUDENT:
            return "Record Not Found", 404
        else:
            student = STUDENT[student_id]
            student['name'] = args['name'] if args['name'] is not None else student['name']
            student['age'] = args['age'] if args['age'] is not None else student['age']
            student['spec'] = args['spec'] if args['spec'] is not None else student['spec']
            return student, 200

    def delete(self, student_id):
        if student_id not in STUDENT:
            return "Record Not Found", 404
        else:
            del STUDENT[student_id]
            return '', 204

api.add_resource(StudentList, '/students/')
api.add_resource(Student, '/students/<student_id>')

if __name__ == '__main__':
    app.run(debug=True)
