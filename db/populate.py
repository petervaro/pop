## INFO ##
## INFO ##

# Import python modules
from json import load

# Import pop modules
from db.models   import Artist
from db.database import initialise, session


#------------------------------------------------------------------------------#
def populate():
    # Initialise database
    initialise()

    # Build database from JSON
    with open('db/artists.json') as file:
        artists = load(file)
        for artist in artists['artists']:
            artist.update(gender='male' if artist['gender'] == 'M' else 'female')
            session.add(Artist(**artist))
        session.commit()
