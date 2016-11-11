## INFO ##
## INFO ##

# Import test modules
from utils import get, Unexpected

# Manually Picked Data Set
# ========================
#
# uuid     : 0 -> 9
# gender   : M(0, 4), F(5, 9)
# age      : 9 -> 0
# rate     : 0 -> 9
# distance : 0 -> 9

#------------------------------------------------------------------------------#
def test_simple_get_one_random():
    if not get(count=1):
        raise Unexpected('Expected to have a single random artist')

#------------------------------------------------------------------------------#
def test_simple_get_the_cheapest_3():
    expected = ("00000000-0000-0000-0000-000000000000",
                "11111111-1111-1111-1111-111111111111",
                "22222222-2222-2222-2222-222222222222")
    received = get(count=3, sort='age*0,gender*0,distance*0,rate*1')

    if not received:
        raise Unexpected('Expected 3 results, got none')

    for i, (uuid, artist) in enumerate(zip(expected, received)):
        if uuid != artist['uuid']:
            raise Unexpected('Expected UUID at {}: {}, but '
                             'got {}'.format(i, uuid, artist['uuid']))



#------------------------------------------------------------------------------#
def test_simple_get_the_closest_3():
    expected = ("00000000-0000-0000-0000-000000000000",
                "11111111-1111-1111-1111-111111111111",
                "22222222-2222-2222-2222-222222222222")
    received = get(count=3, sort='age*0,gender*0,distance*1,rate*0')

    if not received:
        raise Unexpected('Expected 3 results, got none')

    for i, (uuid, artist) in enumerate(zip(expected, received)):
        if uuid != artist['uuid']:
            raise Unexpected('Expected UUID at {}: {}, but '
                             'got {}'.format(i, uuid, artist['uuid']))



#------------------------------------------------------------------------------#
def test_simple_get_the_youngest_3():
    expected = ("99999999-9999-9999-9999-999999999999",
                "88888888-8888-8888-8888-888888888888",
                "77777777-7777-7777-7777-777777777777")
    received = get(count=3,
                   radius=1000,
                   sort='age*1,gender*0,distance*0,rate*0')

    if not received:
        raise Unexpected('Expected 3 results, got none')

    for i, (uuid, artist) in enumerate(zip(expected, received)):
        if uuid != artist['uuid']:
            raise Unexpected('Expected UUID at {}: {}, but '
                             'got {}'.format(i, uuid, artist['uuid']))
