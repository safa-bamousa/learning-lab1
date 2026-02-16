names = input("Enter the first and last name of your friends separated by comma: ")

names_list = names.split(", ")

abbreviated_name = []

for name in names_list: 
    name_parts = name.split()
    print(name_parts)

    first_name = name_parts[0].upper()
    last_name = name_parts[1].upper()

    first_initial = first_name[0]
    last_initial = last_name[0]

    abbreviated = first_initial + "." + last_initial + "."

    abbreviated_name.append(abbreviated)

print("Abbreviated Names:")
for x in abbreviated_name :
    print(x)

