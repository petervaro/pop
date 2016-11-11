#!/usr/bin/env python
## INFO ##
## INFO ##

# Import python modules
from sys       import argv, exit
from itertools import islice
from os.path   import abspath, dirname, join

# Import flask modules
from flask import Flask, jsonify, request

# Import sqlalchemy modules
from sqlalchemy.sql.expression import literal_column
from sqlalchemy                import true, asc, desc, case

# Import pop modules
from params import (youngest, oldest, rate, gender, longitude, latitude, radius,
                    sort, order, count, start, jsonify_error, ParamError, START,
                    EARTH_RADIUS)


#------------------------------------------------------------------------------#
# Setup flask
app = Flask(__name__)
app.config.from_object('config')



#------------------------------------------------------------------------------#
# Module level constants
DEBUG      = False
POPULATE   = False
JSON_PATH  = join('db', 'artists.json')
PARAMETERS = {'youngest' : youngest,
              'oldest'   : oldest,
              'rate'     : rate,
              'gender'   : gender,
              'longitude': longitude,
              'latitude' : latitude,
              'radius'   : radius,
              'sort'     : sort,
              'order'    : order,
              'count'    : count,
              'start'    : start}

DUMMY_FLAGS    = '-d', '--dummy'
DEBUG_FLAGS    = '-D', '--debug'
POPULATE_FLAGS = '-P', '--populate'



#------------------------------------------------------------------------------#
# Set values by command line arguments
for arg in islice(argv, 1, len(argv)):
    if arg in DEBUG_FLAGS:
        from sqlalchemy.dialects import sqlite
        DEBUG     = True

    elif arg in DUMMY_FLAGS:
        import config
        JSON_PATH = join('tests', 'artists.json')
        config.SQLALCHEMY_DATABASE_URI = \
            'sqlite:///' + join(abspath(dirname(__file__)), 'tests', 'artists.db')

    elif arg in POPULATE_FLAGS:
        POPULATE = True



#------------------------------------------------------------------------------#
# Import pop database related modules
from db.models   import Artist
from db.populate import populate
from db.database import session



#------------------------------------------------------------------------------#
@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()



#------------------------------------------------------------------------------#
if POPULATE:
    @app.before_first_request
    def populate_db(*args, **kwargs):
        populate(JSON_PATH)



#------------------------------------------------------------------------------#
@app.route('/')
def index():
    return 'POP test server is up and running!'



#------------------------------------------------------------------------------#
@app.route('/pop/api/v1.0/artists', methods=['GET'])
def artists():
    # If force is 'false' if not defined or specifically defined, otherwise
    # any value is treated as an attempt to define force to be 'true'
    force = request.args.get('force')
    force = True if force is not None and force != 'false' else False

    # Get and set each parameter's value
    asked = {}
    for parameter, getter in PARAMETERS.items():
        try:
            asked[parameter] = getter(request.args.get(parameter), force)
        except ParamError as error:
            return jsonify_error(error)


    count = asked['count']
    start = (asked['start'] - START)*count
    weights = asked['sort']
    distance = Artist.distance(asked['latitude'],
                               asked['longitude']).label('distance')
    query = session.query(Artist, distance).filter(
        true() if asked['gender'] == 'both' else Artist.gender == asked['gender'],
        Artist.rate <= asked['rate'],
        Artist.age.between(asked['youngest'], asked['oldest']),
        literal_column(distance.name) <= asked['radius']
    ).order_by(
    (asc if asked['order'] == 'asc' else desc)(
        (weights['age']*Artist.age) +
        (weights['gender']*Artist.gender) +
        (weights['rate']*Artist.rate) +
        (weights['distance']*literal_column(distance.name))
        )).slice(start, start + count)


    # If debugging print the compiled SQL query
    if DEBUG:
        print('\n',
              str(query.statement.compile(dialect=sqlite.dialect())),
              'parameters:',
              asked,
              sep='\n',
              end='\n\n')

    # Return serialised and jsonified result
    return jsonify([artist.serialise(distance) for artist, distance in query])



#------------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug = DEBUG,
            host  = '0.0.0.0')
