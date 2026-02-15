import random
names_string = input("""
Welcome to 'whose wallet'
You will give me a list of names, and I will pick a person to pay
If you're ready, enter the names seperated by a comma: 
""")
names = names_string.split(", ")
print(f"Please ask '{names[random.randint(0, len(names)-1)]}' to take this wallet out. Dinner is on him")


import random
names = input("Welcome to 'whose wallet' \nYou will give me a list of names, and I will pick a person to pay \nIf you're ready, enter the names seperated by a comma: ").split(", ")
print(f"Please ask '{random.choice(names)}' to take this wallet out. Dinner is on him")

