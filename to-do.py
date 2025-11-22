tasks = []

def menu():
    while True:
        print("\n 1. My List \n 2. Add Task \n 3. Delete Task \n 4. Complete Task \n 5. Quit")
        try:
            input_num = int(input("Enter a number: "))

            if input_num == 1:
                if len(tasks) == 0:
                    print("The list is empty.")
                else:
                    for x in tasks:
                        print(x)

            elif input_num == 2: 
                new_task = input("Enter the Task You Want To Add: ")

                for char in new_task:
                    if char.isdigit():
                        print("Enter a string.")
                        break
                else:
                    tasks.append(new_task)
            elif input_num == 3:
                if len(tasks) == 0:
                    print("The list is empty.")
                    continue

                unwanted_task = input("Enter the Task You Want To Delete: ")

                for x in tasks:
                    if unwanted_task not in x:
                        print(f"{unwanted_task} does not exists.")
                        break
                    else:
                        tasks.remove(unwanted_task)

            elif input_num == 4:
                if len(tasks) == 0:
                    print("The list is empty.")
                    continue

                completed_task = input("Enter the Task You Completed:")

                for i in range(len(tasks)):
                    if tasks[i] == completed_task:
                        tasks[i] = tasks[i] + " ✅"
                        print(f"Completed {tasks[i]}")

            elif input_num == 5:

                break
        except ValueError:
            print("You need to enter a valid number (1-4).")
menu()