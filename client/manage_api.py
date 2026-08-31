from validations import *
import requests
import questionary

def get_base_url():

    return "http://127.0.0.1:8000/"

def check_status_code(response):

    if response.status_code == 200:
        print("Success:", response.status_code, response.json() if response.json() else "")
    else:
        print(f"Error {response.status_code}. {response.json().get("detail")}")
        
def get_all_grades(base_url):

    response = requests.get(f"{base_url}grades/read/")
    data_student = response.json()
   
    print("Success:",response.status_code)
    
    for student in data_student:
        print(student)
    
def get_grade_by_id(base_url):

    username = questionary.text("Enter username:").ask()
    password = questionary.text("Enter password:").ask()
    student_id = questionary.text("Enter ID:", validate=validat_nums_only).ask()
    
    response = requests.get(f"{base_url}grades/read/by_id",params={"student_id": student_id}, json={"username":username,"password": password})

    check_status_code(response)

def add_grade(base_url):

    username = questionary.text("Enter username:").ask()
    password = questionary.text("Enter password:").ask()

    student_id =  questionary.text ("Enter ID:", validate=validat_nums_only).ask()
    name = questionary.text("Enter name:", validate=validat_chars_only).ask()
    grade = questionary.text("Enter grade: ", validate=validat_nums_only).ask()
                   
    response = requests.post(f"{base_url}grades/add/", params={"student_id": student_id, "name": name, "grade": grade}, json={"username":username,"password": password})

    check_status_code(response)

def update_studnt(base_url):

    username = questionary.text("Enter username:").ask()
    password = questionary.text("Enter password:").ask()

    student_id = questionary.text("Enter ID:", validate=validat_nums_only).ask()
    name = None
    grade = None
    ans = questionary.select("",choices=["Update name:", "Update grade:"]).ask()
    if ans == "Update name:":
        name = questionary.text("Enter name:", validate=validat_chars_only).ask()
    elif ans == "Update grade:":
        grade = questionary.text("Enter grade: ", validate=validat_nums_only).ask()

    response = requests.put(f"{base_url}grades/update/",params= {"student_id": student_id, "name": name, "grade": grade}, json={"username": username, "password": password})
        
    

    check_status_code(response)

def delete_student(base_url):

    username = questionary.text("Enter username:").ask()
    password = questionary.text("Enter password:").ask()

    ans = questionary.select("",choices=["Delete by ID","Delete by name"]).ask()
    id_= None
    name = None
    if ans == "Delete by ID":
        id_ = questionary.text("Enter ID:", validate=validat_nums_only).ask()
    elif ans == "Delete by name":
        name = questionary.text("Enter name:", validate=validat_chars_only).ask()
    response = requests.delete(f"{base_url}grades/delete/",params={"student_id":id_, "student_name":name},json={"username": username, "password": password})

    check_status_code(response)

def add_user(base_url):

    username = questionary.text("Enter username:").ask()
    password = questionary.text("Enter password:").ask()
    response = requests.post(f"{base_url}user/signup/",json={"username":username,"password": password})
    check_status_code(response)

    