import random
choice_user = int(input("""Welcome to the Coin Guessing Game!
Choose a methode to toss the coin:
    1. Using random.random()
    2. Using random.randint()
Enter your choice (1 or 2): 
"""))
if choice_user == 1 :
    Guesse_user = input("Enter your Guess (Head or Tails): ").lower()
    Guesse_computer = random.random()
    if Guesse_computer >= 0.5 :
        print("Congratulations! You won")
    else :
        print("Sorry! You faild")
elif choice_user == 2:
    Guesse_user = input("Enter your Guess (Head or Tails): ").lower()
    Guesse_computer = random.randint(0,10)
    if Guesse_computer >= 5 :
        print("Congratulations! You won")
    else :
        print("Sorry! You faild")
else :
    print("Invalide choice! Please try again later.")
