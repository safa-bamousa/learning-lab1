import random
words=["good", "boy", "girl", "september" ]
guesse_word = random.choice(words)
word = ["_"] * len(guesse_word)
# print("".join(word))
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
tentatives = 6 #the total number of tentatives
print("Wlecome to HangMan game, you have 6 tentative to win. Good luck!")
while tentatives > 0  and "".join(word) != guesse_word:
    guesse_letter = input("Enter a guesse letter please: ").lower()
    if guesse_letter not in guesse_word :
        tentatives = tentatives - 1
        print(f"Result: {"".join(word)}")
        print(HANGMANPICS[6-tentatives])
        print(f"You have another {tentatives} tentatives" )
    else:
        i = 0
        for letter in guesse_word :
            if letter == guesse_letter :
                word[i] = letter
            i += 1
        print(f"Result: {"".join(word)}")

if tentatives == 0 :
    print("Sorry you lost! Try again letter")
else:
    print("Congratulation! You won!")