import requests

def get_base_url():
    return "http://127.0.0.1:8000/grades/"

def get_grade(base_url):

    response = requests.get(f"{base_url}read/")
    grade_data = response.json()
    print(grade_data)

def add_grade(base_url):
    name="nati"
    grade = "80"
    requests.post(f"{base_url}add/", params={name:grade})

def get_grade_by_id(base_url, student_id):

    response = requests.get(f"{base_url}read/{student_id}")
    print(response.json())
    

def display_menu():
    ans = input("Menu:\n(choose num)\n1. Add grade\n2. Remove grage\n3. Edit grade\n4. Show grades\n")
    return ans

def run_app():
    base_url = get_base_url()
    ans = display_menu()
    if ans == "1":
        pass
    elif ans == "2":
        pass
    elif ans == "3":
        pass
    elif ans == "4":
        ans = input("\n1. show all grades. \n2. show grade by ID\n")
        if ans == "1":
            get_grade(base_url)
        elif ans == "2":
            get_grade_by_id(base_url,input("Enter ID student:\n"))

        
run_app()