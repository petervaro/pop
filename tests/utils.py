## INFO ##
## INFO ##

# Import python modules
from json           import loads
from urllib.request import urlopen


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Module level constants
BASE_URL = 'http://0.0.0.0:5000/pop/api/v1.0/artists'


#------------------------------------------------------------------------------#
class Unexpected(Exception): pass


#------------------------------------------------------------------------------#
def get(**parameters):
    params = ''
    for i, (param, value) in enumerate(parameters.items()):
        params += ('&' if i else '?') + param + '=' + str(value)
    return loads(urlopen(BASE_URL+params).read().decode('utf-8'))
