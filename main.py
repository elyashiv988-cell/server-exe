from fastapi import FastAPI
import uv
import json

app = FastAPI()

@app.get("/grades/read/")
def get_grades():
    with open("data_grades.json","r") as file:
        data = json.load(file)
        return data

@app.get("/grades/read/{student_id}")
def get_grades(student_id):
    with open("data_grades.json","r") as file:
        data = json.load(file)
        for student in data:
            if student["id"] == student_id:
                return student
        return ("student not found")
    
@app.post("/grades/add/")
def add_grade(id, name, grade):
    with open("data_grades.json","r") as file:
        
        student_data = json.load(file)
    new_student = {'id': id, 'name': name, 'grade': grade}
    student_data.append(new_student)

    with open("data_grades.json","w") as file:

        json.dump(student_data, file, indent=4)

    




