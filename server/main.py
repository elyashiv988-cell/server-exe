from file_manager import *
from fastapi import FastAPI, HTTPException, status
import uv
from pydantic import BaseModel

app = FastAPI()

class Creds(BaseModel):
    username: str
    password: str


@app.get("/grades/read/")
def get_grades():

    return read_from_data_base()

@app.get("/grades/read/by_id/")
def get_grades_by_id(student_id: str, creds: Creds):

    data_grades = read_from_data_base()
    data_users = read_users_data()

    for user in data_users:

        if creds.username==user["username"] and creds.password == user["password"]:
            if user["type"] == "user" or user["type"] == "manager" or user["type"] == "admin":

                for student in data_grades:
                    if student["id"] == student_id:
                        return student

                raise HTTPException(status_code=404, detail=f"Student with ID {student_id} was not found")
            raise HTTPException(status_code=401, detail=f"Not enough permissions")
        raise HTTPException(status_code=403, detail=f"Incorrect login details")
    


@app.post("/grades/add/")
def add_grade(student_id: str, name: str, grade: str, creds: Creds):
        
    student_data = read_from_data_base()
    data_users = read_users_data()
    
    for user in data_users:

        if creds.username == user["username"] and creds.password == user["password"]:
            if user["type"] == "user" or user["type"] == "manager" or user["type"] == "admin":
                for student in student_data:
                    if student["id"] == student_id:

                        raise HTTPException(status_code=400, detail=f"Student with {student.id} ID is exsits")
                    
                new_student = {"id": student_id, "name": name, "grade": grade}
                student_data.append(new_student)
                write_to_data_base(student_data)
                return
                
            raise HTTPException(status_code=401, detail=f"Not enough permissions")
        
        raise HTTPException(status_code=403, detail=f"Incorrect login details")
            
 
    

@app.put("/grades/update/")
def update_student(creds: Creds, student_id: str, name: str | None = None, grade: str | None = None):

    student_data = read_from_data_base()
    data_users = read_users_data()

    for user in data_users:
        if creds.username == user["username"] and creds.password == user["password"]:
            if user["type"] == "manager" or user["type"] == "admin":

                for student in student_data:
                    if student["id"] == student_id:
                        if grade:
                            student["grade"]= grade
                        if name:
                            student["name"]= name
                    write_to_data_base(student_data)
                    return

                raise HTTPException(status_code=404, detail=f"Student with {student_id} ID was not found!")
            raise HTTPException(status_code=401, detail=f"Not enough permissions")
        raise HTTPException(status_code=403, detail=f"Incorrect login details")
                        
    


@app.delete("/grades/delete/")
def delete_student(creds: Creds, student_id: str | None = None, student_name: str | None = None):
  
    student_data = read_from_data_base()
    data_users = read_users_data()
    
    for user in data_users:
        if user["type"] == "admin":
            if creds.username == user["username"] and creds.password == user["password"]:

                for student in student_data:
                    if student["id"]==student_id or student["name"] == student_name:
                        student_data.remove(student)
                    raise HTTPException(status_code=404, detail=f"Student with this value was not found!")
            raise HTTPException(status_code=403, detail=f"Incorrect login details")
        raise HTTPException(status_code=401, detail=f"Not enough permissions")                            

    write_to_data_base(student_data)


@app.post("/user/signup/")
def adding_user(creds: Creds):
    data_users = read_users_data()
    
    for user in data_users:

        if creds.username == user["username"]:
            raise HTTPException(status_code=403, detail=f"Exsits name!")
        
    save_users_to_db(creds.username, creds.password)
   
