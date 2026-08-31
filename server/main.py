from file_manager import read_from_data_base, read_users_data, write_to_data_base, save_users_to_db
from fastapi import FastAPI, HTTPException
from hashing import hash_password
from authenticate import authenticate
from models import Creds

app = FastAPI()

@app.get("/grades/read/")
def get_grades():

    return read_from_data_base()


@app.get("/grades/read/by_id/")
def get_grades_by_id(student_id: str, creds: Creds):

    data_grades = read_from_data_base()
    data_users = read_users_data()

    user = authenticate(creds, data_users, ["guest", "user", "manager", "admin"])

    for student in data_grades:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail=f"Student with {student_id} ID was not found!")

@app.post("/grades/add/")
def add_grade(student_id: str, name: str, grade: str, creds: Creds):
        
    student_data = read_from_data_base()
    data_users = read_users_data()

    user = authenticate(creds, data_users, ["user", "manager", "admin"])

    for student in student_data:
        if student["id"] == student_id:

            raise HTTPException(status_code=400, detail=f"Student with {student_id} ID is exsits")
                    
    new_student = {"id": student_id, "name": name, "grade": grade}
    student_data.append(new_student)
    write_to_data_base(student_data)


@app.put("/grades/update/")
def update_student(creds: Creds, student_id: str, name: str | None = None, grade: str | None = None):

    student_data = read_from_data_base()
    data_users = read_users_data()

    user = authenticate(creds, data_users, ["manager", "admin"])

    for student in student_data:
        if student["id"] == student_id:
            if grade:
                student["grade"] = grade
            if name:
                student["name"] = name
            write_to_data_base(student_data)
            return

    raise HTTPException(status_code=404, detail=f"Student with {student_id} ID was not found!")
 

@app.delete("/grades/delete/")
def delete_student(creds: Creds, student_id: str | None = None, student_name: str | None = None):
  
    student_data = read_from_data_base()
    data_users = read_users_data()
    
    user = authenticate(creds, data_users, ["admin"])

    for student in student_data:
        if student["id"]==student_id or student["name"] == student_name:
            student_data.remove(student)
            write_to_data_base(student_data)
            return

    raise HTTPException(status_code=404, detail=f"Student with this value was not found!")


@app.post("/user/signup/")
def adding_user(creds: Creds):
    
    data_users = read_users_data()
    user_id = len(data_users)+1
    user_type = "guest"
    

    for user in data_users:

        if creds.username == user["username"]:
            raise HTTPException(status_code=403, detail=f"Exsits name!")
        
    save_users_to_db(user_id, creds.username, hash_password(creds.password), user_type)
   
