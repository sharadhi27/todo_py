

tasks = []

def show_tasks():
    if not tasks:
        print("\n No tasks yet.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def main():
    while True:
        print("\n--- TO-DO APP ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else
            print("Invalid choice, try again.")

main()
