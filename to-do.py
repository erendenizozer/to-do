tasks = []

def menu():
    while True:
        print("\n 1. My List \n 2. Add Task \n 3. Delete Task \n 4. Complete Task \n 5. Quit")
        input_num = int(input("Enter a number: "))
        if input_num == 1:
            for x in tasks:
                print(x)
        elif input_num == 2:
            new_task = input("Enter the Task You Want To Add: ")
            tasks.append(new_task)
        elif input_num == 3:
            unwanted_task = input("Enter the Task You Want To Delete: ")
            tasks.remove(unwanted_task)
        elif input_num == 4:
            completed_task = input("Enter the Task You Completed:")
            for i in range(len(tasks)):
                if tasks[i] == completed_task:
                    tasks[i] = tasks[i] + " ✅"
                    print(f"Completed {tasks[i]}")
        elif input_num == 5:
            break
menu()