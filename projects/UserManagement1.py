import time
import os

class User:
    all_users = []
    def __init__(self, first_name, last_name, email, password, status):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status
        User.all_users.append(self)

    def display_user(self):
        print(f"Fisrt Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Status: {self.status}")
        print("-------------------")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  
    
def create_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    return User(first_name, last_name, email, password, status="Inactive")

new_users = []
while True :
    print("Welcome to user management! ")
    print("Choose an Action: \n1. Add new user\n2. Display all users\n3. Exit\n")
    user_choice = input("Enter your chose: ")
    if user_choice == "1" :
        new_users.append(create_user())
        print("User addded successfully!")
        time.sleep(2)
    elif user_choice == "2":
        clear_screen()
        if new_users :
            print("Display all users ....")
            time.sleep(2)
            for user in new_users:
                user.display_user()
            time.sleep(2)
        else:
            print("Sorry, didn't find any user to display")
            time.sleep(2)
    elif  user_choice == "3":
        print("Exiting ... ")
        break
    else:
        print("Invalide choice! Please try again")
