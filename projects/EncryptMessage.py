import string
alphabet = string.ascii_lowercase
word = input("Please type a word: ").lower()
encrypted_word = ""

for letter in word:
    for i in range(36) :
        if alphabet[i] == letter :
            break
    encrypted_word += alphabet[i + 2]

print(encrypted_word)


