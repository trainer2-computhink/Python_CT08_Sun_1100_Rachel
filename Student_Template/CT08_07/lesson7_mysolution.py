import os

filepath = os.getcwd()
fullpath = os.path.join(filepath, "tasks.txt")

def create_task_file():
    if os.path.exists(fullpath):
        overwrite = input(f"{filepath} exists. Do you want to overwrite it? y/n: ")
        if overwrite.lower() == "y":
            with open(fullpath, 'w') as file:
                file.write("My Task List")
        else:
            print("File not overwritten.")
    else:
        with open(fullpath, 'w') as file:
            file.write("My Task List")
    return
        

def view_all_tasks():
    with open(fullpath, 'r') as file:
        lines = file.readlines()
        if len(lines) < 2:
            print("No tasks found.")
            return
        for i in range(len(lines)):
            if i == 0:
                print(lines[i].strip())
            else:
                print(f"{i}. {lines[i].strip()}")

def add_new_task():
    print("Enter a new task: ")
    task = input()
    with open(fullpath, 'a') as file:
        file.write("\n" + task)
    print('\nTask added successfully')
    return

def delete_task():
    view_all_tasks()
    task = int(input("Enter the task number to delete: "))
    with open(fullpath, 'r') as file:
        lines = file.readlines()
    if task < 1 or task >= len(lines):
        print("Index chosen out of range")
        return
    lines.pop(task)
    with open(fullpath, 'w') as file:
        file.writelines(lines)
    print("Task deleted successfully!")
    return

def mark_task_done():
    view_all_tasks()
    task = int(input("Enter the task number to be mark as done: "))
    with open(fullpath, 'r') as file:
        lines = file.readlines()
    if task < 1 or task >= len(lines):
        print("Index chosen out of range")
        return
    lines[task] = lines[task].strip() + " (Done)\n"
    with open(fullpath, 'w') as file:
        file.writelines(lines)
    print("Task marked as done!")
    return

def display_menu():
    print("Menu:")
    print("1. Create a new task file")
    print("2. View all tasks")
    print("3. Add a new task")
    print("4. Delete a task")
    print("5. Mark a task as done")
    print("6. Exit")
    print("\nEnter your choice:")
    return

while True:
    display_menu()
    choice = input()
    if choice == '1':
        create_task_file()
    elif choice == '2':
        view_all_tasks()
    elif choice == '3':
        add_new_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        mark_task_done()
    elif choice == '6':
        break
    else:
        print("Enter a valid input from 1-6")