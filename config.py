## INFO ##
## INFO ##

# Import python modules
from os.path import abspath, dirname, join


# Module level constants
APP_BASE_DIR = abspath(dirname(__file__))

# Flask recognised constants
SECRET_KEY = (b'\x15\n]\xf3\xb7\xff\x9a\xb8\x0b\xff\xca'
              b'AM\xdc\x86\\\xdc\xd0!\xa3\xed\x18c\x98')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(APP_BASE_DIR, 'artists.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
