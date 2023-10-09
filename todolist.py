# Create an empty to-do list
todo_list = []

while True:
    print("To-Do List:")
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")

    print("\nOptions:")
    print("1. Add a new task")
    print("2. Mark a task as done")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        todo_list.append(task)
        print(f"'{task}' added to the to-do list.")
    elif choice == "2":
        if todo_list:
            task_num = int(input("Enter the task number to mark as done: "))
            if 1 <= task_num <= len(todo_list):
                done_task = todo_list.pop(task_num - 1)
                print(f"'{done_task}' marked as done.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks in the to-do list.")
    elif choice == "3":
        if todo_list:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"'{removed_task}' removed from the to-do list.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks in the to-do list.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
