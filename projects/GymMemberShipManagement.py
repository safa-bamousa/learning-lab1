import time
import os

class Member:
    def __init__(self, first_name, last_name, membership_id, membership_status):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_id = membership_id
        self.membership_status = membership_status

    def display_member(self):
        print(f"First name: {self.first_name}")   
        print(f"Last name: {self.last_name}")  
        print(f"Membership ID: {self.membership_id}")  
        print(f"Membership status: {self.membership_status}")  
        print("_" * 20 ) 

all_members = []

def create_member():
    first_name = input("Enter first name: ").capitalize()
    last_name = input("Enter last name: ").capitalize()
    membership_id = int(input("Enter membership id: "))
    membership_status = input("Enter membership status, Or click enter: ").strip().capitalize()
    if not membership_status :
        membership_status = "Inactive"
    return Member(first_name, last_name, membership_id, membership_status)

def clear_screen():
   os.system("cls" if os.name == "nt" else "clear")

def search_member(attribute, value):
    found = False
    for member in all_members :
        if getattr(member, attribute) == value:
            member.display_member()
            found = True
    if not found :
        print("Sorry, no member found! ")


# def search_member_by_id(member_id):
#     members_found = []
#     for member in all_members :
#         if member.membership_id == member_id :
#             members_found.append(member) 
#     if members_found :
#         for member in members_found :
#             member.display_member()
#     else:
#         print("Sorry we didn't found any one!")

# def search_member_by_name(name):
#     members_found = []
#     for member in all_members :
#         if member.first_name == name :
#             members_found.append(member) 
#     if members_found :
#         for member in members_found :
#             member.display_member()
#     else:
#         print("Sorry we didn't found any one!")

# def search_member_by_status(status):
#     members_found = []
#     for member in all_members :
#         if member.membership_status == status :
#             members_found.append(member) 
#     if members_found :
#         for member in members_found :
#             member.display_member()
#     else:
#         print("Sorry we didn't found any one!")

while True :
    print("Welcome to Gym Membership Management ")
    print("\nChoose an Action :")
    print("1. Add new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("4. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1" :
        all_members.append(create_member())
        print("Member added successfly!")
        time.sleep(2)
        clear_screen()
    elif choice == "2" :
        if all_members :
            for member in all_members :
                member.display_member()
        else:
            print("Sorry we didn't found any one!")
    elif choice == "3" :
        clear_screen()
        print("Search by: ")
        print("1. Membership ID")
        print("2. first name")
        print("3. Membership Status")
        search_by = input("\nEnter your choice: ")
        if search_by == "1" :
            member_id = int(input("Enter the id to search for:"))
            search_member("membership_id", member_id)
        elif search_by == "2" :
            name = input("Enter the name to search for:").capitalize()
            search_member("first_name", name)
        elif search_by == "3" :
            status = input("Enter the status to search for:").capitalize()
            search_member("membership_status", status)
        else:
            print("Invalid choice!")
            time.sleep(2)
            # continue
    elif choice == "4" :
        print("Exiting ....")
        time.sleep(2)
        break
    else :
        print("Invalid choice! Please try again!")
