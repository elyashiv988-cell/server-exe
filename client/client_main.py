from validations import *
import requests
import questionary
from manage_api import *


def display_menu():

    ans = questionary.select("\nGrade manager:",choices=["Add grade","Remove grade","Edit grade","Show grades","Sign up","Exit"]).ask()
    
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
        elif ans == "Sign up":

            add_user(base_url)

        elif ans == "Exit":
            break


def main():

    base_url = get_base_url()
    run_app(base_url)

main()

