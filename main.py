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
    
@app.post(f"/grades/add/")
def add_grade(name, grade):
    with open("data_grades.json","w") as file:
        new = {name: grade}
        json.dump(new, file)
    




