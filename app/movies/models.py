from app import db
from datetime import datetime


class Movie(db.Model):
    __tablename__ = 'Movie'
    id = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.String(20))
    homepage = db.Column(db.String(100))
    imdbid = db.Column(db.String(20))
    overview = db.Column(db.Text)
    popularity = db.Column(db.String(20))
    imdbscore = db.Column(db.Integer)
    releaseDate = db.Column(db.String)
    runtime = db.Column(db.Integer)
    tagline = db.Column(db.String(300))
    title = db.Column(db.String(200))
    voteAverage = db.Column(db.Integer)
    voteCount = db.Column(db.Integer)
    addedDate = db.Column(db.DateTime)
    cast = db.relationship('Cast', backref='Cast', lazy='dynamic')
    genres = db.relationship('MovieGenre', backref='MovieGenre', lazy='dynamic')
    image = db.Column(db.String)
    storageId = db.Column(db.Integer)

    def __init__(self, title, imdbid, tagline, addedDate=None, image=None, storageId=None):
        self.title = title
        self.imdbid = imdbid
        self.tagline = tagline
        self.image = image
        self.storageId = storageId
        if addedDate is None:
            addedDate = datetime.utcnow()

    def get_url(self):
        return '/movies/movie/' + str(self.id)


class Cast(db.Model):
    __tablename__ = 'Cast'
    id = db.Column(db.Integer, primary_key=True)
    personId = db.Column(db.Integer, db.ForeignKey('Person.id'))
    movieId = db.Column(db.Integer, db.ForeignKey('Movie.id'))
    charactor = db.Column(db.String(80))
    name = db.Column(db.String(80))
    order = db.Column(db.String(30))
    source = db.Column(db.String(30))
    type = db.Column(db.String(30))
    person = db.relationship('Person', backref='Person', lazy='subquery')

    def __init__(self, id, movieid, charactor, name, order, source, type):
        self.personId = id
        self.movieId = movieid
        self.charactor = charactor
        self.name = name
        self.order = order
        self.source = source
        self.type = type

    def getPersonName(self):
        # hack until i figure out problem
        return self.person.name
        # person = Person.query.filter_by(id=self.personId).first()
        # return person.name


class Person(db.Model):
    __tablename__ = 'Person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    birthday = db.Column(db.String(30))
    deathday = db.Column(db.String(30))
    homepage = db.Column(db.String(80))
    profilepath = db.Column(db.String(100))
    source = db.Column(db.String(30))

    def __init__(self, name, birthday=None, deathday=None, homepage= None, profileimage = None):
        self.name = name
        self.birthday = birthday
        self.deathday = deathday
        self.homepage = homepage
        self.profilepath = profileimage


class Genre(db.Model):
    __tablename__ = 'Genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    source = db.Column(db.String(30))

    def __init__(self, name, source, ):
        self.name = name
        self.source = source


class MovieGenre(db.Model):
    __tablename__ = "MovieGenre"
    movieGenreId = db.Column(db.Integer, primary_key=True)
    movieId = db.Column(db.Integer, db.ForeignKey('Movie.id'))
    genreId = db.Column(db.Integer, db.ForeignKey('Genre.id'))
    genre =  db.relationship('Genre', backref='Genre')

    def __init__(self, movieId, genreId ):
        self.movieId = movieId
        self.genreId = genreId

