from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    'postgresql+psycopg:///STUDENTS'
)
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))
    
def student_serializer(stud: Students) -> dict:
    return {
        "id": stud.id,
        "first_name": stud.first_name,
        "last_name": stud.last_name,
        "age": stud.age,
        "grade": stud.grade
    }    

to_json = lambda x : [map(student_serializer,x)]


@app.route('/students/', methods=['GET'])
def get_students():
    out = Students.query.all()
    return [{stud.id : student_serializer(stud)} for stud in out]

@app.route('/students/old_students/', methods=['GET'])
def get_students_old():
    out = Students.query.all()#filters and creates list of objects
    return to_json(out) #another way to do below return
    # return jsonify([student_serializer(stud)for stud in old])
    

@app.route('/students/young_students/', methods=['GET'])
def get_students_young():
    out = Students.query.filter(Students.age < 21).all()
    return to_json(out)

@app.route('/students/advance_students/', methods=['GET'])
def get_students_advance():
    out = Students.query.filter(Students.age < 21, Students.grade == 'A').all()
    return to_json(out)

@app.route('/students/student_names/', methods=['GET'])
def get_students_names():
    holder = Students.query.all()
    return [{"first_name" : stud.first_name,"last_name": stud.last_name} for stud in holder] 
     

@app.route('/students/student_ages/', methods=['GET'])
def get_students_ages():
    holder = Students.query.all()
    return [{"student_name" : f'{stud.first_name} {stud.last_name}', "age":stud.age} for stud in holder]

if __name__ == '__main__':
    app.run(debug=True, port=8000)