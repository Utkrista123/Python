tasks = []
while True:
    command = input("Enter a command (add/remove/display/exit): ").strip().lower()
    if command == "add":
        task = input("Enter a task: ")
        tasks.append(task)
        print(f"The Task {task} sucessfully added.")
    elif command == "remove":
        if tasks == []:
            print("Their is no task to remove.")
        else:
            task = input("Enter the task you want to remove: ")
            tasks.remove(task)
            print(f"The Task {task} sucessfully removed.")
    elif command == "display":
        if tasks == []:
            print("Their is no task to display.")
        else:
            for idx, task in enumerate(tasks, start = 1):
                print(f"Task {idx}: {task}")
    elif command == "exit":
        print("Exiting the list.")
        break
    else:
        print(f"Sorry the '{command}' is not a valid command.")

