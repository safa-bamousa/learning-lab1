colors = []
colors.append(input("Add the first color you like: ").lower()) 
confirm = input("Do you want to add more colors? Yes, or No?").lower()
if confirm == "yes" :
    colors.append(input("Add another color to the list: ").lower()) 
print(f"""The colors you like are:{colors}""")

class_a = ["tom", "Sarah"]
class_b = ["Safa", "Bin"]
# class_a.extend(class_b) 
print(class_a + class_b)
class_a.remove("tom")
print(class_a)