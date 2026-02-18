class Movie:
    def __init__(self, title, director, release_year, genre):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre

    def display_movie(self):
        print("")
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Release year: {self.release_year}")
        print(f"Genre: {self.genre}")

    def Change_movie_director(self, new_director):
        self.director = new_director

movie1 = Movie("Inception", "Christopher Nolan", 2010,"Sci-Fi")
movie2 = Movie("The Godfather", "Francis Ford", 1972,"Crime")
movie3 = Movie("Parasite", "Bon Jonn", 2019,"Thriller")

print("______ MOVIES LIST ______")
movie1.display_movie()
movie2.display_movie()
movie3.display_movie()

movie1.Change_movie_director("Shkry Sarham")
movie2.Change_movie_director("Ahmed Mazhar")
movie3.Change_movie_director("Ismel Yassine")

print("")
print("Changing Movie Directores .....")
movie1.display_movie()
movie2.display_movie()
movie3.display_movie()
