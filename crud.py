from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    return user



def create_movie(title, overview, release_date, poster_path):
    movie = Movie(
        title =title,
        overview=overview,
        release_date=release_date,
        poster_path=poster_path
    )
    return movie

def get_all_movies():

    all_movies = Movie.query.all()

    return all_movies

def get_movie_by_id(movie_id):

    movie = Movie.query.get(movie_id)

    return movie


def get_all_users():

    all_users = User.query.all()

    return all_users


def get_user_by_id(user_id):

    user = User.query.get(user_id)

    return user

def add_rating(movie,user,score):
    """Create and return a new user."""

    rating = Rating(movie=movie, user=user,score=score)

    return rating

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
