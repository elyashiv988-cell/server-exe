# Grade Manager

Simple API project for managing student grades.
Built with FastAPI (server) and a CLI client (using questionary).

## What it does

- Show all grades
- Show grade by student ID
- Add a new grade
- Edit a grade
- Delete a grade
- Sign up a new user

## Files

- main.py - the API server (FastAPI)
- file_manager.py - reads and writes the data files (json/csv)
- authenticate.py - checks username/password and permissions
- hashing.py - hashes and checks passwords (bcrypt)
- models.py - data models (Creds)
- client.py - the CLI app the user runs
- manage_api.py - functions that call the API from the client
- validations.py - input validation for the CLI

## How to run

1. Install the requirements:

```
pip install -r req.txt
```

2. Run the server:

```
uvicorn main:app --reload
```

3. In another terminal, run the client:

```
python client.py
```

## Users and permissions

There are 4 user types: guest, user, manager, admin.

- guest / user - can view grades
- manager - can view and edit grades
- admin - can view, edit, and delete grades

New users sign up as "guest" by default.

## Notes

- Data is stored in local files (csv for users, json for grades).
- Passwords are hashed with bcrypt before saving.
