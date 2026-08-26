import json

def write_to_data_base(data):

    with open("data_grades.json","w") as file:
    
        json.dump(data, file, indent=4)

def read_from_data_base():

    with open("data_grades.json","r") as file:
        
        return json.load(file)
