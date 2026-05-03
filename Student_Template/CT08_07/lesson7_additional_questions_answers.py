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

    tasks = lines[1:]

    priority_order = {
        "HIGH": 3,
        "MEDIUM": 2,
        "LOW": 1
    }

    def get_priority(line):
        if "[HIGH]" in line:
            return priority_order["HIGH"]
        elif "[MEDIUM]" in line:
            return priority_order["MEDIUM"]
        elif "[LOW]" in line:
            return priority_order["LOW"]
        return 0
    
    tasks_sorted = sorted(tasks, key=get_priority, reverse=True)

    print(lines[0].strip())

    for i in range(len(tasks_sorted)):
        print(f"{i + 1}. {tasks_sorted[i].strip()}")

def add_new_task():
    task = input("Enter a new task: ")
    priority = input("Enter priority (low/medium/high): ").lower()

    if priority not in ["low", "medium", "high"]:
        print("Invalid priority. Add task with valid priority again")
        return

    task_line = f"{task} [{priority.upper()}]"

    with open(fullpath, 'a') as file:
        file.write("\n" + task_line)

    print("Task added successfully.")

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

def toggle_task_done():
    view_all_tasks()
    task = int(input("Enter the task number to toggle done: "))
    
    with open(fullpath, 'r') as file:
        lines = file.readlines()

    if task < 1 or task >= len(lines):
        print("Index chosen out of range")
        return

    line = lines[task].strip()

    if "(Done)" in line:
        line = line.replace(" (Done)", "")
        print("Task marked as undone!")
    else:
        line = line + " (Done)"
        print("Task marked as done!")

    lines[task] = line + "\n"

    with open(fullpath, 'w') as file:
        file.writelines(lines)

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
        toggle_task_done()
    elif choice == '6':
        break
    else:
        print("Enter a valid input from 1-6")