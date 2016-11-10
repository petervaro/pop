## INFO ##
## INFO ##

# Import python modules
from json           import loads
from urllib.request import urlopen

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Module level constants
PREFIX   = 'test_case_'
BASE_URL = 'http://0.0.0.0:5000/pop/api/v1.0/artists'


#------------------------------------------------------------------------------#
class Unexpected(Exception): pass


#------------------------------------------------------------------------------#
def get(**parameters):
    params = ''
    for i, (param, value) in enumerate(parameters.items()):
        params += ('&' if i else '?') + param + '=' + str(value)
    return loads(urlopen(BASE_URL+params).read().decode('utf-8'))


#------------------------------------------------------------------------------#
def test_case_no_params():
    received = get()
    expected = {'rate': 10.0, 'oldest': 74, 'youngest': 16}
    if received != expected:
        raise Unexpected('Expected: {}, but got: {}'.format(expected, received))


#------------------------------------------------------------------------------#
def test_case_youngest_set_good():
    expected = 22
    received = get(youngest=expected)
    if received['youngest'] != expected:
        raise Unexpected('youngest should be 22 instead '
                         'of {youngest}'.format(**received))


#------------------------------------------------------------------------------#
def test_case_age_gender_location_set_good():
    received = get(youngest=18,
                   oldest=30,
                   gender='female',
                   longitude=51.5,
                   latitude=-0.15,
                   radius=1.2)
    print(received)


#------------------------------------------------------------------------------#
name = value = None
for name, value in locals().items():
    if name.startswith(PREFIX):
        print('test case:', name[len(PREFIX):], end=' => ')
        try:
            value()
            print('SUCCESS')
        except Unexpected as e:
            print('FAILURE')
            print('   ', str(e))
        except Exception as e:
            print('FAILURE')
            raise e
