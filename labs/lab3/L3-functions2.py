movies = [
    {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
    },
    {
    "name": "Hitman",
    "imdb": 6.3,
    "category": "Action"
    },
    {
    "name": "Dark Knight",
    "imdb": 9.0,
    "category": "Adventure"
    },
    {
    "name": "The Help",
    "imdb": 8.0,
    "category": "Drama"
    },
    {
    "name": "The Choice",
    "imdb": 6.2,
    "category": "Romance"
    },
    {
    "name": "Colonia",
    "imdb": 7.4,
    "category": "Romance"
    },
    {
    "name": "Love",
    "imdb": 6.0,
    "category": "Romance"
    },
    {
    "name": "Bride Wars",
    "imdb": 5.4,
    "category": "Romance"
    },
    {
    "name": "AlphaJet",
    "imdb": 3.2,
    "category": "War"
    },
    {
    "name": "Ringing Crime",
    "imdb": 4.0,
    "category": "Crime"
    },
    {
    "name": "Joking muck",
    "imdb": 7.2,
    "category": "Comedy"
    },
    {
    "name": "What is the name",
    "imdb": 9.2,
    "category": "Suspense"
    },
    {
    "name": "Detective",
    "imdb": 7.0,
    "category": "Suspense"
    },
    {
    "name": "Exam",
    "imdb": 4.2,
    "category": "Thriller"
    },
    {
    "name": "We Two",
    "imdb": 7.2,
    "category": "Romance"
}
]

def worthwatching(movie):
    return movie.get('imdb') > 5.5
print(worthwatching(movies[0]))

def goodimdb(movies):
    return [movie for movie in movies if worthwatching(movie)]
print(goodimdb(movies))

def cat(movies, cat_name):
    return [movie for movie in movies if movie.get('category') == cat_name]
print(cat(movies, 'Romance'))

def avg_imdb(x):
    res = sum(movie.get('imdb') for movie in x)
    return res / len(x)
print(avg_imdb(movies))

def avgbycat(x, cat_name):
    res = sum(movie.get('imdb') for movie in cat(x, cat_name))
    return res / len(cat(x, cat_name))
print(avgbycat(movies, 'Romance'))