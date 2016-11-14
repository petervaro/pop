## INFO ##
## INFO ##

# Import flask modules
from flask import Flask, jsonify, request

# Import sqlalchemy modules
from sqlalchemy.dialects       import sqlite
from sqlalchemy.sql.expression import literal_column
from sqlalchemy                import true, asc, desc

# Import pop modules
from db.models   import Artist
from db.populate import populate
from db.database import session
from validators  import ParamError
from params      import (youngest, oldest, rate, gender, longitude, latitude,
                         radius, sort, order, count, start, START)


#------------------------------------------------------------------------------#
# Module level constants
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


#------------------------------------------------------------------------------#
# Setup flask
app = Flask(__name__)
app.config.from_object('config')



#------------------------------------------------------------------------------#
@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()



#------------------------------------------------------------------------------#
@app.before_first_request
def populate_db(*args, **kwargs):
    if app.config['POPULATE_DB']:
        populate(app.config['POPULATION_DATA_PATH'])



#------------------------------------------------------------------------------#
@app.route('/')
def index():
    return 'POP test server is up and running!'



#------------------------------------------------------------------------------#
@app.route('/pop/api/v1.0/artists', methods=['GET'])
def artists():
    # If the user not specifically define 'false' for force (which is the
    # default) value, then the attempt will be treated as if it were defined as
    # 'true'. Eg. force=yes or force=1 and even force=fasle (mistyped value)
    # will be treated as force=true
    force = request.args.get('force')
    force = True if force is not None and force != 'false' else False

    # Get and set each parameter's value
    asked = {}
    for parameter, getter in PARAMETERS.items():
        try:
            asked[parameter] = getter(request.args.get(parameter), force)
        except ParamError as error:
            return error.jsonify()


    # Store values more than once locally
    count    = asked['count']
    start    = (asked['start'] - START)*count
    weights  = asked['sort']
    distance = Artist.distance(asked['latitude'],
                               asked['longitude']).label('distance')

    # Do the query
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


    # If debugging mode is on print the compiled SQL(ite) query
    if app.debug:
        print('\n',
              str(query.statement.compile(dialect=sqlite.dialect())),
              'parameters:',
              asked,
              sep='\n',
              end='\n\n')

    # Return serialised and jsonified result
    return jsonify([artist.serialise(distance) for artist, distance in query])
