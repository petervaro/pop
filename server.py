#!/usr/bin/env python
## INFO ##
## INFO ##

# Import python modules
from sys       import argv
from itertools import islice
from os.path   import abspath, dirname, join


#------------------------------------------------------------------------------#
# Module level constants
DEBUG      = False
POPULATE   = False
JSON_PATH  = join('db', 'artists.json')

DUMMY_FLAGS    = '-d', '--dummy'
DEBUG_FLAGS    = '-D', '--debug'
POPULATE_FLAGS = '-P', '--populate'



#------------------------------------------------------------------------------#
# Set values by command line arguments
for arg in islice(argv, 1, len(argv)):
    if arg in DEBUG_FLAGS:
        DEBUG = True

    elif arg in DUMMY_FLAGS:
        import config
        JSON_PATH = join('tests', 'artists.json')
        config.SQLALCHEMY_DATABASE_URI = \
            'sqlite:///' + join(abspath(dirname(__file__)), 'tests', 'artists.db')

    elif arg in POPULATE_FLAGS:
        POPULATE = True


#------------------------------------------------------------------------------#
if __name__ == '__main__':
    from app import app

    app.config['POPULATE_DB'] = POPULATE
    app.config['POPULATION_DATA_PATH'] = JSON_PATH

    app.run(debug = DEBUG,
            host  = '0.0.0.0')
