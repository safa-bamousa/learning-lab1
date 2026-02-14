#indent : after if and else


age = int(input("Enter your age please: "))
if age >= 12 :
    print("Good, You can use the app.")
else:
    print("Sorry, you can'y use the app.")


number = int(input("Please enter a number: "))
if number<0 :
    print("The number is negative.")
elif number==0:
    print("The number is null")
else:
    print("The number is posotive")


area = input("Chose an area: (Casablanca), (Rabat), or (Laayoune): ")
if area.lower() == "casablanca" :
    print("You choose Casablanca!")
elif area.upper() == "RABAT" :
    print("Rabat is very nice!")
elif area.lower() == "laayoune" :
    print("Laayoune feels always like summer!")
else:
    print(f"Sorry, {area} is not on our list!")


area = input("Chose an area: (Casablanca), (Rabat), or (Laayoune): ")
if area.lower() == "casablanca" or area.upper() == "RABAT" or area.lower() == "laayoune":
    print(f"{area} is on our list!")
else:
    print(f"Sorry, {area} is not on our list!")


print("""
Welcom to the show
You can sit in the front if you like
but it is expensive
""")

name = input("""
Welcom to the show
What is youe name?
""")

print("""

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
""")
#site: esymboles , quicktools