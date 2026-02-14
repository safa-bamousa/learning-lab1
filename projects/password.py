import random
pin_user = input("Enter a 4_digit PIN code: ")
while len(pin_user) != 4 :
    pin_user = input("Enter a 4 digit: ")
pin_computer = f"{random.randint(0,9999):04}"
if pin_computer == pin_user :
    print("PIN code is correct!")
else:
    print(f"""Failure! PIN code did not match!
The computer generate this PIN:{pin_computer}
""")
# 04 means:
#     total width = 4 digits
#     add zeros in front if needed
