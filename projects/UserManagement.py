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
    
def create_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    return User(first_name, last_name, email, password, status="Inactive")

print("Welcome to user management! ")
user_choice = 0
while user_choice != 3 :
    user_choice = int(input("Choose an Action: \n1. Add new user\n2. Display all users\n3. Exit\nEnter your chose: "))
    if user_choice == 1 :
        new_user = create_user()
        print("User addded successfully!")
    elif user_choice == 2:
        for user in User.all_users:
            user.display_user()
    elif  user_choice == 3:
        print("See you again! ")
        continue
    else:
        print("Invalide choice!")
