#!/usr/bin/env python
import os
import readline
from pprint import pprint

from flask import *
from app import *
from app.movies.models import Movie
from app.movies.models import Genre
from app.movies.models import MovieGenre
from app.movies.models import Person
from app.movies.models import Cast
import tmdb3
import csv
import tmdbsimple as tmdb


tmdb.API_KEY ='c9a18ea34091a088d00dfa65325c19db'

os.environ['PYTHONINSPECT'] = 'True'


# lets delete the database for now.
db.drop_all()
db.create_all()
db.session.commit()
#exit()
with open('/Users/marktooth/Projects/python-movies2/dvds.csv', 'rb') as csvfile:
    movies = csv.DictReader(csvfile)
    for mov in movies:
        if mov['IMDB_ID'] == '':
            pass
            # we have friends which crashes tmdb
            print 'manual addimg of ' + mov['Title']
            dbMov = Movie(mov['Title'], mov['IMDB_ID'],None, None, None, mov['DVD_ID'])
            db.session.add(dbMov)
            db.session.commit()
        else:

            external_source = 'imdb_id'
            find = tmdb.Find(mov['IMDB_ID'])
            response = find.info(external_source=external_source)
            if len(response['movie_results']):
                #     we have a movie
                movie = response['movie_results'][0]
                movie = tmdb.Movies(movie['id'])
                m = movie.info()
                dbMov = Movie(m['original_title'], mov['IMDB_ID'], m['tagline'][0:297]+'...', m['release_date'], 'http://image.tmdb.org/t/p/w396' + m['poster_path'], mov['DVD_ID'])
                db.session.add(dbMov)
                db.session.commit()
                print 'added ' + m['original_title']
                #  now to add the code to add genres...
                for genre in m['genres']:
                    # test if genre exists.
                    dbGenre = Genre(genre['name'], "tmdb3")
                    db.session.add(dbGenre)
                    # we commit to get ids :)
                    db.session.commit()
                    dbMovieGenre = MovieGenre(dbMov.id, dbGenre.id)
                    db.session.add(dbMovieGenre)
                    db.session.commit()
                    # need to loop over people now :)
                cast = movie.credits()
                order = 1
                for c in cast['cast']:

                    # cast._populate_images()
                    # image = ''
                    # if 'geturl' in dir(cast.profile):
                    #     image = cast.profile.geturl()
                    dbPerson = Person(c['name'], '', '', '', '')
                    db.session.add(dbPerson)
                    db.session.commit()

                    dbCast =  Cast(dbPerson.id, dbMov.id, c['character'], c['name'], order , 'TMDb3', 'cast')

                    db.session.add(dbCast)
                    db.session.commit()
                    order = mov['DVD_ID']





            elif len(response['tv_results']):
                tv = response['tv_results'][0]
                tv = tmdb.TV(tv['id']).info()
                dbMov = Movie(tv['name'], mov['IMDB_ID'], tv['overview'][0:297]+'...', tv['first_air_date'], 'http://image.tmdb.org/t/p/w396' + tv['poster_path'], mov['DVD_ID'])
                db.session.add(dbMov)
                db.session.commit()
                print 'added ' + tv['name']



