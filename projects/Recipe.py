class Recipe:
    def __init__(self, name, ingredients, cooking_time, cooking_instructions):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.cooking_instructions = cooking_instructions
    
    def display_Recipe(self):
        print("")
        print(f"Name: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Cooking time: {self.cooking_time}")
        print(f"Cooking instructions: {self.cooking_instructions}")
        print("_" * 20)

def add_Recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma_seperated)")
    cooking_time = input("Enter cooking time: ")
    cooking_instructions = input("Enter cooking instructions: ")
    return Recipe(name, ingredients,cooking_time, cooking_instructions)

recipe1 = add_Recipe()
print("Display recipe ....")
recipe1.display_Recipe()