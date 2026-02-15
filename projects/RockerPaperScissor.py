import random
game = ["Rock", "Paper", "Scissors"]
game1 = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
 """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
 """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

confirm = input("""
Welcome to the Rock, Paper, Scissors game:
      Press Enter to continue or tyow (Help) for the rules help
""").capitalize()

if confirm == "Help" :
    print("""
*************** RULES ***************
1) You choose and the computer chooses
2) Rock smashes Scissors -> Rock wins
3) Scissors cut Paper -> Scissors wins
4) Paper covers Rock -> Paper wins
""")
elif confirm == "" :
    users_choice = input("Enter your choice(rock, paper, scissors): ").capitalize()

    if users_choice in game :
        computers_choice = random.choice(game)

        print("You chose:")
        if users_choice == "Rock" :
            print(f"{game1[0]}")
        elif users_choice == "Paper" :
            print(f"{game1[1]}")
        else: 
            print(f"{game1[2]}")

        print("Computer chose:")
        if computers_choice == "Rock" :
            print(f"{game1[0]}")
        elif computers_choice == "Paper" :
            print(f"{game1[1]}")
        else: 
            print(f"{game1[2]}")

        if users_choice == "Rock" :
            if computers_choice == "Rock" :
                print("You both win")
            elif computers_choice == "Paper" :
                print("You lose! Paper covers Rock")
            else:
                print("You won! Rock smashes Scissors")

        elif users_choice == "Paper" :
            if computers_choice == "Rock" :
                print("You win! Paper covers Rock")
            elif computers_choice == "Paper" :
                print("You both win")
            else:
                print("You lose! Scissors cut Paper")

        else: 
            if computers_choice == "Rock" :
                print("You lose! Rock smashes Scissors")
            elif computers_choice == "Paper" :
                print("You win! Scissors cut Paper")
            else:
                print("You both win")

    else: 
        print("Invalide choice. Please run the program again and choose rock, paper, or scissors. ") 

else: 
    print("Invalide choice. Please type 'Help' or skip by typin 'Enter'. ")