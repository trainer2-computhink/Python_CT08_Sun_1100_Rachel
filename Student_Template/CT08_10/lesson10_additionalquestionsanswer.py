import random

def create_new_user(user_db, role_db):
    username = input("Enter a username: ")
    if not username:
        print("Invalid username")
        return user_db, role_db
    elif username in user_db:
        print("Username exists")
        return user_db, role_db

    role = input("Enter role (admin/user): ").lower()
    if role not in ["admin", "user"]:
        print("Invalid role. Defaulting to 'user'.")
        role = "user"

    password = generate_password()
    user_db[username] = password
    role_db[username] = role

    print(f"User created. Username: {username}, Password: {password}, Role: {role}")
    return user_db, role_db

def generate_password():
    password = ""
    for _ in range(12):
        char_type = random.choice(['upper', 'lower', 'numbers', 'symbols'])
        if char_type == "upper":
            password += chr(random.randint(65, 90))
        if char_type == "lower":
            password += chr(random.randint(97, 122))
        if char_type == "numbers":
            password += chr(random.randint(48, 57))
        if char_type == "symbols":
            password += chr(random.randint(33, 47))
    return password

def update_password(user_db):
    username = input("Enter your username: ")
    if username not in user_db:
        print("User does not exist")
        return user_db
    password = input("Enter your current password: ")
    if password != user_db[username]:
        print("Incorrect password")
        return user_db
    new_password = generate_password()
    user_db[username] = new_password
    print(f"Password updated. Your new password is: {new_password}")
    return user_db

def login(user_db, attempts_db):
    username = input("Enter your username: ")

    if username not in user_db:
        print("User not found")
        return False

    if attempts_db.get(username, 0) >= 3:
        print("Account locked. Too many failed attempts.")
        return False

    password = input("Enter your password: ")

    if password != user_db[username]:
        print("Password invalid")
        attempts_db[username] = attempts_db.get(username, 0) + 1
        print(f"Attempts: {attempts_db[username]}/3")
        return False

    attempts_db[username] = 0
    print(f"Login successful. Welcome {username}.")
    return True

def admin_view_users(user_db, role_db, current_user):
    if current_user not in role_db:
        print("User not found")
        return

    if role_db[current_user] != "admin":
        print("Access Denied")
        return

    print("Usernames and passwords:")
    for user, pw in user_db.items():
        print(f"{user}: {pw}")

def view_user_data(user_db):
    print("Usernames and passwords:")
    for user, pw in user_db.items():
        masked_pw = "*" * len(pw)
        print(f"{user}: {masked_pw}")

def view_menu():
    print("Username and Password Manager")
    print("1. Create a new user")
    print("2. Update password")
    print("3. Login")
    print("4. View stored usernames and passwords")
    print("5. Admin view users")
    print("6. Exit")

user_db = {}
attempts_db = {}
role_db = {}
current_user = None

while True:
    view_menu()
    choice = int(input())

    if choice == 1:
        create_new_user(user_db, role_db)

    elif choice == 2:
        update_password(user_db)

    elif choice == 3:
        if login(user_db, attempts_db):
            current_user = input("Re-enter username to confirm session: ")

    elif choice == 4:
        view_user_data(user_db)

    elif choice == 5:
        if current_user:
            admin_view_users(user_db, role_db, current_user)
        else:
            print("Please login first")

    elif choice == 6:
        break

    else:
        print("Please choose a valid action")

    print("\n")