import random

with open ("c:/Users/safab/learning-lab1/projects/words.txt","r") as file:
    words = file.read().splitlines()

#C:\Users\safab\learning-lab1\projects
guesse_word = random.choice(words)