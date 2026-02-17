import string

alphabet = string.ascii_lowercase 
alphabet1 = string.ascii_uppercase

def encrypt_message(message, key):
    encrypted_word = ""
    for letter in message:
        if letter.islower():
            original_position = alphabet.index(letter)
            encrypted_word += alphabet[(original_position + key) % 26]
            
        elif letter.isupper() :
            original_position = alphabet1.index(letter)
            encrypted_word += alphabet1[(original_position + key) % 26]
                #(Index+Moves)%Total?
        
        else :
            encrypted_word += letter
    print(encrypted_word)

message = input("Please type a message: ")
key = int(input("Enter a shift number please: "))

encrypt_message(message, key)





