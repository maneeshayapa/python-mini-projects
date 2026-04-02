tasks = []
FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks():
    if not tasks:
        print("\n No tasks in the list.")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    save_tasks()
    print(f"Task '{task}' added!")

def delete_task(): 
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                save_tasks()
                print(f"Task '{removed_task}' deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    load_tasks()
    while True:
        print("\n Todo List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

