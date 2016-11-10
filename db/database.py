## INFO ##
## INFO ##

# Import python modules
from math import asin, sin, cos, sqrt

# Import sqlalchemy modules
from sqlalchemy                 import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm             import scoped_session, sessionmaker

# Import pop modules
from params import EARTH_RADIUS
from config import SQLALCHEMY_DATABASE_URI

#------------------------------------------------------------------------------#
def haversine(lat1, lon1, lat2, lon2) -> 'distance in km':
        return 2*EARTH_RADIUS*asin(
            sqrt(sin((lat2 - lat1)*0.5)**2 +
            cos(lat1)*cos(lat2)*sin((lon2 - lon1)*0.5)**2))


#------------------------------------------------------------------------------#
engine  = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)

@event.listens_for(engine, 'connect')
def connect(dbapi_connection, _):
    dbapi_connection.create_function('haversine', 4, haversine)

session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base = declarative_base()
Base.query = session.query_property()

#------------------------------------------------------------------------------#
def initialise():
    import db.models
    Base.metadata.create_all(bind=engine)
