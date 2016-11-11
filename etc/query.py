## INFO ##
## INFO ##

# Import python modules
from sqlite3 import connect
from math    import asin, sin, cos, sqrt, radians

EARTH_RADIUS = 6371
FILTER = """
SELECT artists.uuid,
       artists.gender,
       artists.age,
       artists.rate,
       artists.longitude,
       artists.latitude,
       haversine(:latitude, :longitude,
                 artists.latitude, artists.longitude) AS distance FROM artists
    WHERE artists.rate <= :rate AND
          artists.age BETWEEN :youngest AND :oldest AND
          distance <= :radius
          ORDER BY distance ASC;
          LIMIT :limit OFFSET :offset;
"""

def haversine(lat1, lon1, lat2, lon2) -> 'distance in km':
        return 2*EARTH_RADIUS*asin(
            sqrt(sin((lat2 - lat1)*0.5)**2 +
            cos(lat1)*cos(lat2)*sin((lon2 - lon1)*0.5)**2))

conn = connect('artists.db')
conn.create_function('haversine', 4, haversine)
c = conn.cursor()
xs = c.execute(FILTER, {'youngest'  : 20,
                        'oldest'    : 22,
                        'rate'      : 30,
                        'latitude'  : radians(51.5126064),
                        'longitude' : radians(-0.1802461),
                        'radius'    : 16.0934,
                        'limit'     : 999,
                        'offset'    : 0})
for x in xs:
    print(x)
