from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.movies.models import Movie
from app.movies.models import Genre
from app.movies.models import MovieGenre
from app.movies.models import Person
from app.movies.models import Cast
# import app.movies.forms as Form
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

mod = Blueprint('movies', __name__, url_prefix = '/movies')

@mod.route('/', methods=['GET', 'POST'])
def index():
    movies = Movie.query.order_by(Movie.title)
    return render_template("movies/list.html", movies = movies);


@mod.route('/movie/<movieid>', methods=['GET', 'POST'])
def movie(movieid):
    movie = Movie.query.filter_by(id=movieid).first_or_404()
    return render_template("movies/movie.html", movie = movie)
#
#
# ##TMDB STUFF
# @mod.route('/searchTmdb/', methods=['GET', 'POST'])
# def searchTmdb():
#     form = Form.searchMovieForm(request.form)
#
#     if form.validate_on_submit():
#
#         movies = tmdb3.searchMovie(form.name.data)
#         flash('Snipeet added', 'success-message')
#         return render_template("movies/searchResults.html",movies=movies)
#     return render_template("movies/searchTmdb.html", form = form)
#
#
# ##tmdb3 support
# @mod.route('/searchTmdb/Movie/<movieid>', methods = ['GET', 'POST'])
# def searchTmdbForMovie(movieid):
#     movie = tmdb3.Movie(movieid)
#     form = Form.addMovieForm(request.form)
#     if movie:
#         if request.method == 'POST' and form.validate_on_submit() :
#             # TOOD check
#             if form.tmdb3correct.data == True:
#                 if 'geturl' in dir(movie.poster):
#                     poster = movie.poster.geturl()
#                 else:
#                     poster = '.'
#                 dbMov = Movie(movie.title, movie.imdb, movie.tagline, movie.releasedate, poster)
#                 db.session.add(dbMov)
#                 for genre in movie.genres:
#                     dbGenre = Genre(genre.name, "tmdb3")
#                     db.session.add(dbGenre)
#                     # we commit to get ids :)
#                     db.session.commit()
#                     dbMovieGenre = MovieGenre(dbMov.id,dbGenre.id)
#                     db.session.add(dbMovieGenre)
#                     db.session.commit()
#                 # need to loop over people now :)
#                 for cast in movie.cast:
#                     order=1
#                     cast._populate_images()
#                     image = ''
#                     if 'geturl' in dir(cast.profile):
#                         image = cast.profile.geturl()
#                     dbPerson = Person(cast.name, cast.dayofbirth, cast.dayofdeath, cast.homepage, image)
#                     dbCast =  Cast(dbPerson.id, dbMov.id, cast.character, cast.name, order , 'TMDb3', 'cast')
#                     db.session.add(dbPerson)
#                     db.session.add(dbCast)
#                     db.session.commit()
#                     order = order + 1
#             else:
#                 dbMov = Movie(form.title.data, form.imbdId.data, form.tagline.data, form.releaseDate.data)
#                 db.session.add(dbMov)
#                 db.session.commit()
#             flash('Movie Added')
#             return redirect('movies')
#         else:
#             form.id.data = movie.id
#             form.title.data = movie.title
#             form.homepage.data = movie.homepage
#             form.budget.data = movie.budget
#             form.imbdId.data = movie.imdb
#             form.overview.data = movie.overview
#             form.popularity.data = movie.popularity
#             form.imdbscore.data = movie.userrating
#             form.releaseDate.data = movie.releasedate
#             form.runtime.data = movie.runtime
#             form.tagline.data = movie.tagline
#             form.releaseDate.data = movie.releasedate
#             form.storageId.data = 1
#             if 'geturl' in dir(movie.poster):
#                 poster = movie.poster.geturl()
#             else:
#                 poster = '.'
#             return render_template("movies/searchMovieInfo.html",form=form,img=poster)
