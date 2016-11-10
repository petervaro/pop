#!/usr/bin/env python
## INFO ##
## INFO ##

# Import python modules
from sys       import argv

# Import flask modules
from flask import Flask, jsonify, request

# Import sqlalchemy modules
from sqlalchemy                import true
from sqlalchemy.sql.expression import func

# Import pop modules
from db.models   import Artist
from db.populate import populate
from db.database import session
from params      import (youngest, oldest, rate, gender, longitude, latitude,
                         radius, sort, order, count, start, jsonify_error,
                         ParamError, START, EARTH_RADIUS)


#------------------------------------------------------------------------------#
# Module level constants
DEBUG      = True if len(argv) > 1 and argv[1] in ('-D', '--debug') else False
PARAMETERS = {
    'youngest' : youngest,
    'oldest'   : oldest,
    'rate'     : rate,
    'gender'   : gender,
    'longitude': longitude,
    'latitude' : latitude,
    'radius'   : radius,
    'sort'     : sort,
    'order'    : order,
    'count'    : count,
    'start'    : start,
}


#------------------------------------------------------------------------------#
# Conditional imports
if DEBUG:
    # Import sqlalchemy modules
    from sqlalchemy.dialects import sqlite


#------------------------------------------------------------------------------#
# Setup flask
app = Flask(__name__)
app.config.from_object('config')


#------------------------------------------------------------------------------#
@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

#  @app.before_first_request
#  def populate_database(*args, counter=[0], **kwargs):
#      print('POPULATING', counter)
#      counter[0] += 1
#      populate()


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

    print(asked)

    query = Artist.query.filter(
        Artist.age.between(asked['youngest'], asked['oldest']),
        true() if asked['gender'] == 'both' else Artist.gender == asked['gender'],
        Artist.rate <= asked['rate'],
        func.haversine(asked['latitude'],
                       asked['longitude'],
                       Artist.latitude,
                       Artist.longitude) <= asked['radius'])

    query = query.order_by(
        getattr({'age'      : Artist.age,
                 'gender'   : Artist.gender,
                 'rate'     : Artist.rate,
                 'uuid'     : Artist.uuid,
                 'distance' : func.haversine(asked['latitude'],
                                             asked['longitude'],
                                             Artist.latitude,
                                             Artist.longitude)
                }.get(asked['sort'], 'uuid'),
                asked['order'])())

    # If debugging print the compiled SQL query
    if DEBUG:
         print('\n', str(query.statement.compile(dialect=sqlite.dialect())),
               end='\n\n', sep='\n')

    # Return paginated query
    count = asked['count']
    start = (asked['start'] - START)*count
    return jsonify([a.serialise() for a in query.slice(start, start + count)])



#------------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug = DEBUG,
            host  = '0.0.0.0')
