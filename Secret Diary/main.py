from replit import db
import os, time, datetime, random, hashlib

def hashPassword(password, salt):
  hasher = hashlib.sha256()
  passwd = f"{password}{salt}".encode("utf-8")
  hasher.update(passwd)
  hashedPassword = hasher.hexdigest()
  return hashedPassword

def menu():
  print("My Diary")
  option = ""
  while option not in ["1", "2", "3"]:
    option = input("\n1. Create Account\n2. Login\n3. Exit\n> ")
  return option

def createAccount():
  while True:
    user = input("Username: ").strip()
    if user in db:
      print(f"{user} already in use")
      return
    passwd = input("Password: ").strip()
    salt = random.randint(0,99999)
    hashedPassword = hashPassword(passwd, salt)
    db[user] = {"password": hashedPassword, "salt": salt}
    print("User registered successifully")
    break

def login():
  os.system("clear")
  while True:
    user = input("Username: ").strip()
    if user not in db:
      print(f"There is no user called {user} on the system")
      return
    passwd = input("Password: ").strip()
    hashedPassword = hashPassword(passwd, db[user]["salt"])
    if hashedPassword == db[user]["password"]:
      diary(user)
      break
    else:
      print("Invalid password.")
      return

def add(user):
  entry = input("Diary entry: ").strip()
  now = str(datetime.datetime.now())
  db[user][now] = entry
  print("You entry was saved.\n")

def view(user):
  keys = list(db[user].keys())
  keys.remove("password")
  keys.remove("salt")
  keys.sort(reverse=True)

  if len(keys) == 0:
    print("Your diary has no entries.\n")
    return

  n = 0
  while True:
    print(f"Your most recent entry is: {db[user][keys[n]]}\n")
    option = input("Do you want to see an older one[y/n]? ").lower()
    if option == "n":
      break
    n += 1
    if n >= len(keys):
      print("No more entries.\n")
      break
  print("Returning to the menu.")
  time.sleep(3)

def diary(user):
  while True:
    os.system("clear")
    print(f"Welcome to you private dictionary, {user}\n")
    option = input("1. Add\n2. View\n3. Exit\n\nWhat would you like to do? > ").strip()

    time.sleep(2)
    os.system("clear")

    if option == "1": 
      add(user)
    elif option == "2":
      view(user)
    elif option == "3":
      print("Exiting your diary...")
      time.sleep(2)
      break
    else:
      print("Invalid option. Choose another one.\n")
    time.sleep(3)


#main
while True:
  os.system("clear")
  option = menu()
  if option == "1":
    createAccount()
  elif option == "2":
    login()
  elif option == "3":
    exit()
  else:
    print("Invalid command")
  time.sleep(3)
