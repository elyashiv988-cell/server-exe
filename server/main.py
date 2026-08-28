from file_manager import *
from fastapi import FastAPI, HTTPException, status
import uv
from pydantic import BaseModel

app = FastAPI()

@app.get("/grades/read/")
def get_grades():

    return read_from_data_base()

@app.get("/grades/read/{student_id}")
def get_grades(student_id):
    data = read_from_data_base()
    for student in data:
        if student["id"] == student_id:
            return student

        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} was not found")
                        
class AddStudent(BaseModel):
    id: str
    name: str
    grade: str

@app.post("/grades/add/")
def add_grade(student: AddStudent):
        
    student_data = read_from_data_base()
    for item in student_data:
        if student.id == item["id"]:
            raise HTTPException(status_code=400, detail=f"Student with {student.id} ID is exsits")
    
    new_student = student.model_dump()

    student_data.append(new_student)

    write_to_data_base(student_data)
    
class UpdatingStudent(BaseModel):
    id: str
    name: str | None = None
    grade: str | None = None

@app.put("/grades/update/")
def update_student(updating: UpdatingStudent):

    student_data = read_from_data_base()
    found_id = False

    for student in student_data:
        if student["id"] ==updating.id:
            found_id = True
            if updating.grade:
                student["grade"]= updating.grade
            if updating.name:
                student["name"]= updating.name

    write_to_data_base(student_data)

    if not found_id:
        raise HTTPException(status_code=404, detail=f"Student with {updating.id} ID was not found!")
       
@app.delete("/grades/delete/")
def delete_student(student_id: str | None = None, student_name: str | None = None):
    found_id = False
    found_name = False
    student_data = read_from_data_base()
    for student in student_data:
        if student["id"]==student_id:
            student_data.remove(student)
            found_id = True
            
        if student["name"] == student_name:
            student_data.remove(student)
            found_name = True

    write_to_data_base(student_data)

    if not found_id and not found_name:
        raise HTTPException(status_code=404, detail=f"Student with this value was not found!")

class Creds(BaseModel):
    username: str
    password: str

@app.post("/user/signup/")
def signin_user(creds: Creds):
    data_users = read_users_data()
    for user in data_users:

        if creds.username == user["username"]:
            raise HTTPException(status_code=404, detail=f"Exsits name!")
        
    save_users_to_db(creds.username, creds.password)
   
