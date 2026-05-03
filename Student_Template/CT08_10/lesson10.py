import random

def generate_password():
    password = ""
    for _ in range(12):
        character_pool = random.choice(['upper', 'lower', 'digit', 'symbols'])
        if character_pool == 'upper':
            password += chr(random.randint(65, 90))
        elif character_pool == 'lower':
            password += chr(random.randint(97, 122))
        elif character_pool == 'digit':
            password += chr(random.randint(48, 57))
        else:
            password += chr(random.randint(33, 47))
    return password

user_db = {}
def create_new_user(user_db):
    username = input("Enter a username: ")
    if not username or username in user_db:
        print("Invalid username")
        return user_db
    password = generate_password()
    user_db[username] = password
    print(f"Username created: {username}")
    print(f"Your password: {password}")

create_new_user(user_db)

def update_password(user_db):
    username = input("Enter your username: ")
    if not username in user_db:
        print("Invalid username")
        return user_db
    password = input("Enter your password: ")
    if password != user_db[username]:
        print("Invalid password")
        return user_db
    new_password = generate_password()
    user_db[username] = new_password
    print(f"{username} updated")
    print(f"Your new password is: {new_password}")
    return user_db

update_password(user_db)