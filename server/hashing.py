import bcrypt

def hash_password(password):

    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)

    return hashed.decode('utf-8')

def verify_password(user_password, stored_hash):
    password_bytes = user_password.encode('utf-8')
    stored_hash_bytes = stored_hash.encode('utf-8')
 
    return bcrypt.checkpw(password_bytes, stored_hash_bytes)

