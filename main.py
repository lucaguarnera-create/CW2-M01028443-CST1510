import sqlite3

conn = sqlite3.connect("my_database.db")  # Make sure the path is correct
cursor = conn.cursor()

from login import register_user, login_user
def create_account(conn, username, password_hash):
    from app.users import add_user
    add_user(conn, username, password_hash)

def menu():
    print("\n--- Menu ---")
    print("1. Register User")
    print("2. Login User")
    print("3. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            username = input("Enter username for login: ")
            password = input("Enter password for login: ")
            if login_user(username, password):
                print("Login successful!")
            else:
                print("Login failed.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


