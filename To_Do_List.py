tasks = []

def show_menu():
    print("\n TO DO LIST ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    
while True:
    show_menu()
    choice = (input("Enter the choice from(1-4):"))
    
    if choice == '1':
        task = input("Enter the task:")
        tasks.append(task)
        print("task added")

    elif choice == '2':
        if not tasks:
            print("Nothing is their")
        else:
            print("View the choice")
            for i,task in enumerate(tasks, start = 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("Nothing is their")
        else:
            for i,task in enumerate(tasks, start = 1):
                print(f"{i}. {task}")

            num = int(input("Enter the choice:"))
            if 1 <= num <= len(tasks):
                num_task = input("udpate the task:")
                tasks[num -1] = num_task
                print("Successfull updated")
            else:
                print("Invalid!")
    
    elif choice == '4':
        if not tasks:
            print("Nothing is their")
        else:
            for i,task in enumerate(tasks, start = 1):
                print(f"{i}. {task}")
                
            num = int(input("Enter the choice:"))
            if 1 <= num <= len(tasks):
                remove = tasks.pop(num-1)
                print("Deleted successfully")
            else:
                print("Invalid")
    else:
        print("Try again!")   
