#Classes are blueprints
#Objects are the actual things you built
#variables => attributes
#functions => methods
#Self refers to the object we are creating

class Movie:
    def __init__(self, title, year, imdb_score, have_seen):
            self.title = title
            self.year = year
            self.imdb_score = imdb_score
            self.have_seen = have_seen
        
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)

film1 = Movie("Life of Brian", 1979, 8.1, True)
film2 = Movie("The Holy Grail ", 1975, 8.2, True)

# print(film1.title, film1.imdb_score)
# film2.nice_print()
# Movie.nice_print(film2)
#Make a database of the above by using a list

films = [film1, film2]
print(films[1].title, films[0].title)
films[0].nice_print()