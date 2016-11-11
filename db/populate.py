## INFO ##
## INFO ##

# Import python modules
from json import load
from math import radians

# Import pop modules
from db.models   import Artist
from db.database import initialise, session


#------------------------------------------------------------------------------#
def populate(path):
    # Initialise database
    initialise()

    # Build database from JSON
    with open(path) as file:
        artists = load(file)
        for i, artist in enumerate(artists['artists']):
            artist.update(gender='male' if artist['gender'] == 'M' else 'female')
            artist.update(longitude=radians(float(artist['longitude'])))
            artist.update(latitude=radians(float(artist['latitude'])))
            session.add(Artist(**artist))
        session.commit()
