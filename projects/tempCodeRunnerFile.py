#Asking the user for books he wish he have:
books_wish = []
books_wish.append(input("Enter the name of a book you wish to have in the future: ").lower())
confirm = input("Enter the name of another book you wish you have in the future (or press 'Enter' to skip): ").lower()
if confirm :
    books_wish.append(confirm)
print(f"Your WishListe: {books_wish}")