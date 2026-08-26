from validations import *
import requests
import questionary

def get_base_url():
    return "http://127.0.0.1:8000/grades/"


def get_all_grades(base_url):

    response = requests.get(f"{base_url}read/")
    data_student = response.json()
   
    print("Success:",response.status_code)
    
    for student in data_student:
        print(student)
    
        
def get_grade_by_id(base_url, student_id):

    response = requests.get(f"{base_url}read/{student_id}")

    check_status_code(response)

def add_grade(base_url):
    
    id_ =  questionary.text ("Enter ID:", validate=validat_nums_only).ask()
    name = questionary.text("Enter name:", validate=validat_chars_only).ask()
    grade = questionary.text("Enter grade: ", validate=validat_nums_only).ask()
                   
    response = requests.post(f"{base_url}add/", json={"id": id_, "name": name, "grade": grade})

    check_status_code(response)

def update_studnt(base_url):

    id_ = questionary.text("Enter ID:", validate=validat_nums_only).ask()
    name = None
    grade = None
    ans = questionary.select("",choices=["Update name:", "Update grade:"]).ask()
    if ans == "Update name:":
        name = questionary.text("Enter name:", validate=validat_chars_only).ask()
    elif ans == "Update grade:":
        grade = questionary.text("Enter grade: ", validate=validat_nums_only).ask()

    response = requests.put(f"{base_url}update/", json={"id": id_, "name": name, "grade": grade})

    check_status_code(response)

def delete_student(base_url):

    ans = questionary.select("",choices=["Delete by ID","Delete by name"]).ask()
    id_= None
    name = None
    if ans == "Delete by ID":
        id_ = questionary.text("Enter ID:", validate=validat_nums_only).ask()
    elif ans == "Delete by name":
        name = questionary.text("Enter name:", validate=validat_chars_only).ask()
    response = requests.delete(f"{base_url}delete/",params={"student_id":id_, "student_name":name})

    check_status_code(response)

def check_status_code(response):

    if response.status_code == 200:
        print("Success:", response.status_code,response.json())
    elif response.status_code == 404:
        print(f"Error {response.status_code}. {response.json().get("detail")}")

def display_menu():

    ans = questionary.select("\nGrade manager:",choices=["Add grade","Remove grade","Edit grade","Show grades","Exit"]).ask()
    
    return ans

def run_app(base_url):
    
    while True:
        ans = display_menu()

        if ans == "Add grade":
            add_grade(base_url)

        elif ans == "Remove grade":
            delete_student(base_url)

        elif ans == "Edit grade":
            update_studnt(base_url)

        elif ans == "Show grades":
            ans = questionary.select("",choices=["show all grades","show grade by ID", "Return"]).ask()

            if ans == "show all grades":
                get_all_grades(base_url)

            elif ans == "show grade by ID":
                get_grade_by_id(base_url,questionary.text("Enter ID student:",validate=validat_nums_only).ask())

            elif ans == "Return":
                continue

        elif ans == "Exit":
            break

def main():

    base_url = get_base_url()
    run_app(base_url)

main()