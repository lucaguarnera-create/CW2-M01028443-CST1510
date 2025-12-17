import bcrypt

def hash_password(pwd):
    password_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def validate_password(pwd, hashed):
    password_bytes = pwd.encode('utf-8')
    hashed_bytes = hashed.strip().encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)


def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)
    with open('user.txt', 'a') as f:
        f.write(f"{username},{hashed_password}\n")
    print("User registered successfully.")

def login_user(username, password):
    try:
        with open('user.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if not line.strip():
                    continue
                u_name, hashed = line.strip().split(',', 1)
                u_name = u_name.strip()
                hashed = hashed.strip()
                if u_name == username:
                    return validate_password(password, hashed)
    except FileNotFoundError:
        print("User database not found.")
    return False