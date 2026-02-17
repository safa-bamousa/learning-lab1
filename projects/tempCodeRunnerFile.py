import random
words=["good", "boy", "girl", "september" ]
guesse_word = random.choice(words)
word = "_" * len(guesse_word)
print("".join(word))