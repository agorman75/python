movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
# if not in dictioinary, rather than returning 'None' the return will be 'not found'
print(movie.get('budget','not found'))
print(movie)

#updating
movie.update({'title' : 'The Holy Grail',
'year':1975,
'cast':['John','Eric','Michael','George','Terry']})

for key, value in movie.items():
    print(key, value)

#adding to dictionary
movie['title'] = 'The Holy Grail'
movie['budget'] = 25000

print(movie.get('title'))
print(movie.get('budget','not found'))
print(movie, "items here")

#delete key
# del movie['year']
year = movie.pop('year')
print(year)
print(movie.keys())
print(movie.values())
print(movie.items()) #printed as a tuples

