## INFO ##
## INFO ##

# Import python modules
from math import degrees

# Import sqlalchemy modules
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.hybrid     import hybrid_method
from sqlalchemy                import Column, String, Enum, Integer, Float

# Import pop modules
from params      import EARTH_RADIUS
from db.database import Base, haversine


#------------------------------------------------------------------------------#
class Artist(Base):

    __tablename__ = 'artists'

    uuid      = Column(String(36), primary_key=True)
    gender    = Column(Enum('male', 'female'))
    age       = Column(Integer)
    rate      = Column(Float)
    longitude = Column(Float)
    latitude  = Column(Float)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    @hybrid_method
    def distance(self, latitude, longitude):
        return haversine(latitude, longitude,
                         self.latitude, self.longitude)

    @distance.expression
    def distance(self, latitude, longitude):
        return func.haversine(latitude, longitude,
                              self.latitude, self.longitude)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __repr__(self):
        return ('<Artist (uuid={0.uuid!r}, '
                         'gender={0.gender!r}, '
                         'age={0.age!r}, '
                         'rate=\u00A3{0.rate!r}, '
                         'longitude={0.longitude!r}\u03C0, '
                         'latitude={0.latitude!r}\u03C0)').format(self)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def serialise(self, distance) -> dict:
        return {'uuid'      : self.uuid,
                'gender'    : 'M' if self.gender == 'male' else 'F',
                'age'       : self.age,
                'rate'      : self.rate,
                'longitude' : degrees(self.longitude),
                'latitude'  : degrees(self.latitude),
                'distance'  : distance}
