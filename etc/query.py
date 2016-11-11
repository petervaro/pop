## INFO ##
## INFO ##

# Import python modules
from sqlite3 import connect
from math    import asin, sin, cos, sqrt, radians

EARTH_RADIUS = 6371

def haversine(lat1, lon1, lat2, lon2) -> 'distance in km':
        return 2*EARTH_RADIUS*asin(
            sqrt(sin((lat2 - lat1)*0.5)**2 +
            cos(lat1)*cos(lat2)*sin((lon2 - lon1)*0.5)**2))

conn = connect('artists.db')
conn.create_function('haversine', 4, haversine)
c = conn.cursor()

with open('filter.sql') as query:
    artists = [a for a in c.execute(query.read(),
                                    {'youngest': 16,
                                     'latitude': 0.8990645879639032,
                                     'oldest': 74,
                                     'age_rank': 0.1,
                                     'gender_rank': 0.1,
                                     'distance_rank': 0.1,
                                     'rate_rank': 0.7,
                                     'radius': 8.0467,
                                     'count': 999,
                                     'rate': 24.0,
                                     'longitude': -0.0031458879088789513,
                                     'start': 1})]
print('ARTISTS:', *artists, sep='\n')
print('LENGTH:', len(artists))
