import os, time, random

def menu():
  os.system("clear")
  print(20*"*","\tMy Todo List\t", 16*"*", "\n")
  print("Welcome to your to do list. What do you want to do?")
  print("\nAdd\nView\nMove\nEdit\nRemove\nExit\n")
  choice = input("> ").strip().lower()
  print(57*"*", "\n")
  time.sleep(2)
  return choice

def add():
  item = {"name" : "", "date" : "", "priority" : ""}
  item["name"] = input("What is the task? > ").strip()
  item["date"] = input("When is it due by? > ").strip()
  item["priority"] = input("What is the priority? > ").strip().title()
  while item["priority"] != "High" and item["priority"] != "Medium" and item["priority"] != "Low":
    print("\nInvalid priority. Please add the item again and choose\nbetween high, medium or low priority.")
    item["priority"] = input("What is the priority? > ").strip().title()
  return item, item["priority"]

def view(*lists):
  print()
  numberOfLists = len(lists)
  counter = 0
  for list in lists:
    if numberOfLists == 1 and len(list) == 1:
      print("\nYou are currently out of tasks to do.\n")
    if len(list) == 1:
      counter += 1
      if counter == 3:
        print("\nYou are currently out of tasks to do.\n")
      continue
    for item in list:
      if isinstance(item, str):
        continue
      print(f"{item['name']:^25} | {item['date']:^25} | {item['priority']:^25}")
  print()
  if counter < 3:
    return True
  return False

def move(option, priority, *lists):
  removedItem = {}
  for list in lists:
    for item in list:
      if isinstance(item, str):
        continue
      if item["name"] == option:
        removedItem = item
        list.remove(item)
        removedItem["priority"] = priority

  for list in lists:
    if list[0] == removedItem["priority"]:
      list.append(removedItem)
      break

def edit(option, *lists):
  for list in lists:
    for item in list:
      if isinstance(item, str):
        continue
      if item["name"] == option:
        choice = input("Do you want to change the name or the date? > ").strip().title()
        if choice == "Name":
          item["name"] = input("What is the new name? > ")
        elif choice == "Date":
          item["date"] = input("What is the new date? > ")
        else:
          print("Invalid option")
        return

def remove(option, *lists):
  for list in lists:
    for item in list:
      if isinstance(item, str):
        continue
      if item["name"] == option:
        sure = input("Are you sure you want to remove the item? > ").strip().lower()
        if sure == "yes" or sure == "y":
          list.remove(item)
        else:
          print("Item not removed")
        return

#main

#autoload
#if the file exists
files = os.listdir()
if "todoList.txt" in files:
  f = open("todoList.txt", "r")
  todo = eval(f.read())
  highTodo = todo[0]
  mediumTodo = todo[1]
  lowTodo = todo[2]
else:
  highTodo = ["High"]
  mediumTodo = ["Medium"]
  lowTodo = ["Low"]
if "backups" not in files:
  os.mkdir("backups")

choice = ""

while choice != "exit":
  choice = menu()

  if choice == "add":
    item, priority = add()

    if priority == "High":
      highTodo.append(item)
    elif priority == "Medium":
      mediumTodo.append(item)
    elif priority == "Low":
      lowTodo.append(item)

    print("Item added successfully!")

  elif choice == "view":
    priority=""
    option = input("View all or view a specific priority? > ").strip().title()

    if option == "All":
      view(highTodo, mediumTodo, lowTodo)

    elif option == "Priority":
      while priority != "High" and priority != "Medium" and priority != "Low":
        priority = input("Which priority do you want to see? ").strip().title()
        if priority == "High":
          view(highTodo)
        elif priority == "Medium":
          view(mediumTodo)
        elif priority == "Low":
          view(lowTodo)
        else:
          print("Invalid priority. Please type a valid option.")

    else:
      print("Invalid choice")


  elif choice == "move":
    itemExist = view(highTodo, mediumTodo, lowTodo)
    if itemExist:
      option = input("Which item do you want to change the priority? > ")
      priority = input("To which priority? > ").strip().title()
      move(option, priority, highTodo, mediumTodo, lowTodo)
      print("Item moved successifuly")
    else:
      print("No tasks to be moved")

  elif choice == "edit":
    itemExist = view(highTodo, mediumTodo, lowTodo)
    if itemExist:
      option = input("Which item do you want to edit? > ")
      edit(option, highTodo, mediumTodo, lowTodo)
      print("Successfully edited")
    else:
      print("No tasks to be moved")

  elif choice == "remove":
    itemExist = view(highTodo, mediumTodo, lowTodo)
    if itemExist:
      option = input("Which item do you want to remove? > ")
      remove(option, highTodo, mediumTodo, lowTodo)
    else:
      print("No tasks to be removed")    

  elif choice == "exit":
    print("Thank you for using My Todo List\n")
    exit()
    
  else:
    print("Invalid command. Please type one of the given options.\n")

  #autosave
  if choice in ["add", "edit", "remove", "move"]:
    todo = [highTodo, mediumTodo, lowTodo]
    #backup
    backupPath = f"backup{random.randint(0,1000)}.txt"
    backupPath = os.path.join("backups/", backupPath)
    backup = open(backupPath, "w")
    backup.write(str(todo))
    backup.close()

    #saving
    f = open("todoList.txt", "w")
    f.write(str(todo))
    f.close()
  time.sleep(3)
