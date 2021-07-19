movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']

# print(list(zip(movies, year)))

# new_d = dict()
# for movie, yr in zip(movies,year):
#     new_d[movie] = yr
# print(new_d)

new_dict = {movie:yr for movie,yr in zip(movies,year) if yr < 1983 and movie.startswith('Monty')}
print(new_dict)

n1 =[[f'{name}\'s favorite movie was {movie} from {yr}'] for name,movie,yr in zip(names,movies,year) if yr < 1981 ]
print(n1)

d1 = zip(movies, year)
d2 = {movie:years for movie,years in d1 if years > 1976}
print(d2)