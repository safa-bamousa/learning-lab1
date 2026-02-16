import random
import string

print("Welcom to the Password Generator!")
nbr_total = int(input("Enter the total number of charachters in the password: "))
nbr_letters = int(input("Enter the number of letters in the password: "))
nbr_numbers = int(input("Enter the number of nnumbers in the password: "))
nbr_symbols = int(input("Enter the number of symbols in the password: "))
if nbr_total != nbr_letters + nbr_numbers + nbr_symbols :
    print("Invalid input. The sum of letters, numbers and symbols doesn't match the password!")
else: 
    random_letters = random.choices(string.ascii_letters , k= nbr_letters)
    random_numbers = random.choices(string.digits , k= nbr_numbers)
    random_symbols = random.choices(string.punctuation , k= nbr_symbols)
    random_password = random_letters + random_numbers + random_symbols
    random.shuffle(random_password) #to shuffl the cotinue of random password
    # print(random_password) 
    password = "".join(random_password) # to remove [] and , spaces
    print(f"Generated Password: {password}")