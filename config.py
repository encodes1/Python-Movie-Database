import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['encodes1@gmail.com'])
SECRET_KEY = 'w43234435'
SQLALCHEMY_DATABASE_URI = 'postgresql://httkqucklymdhl:IzdNP8SZMVxgRpewHNcxfNA_NV@ec2-54-243-181-9.compute-1.amazonaws.com/ddtqeemf8pggrq'
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = 'blahblahblahblahblahblahblahblahblah'
RECAPTCHA_PRIVATE_KEY = 'blahblahblahblahblahblahprivate'
RECAPTCHA_OPTIONS = {'theme': 'white'}
UPLOAD_FOLDER = '//Users/mark/Projects/vooprint/app/static/uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
