"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system("createdb ratings")

model.connect_to_db(server.app)
model.db.create_all()
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:

    # print(f"movie: {movie}")
    # movie: {'overview': "While trying to make his sister's wedding day go smoothly, Jack finds himself juggling an angry ex-girlfriend, an uninvited guest with a secret, a misplaced sleep sedative, and the girl that got away in alternate versions of the same day.",
    #         'poster_path': 'https://image.tmdb.org/t/p/original//zn7feouGPU8sELez4qvpp0EtgeQ.jpg',
    #         'release_date': '2020-04-10',
    #         'title': 'Love Wedding Repeat'}

    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    title = movie["title"]
    overview = movie["overview"]
    poster_path = movie["poster_path"]

    format2 = "%Y-%m-%d"
    release_date =datetime.strptime(movie["release_date"], format2)


    # TODO: create a movie here and append it to movies_in_db
    movie_db = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(movie_db)

model.db.session.add_all(movies_in_db)
model.db.session.commit()

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # TODO: create a user here
    usr = crud.create_user(email= email, password = password)
    model.db.session.add(usr)

    # TODO: create 10 ratings for the user

    for i in range(10):

        score = randint(1,5)
        rate_movie = choice(movies_in_db)
        rat = crud.add_rating(rate_movie,usr,score)
        model.db.session.add(rat)

model.db.session.commit()
