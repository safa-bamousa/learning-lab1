import string
alphabet = string.ascii_lowercase 
word = input("Please type a word: ").lower()
encrypted_word = ""

for letter in word:
    if letter not in alphabet :
        encrypted_word += letter
    else:
        original_position = alphabet.index(letter)
        encrypted_word += alphabet[(original_position + 2) % 26]
        #(Index+Moves)%Total?

print(encrypted_word)


