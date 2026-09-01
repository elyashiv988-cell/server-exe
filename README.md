# Grade Manager

Simple API project for managing student grades.

## Project structure

client/

    client.py       - the CLI app the user runs. 

    manage_api.py   - functions that call the API from the client. 

    validations.py  - input validation. 

    req.txt         - client dependencies. 

server/

    main.py         - the API server (FastAPI). 

    file_manager.py - reads and writes the data files (json/csv). 

    authenticate.py - checks username/password and permissions. 

    hashing.py      - hashes and checks passwords (bcrypt). 

    models.py       - data models (Creds). 

    req.txt         - server dependencies. 

    db grades/

        data_grades.json. 

    db users/

        data_users.csv. 


## How to run

Run in Bash:

### 1. Set up the server

cd server
pip install -r req.txt
uvicorn main:app --reload

Keep this terminal open, the server needs to keep running.

### 2. Set up the client

Open a new terminal:

cd client
pip install -r req.txt
python client.py

## Users and permissions

There are 4 user types: guest, user, manager, admin.

- guest - can view all grades
- user - can also view grades by ID
- manager - can also edit grades
- admin - can also delete grades

New users sign up as "guest" by default. To test manager/admin features, edit server/db users/data_users.csv directly and change the "type" field for a user.

## Notes

- Data is stored in local files (csv for users, json for grades).
- Passwords are hashed with bcrypt before saving.