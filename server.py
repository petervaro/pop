#!/usr/bin/env python
## INFO ##
## INFO ##

# API documentation
# =================
#
#   Query artists
#   -------------
#
#     http://<host>/pop/api/v1.0/artists
#
#   Filter paramteres
#   -----------------
#
#     youngest=<int> (default:16)
#     oldest=<int> (default:74)
#     rate=<float> (default:10.00)
#     gender=male|female|both (default:both)
#     longitude=<float> (default:-0.1802461)
#     latitude=<float> (default:51.5126064)
#     radius=<float> (default:1 (miles))
#     sort=age|rate|gender|distance (default:rate)
#     order=ascending|descending (default:ascending)
#     count=all|<int> (default:all)
#     start=<int> (default:0)
#     force=true|false (default:false)

# Import python modules
from sys import argv

# Import flask modules
from flask import Flask, jsonify, request

# Import pop modules
from db.models   import Artist
from db.database import session
from db.populate import populate
from params      import (youngest, oldest, rate, gender, longitude, latitude,
                         radius, sort, order, count, start, jsonify_error)


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

    # Start the query
    query = Artist.query
    query = query.filter(Artist.age.between(asked['youngest'], asked['oldest']))
    query = query.intersect(Artist.query.filter(Artist.rate <= asked['rate']))

    # If gender is specified
    if asked['gender'] != 'both':
        query = query.intersect(Artist.query.filter_by(gender=asked['gender']))

    # Set query order
    query = query.order_by(
        getattr({'age'    : Artist.age,
                 'gender' : Artist.gender,
                 'rate'   : Artist.rate,
                 'uuid'   : Artist.uuid}.get(asked['sort'], 'uuid'),
                asked['order'])())

    # Paginate...
    query = query.limit(asked['count'])

    # If debugging print the compiled SQL query
    if DEBUG:
         print(str(query.statement.compile(dialect=sqlite.dialect())))

    return jsonify([a.serialise() for a in query.all()])



#------------------------------------------------------------------------------#
if __name__ == '__main__':
    #  populate()
    app.run(debug = DEBUG,
            host  = '0.0.0.0')
