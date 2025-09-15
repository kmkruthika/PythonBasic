#to do list simple
tasks=[]
done_tasks=[]

while True:
  print("\n1. Add Tasks")
  print("2.View Tasks")
  print("3.Exit")
  print("4.Delete task")
  print("5.Mark task as done")

  choice=input("Enter the choice")

  if choice=='1':
    task=input("enter the task:")
    tasks.append(task)
    print("Task added")
  elif choice=='2':
    print("your tasks:")
    for i,task in enumerate(tasks,1):
      print(f'{i}.{task}')
    print("Compelted tasks")
    for i,task in enumerate(tasks,1):
      print(f'{i}.{done_tasks}')
  elif choice=='3':
    print("Bye!")
    break
  elif choice=='4':
    num=int(input("enter the task to be deleted"))
    tasks.pop(num-1)
  elif choice=='5':
    print("completed(Mark as done)")
    num=int(input("Enter the tasks finished:"))
    done=tasks.pop(num-1)
    done_tasks.append(done)
    print(f"Marked {done} ✔")
  else:
    print("Invalid choice1")
