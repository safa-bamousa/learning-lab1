OnGoingTasks = []
DoneTasks = []
tasks =[]
Tasks = input("Enter your tasks for today seperated by a comma: ").split(", ")
for task in Tasks:
    print(task)
for task in Tasks :
    print("\n",task,"\n")
    confirm = input(f"Did you finish {task} already?\n").lower()
    if confirm == "yes" :
        print("Nice job!")
        OnGoingTasks.append(task)
        DoneTasks.append(task)
    else:
        print("Try not to put it off")
    print("\n------------\n")
confirm = input("Do you want to see your today's progress? (yes, no)").lower()
if confirm == "yes" :
    print("******** Done Tasks ********")
    print(DoneTasks)
    print("******** OnGoing Tasks ********")
    print(OnGoingTasks)
