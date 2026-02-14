#Asking the user for the books he have:
books_own = []
books_own.append(input("Enter the name of a book you own: ").lower())
confirm = input("Enter the name of another book you own (or press 'Enter' to skip): ").lower()
if confirm :
    books_own.append(confirm)
print(f"Your Library: {books_own}")

#Asking the user for books he wish he have:
books_wish = []
books_wish.append(input("Enter the name of a book you wish to have in the future: ").lower())
confirm = input("Enter the name of another book you wish you have in the future (or press 'Enter' to skip): ").lower()
if confirm :
    books_wish.append(confirm)
print(f"Your WishListe: {books_wish}")

#Asking the user if he had a book from the wishList
confirm = input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ").lower()
if confirm in books_wish:
    books_wish.remove(confirm)
    print(f"Update Liberary: {books_own}\nUpdated WishList: {books_wish}")

#Asking the user if he wanna donate a book he have
confirm = input("Enter the name of a book from your liberary you wish to donate (or press 'Enter' to skip): ").lower()
if confirm in books_own:
    books_own.remove(confirm)
    print(f"Final Liberary after Danations: {books_own}")
