import json
import csv 

db_users = '/Users/elyashiv/kodcode/projects/server-exe/server/db users/data_users.csv'
db_grades = '/Users/elyashiv/kodcode/projects/server-exe/server/db grades/data_grades.json'

def write_to_data_base(data):

    with open(db_grades,"w") as file:
    
        json.dump(data, file, indent=4)

def read_from_data_base():

    with open(db_grades,"r") as file:
        
        return json.load(file)
    
import csv

def read_users_data():
    
    with open(db_users, newline='') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def save_users_to_db(username, password):
    user = {"id": None, "username": username, "password": password, "type": "user"}
    data = read_users_data()
    data.append(user)

    fieldnames = user.keys()

    with open(db_users, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

