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
def test_complex_get_cheapest_closest_female_3():
    expected = ("55555555-5555-5555-5555-555555555555",
                "66666666-6666-6666-6666-666666666666",
                "77777777-7777-7777-7777-777777777777")
    received = get(count=3,
                   gender='female',
                   radius=2000,
                   sort='distance*1,rate*1')

    if not received:
        raise Unexpected('Expected 3 results, got none')

    for i, (uuid, artist) in enumerate(zip(expected, received)):
        if uuid != artist['uuid']:
            raise Unexpected('Expected UUID at {}: {}, but '
                             'got {}'.format(i, uuid, artist['uuid']))



#------------------------------------------------------------------------------#
def test_complex_get_equally_cheapest_closest_youngest_male_3():
    expected = ("11111111-1111-1111-1111-111111111111",
                "00000000-0000-0000-0000-000000000000",
                "33333333-3333-3333-3333-333333333333")
    received = get(count=3,
                   gender='male',
                   radius=10,
                   sort='age*1,distance*1,rate*1')

    if not received:
        raise Unexpected('Expected 3 results, got none')

    for i, (uuid, artist) in enumerate(zip(expected, received)):
        if uuid != artist['uuid']:
            raise Unexpected('Expected UUID at {}: {}, but '
                             'got {}'.format(i, uuid, artist['uuid']))



#------------------------------------------------------------------------------#
def test_complex_get_youngest_very_close_cheapest_enough_male_3():
    expected = ("33333333-3333-3333-3333-333333333333",
                "11111111-1111-1111-1111-111111111111",
                "22222222-2222-2222-2222-222222222222")
    received = get(count=3,
                   gender='male',
                   radius=10,
                   sort='age*1,distance*0.9,rate*0.8')

    if not received:
        raise Unexpected('Expected 3 results, got none')

    for i, (uuid, artist) in enumerate(zip(expected, received)):
        if uuid != artist['uuid']:
            raise Unexpected('Expected UUID at {}: {}, but '
                             'got {}'.format(i, uuid, artist['uuid']))


#------------------------------------------------------------------------------#
def test_complex_get_youngest_very_close_cheapest_enough_but_max_20_male_3():
    expected = ("11111111-1111-1111-1111-111111111111",
                "22222222-2222-2222-2222-222222222222",
                "00000000-0000-0000-0000-000000000000")
    received = get(count=3,
                   gender='male',
                   rate=22,
                   radius=10,
                   sort='age*1,distance*0.9,rate*0.8')

    if not received:
        raise Unexpected('Expected 3 results, got none')

    for i, (uuid, artist) in enumerate(zip(expected, received)):
        if uuid != artist['uuid']:
            raise Unexpected('Expected UUID at {}: {}, but '
                             'got {}'.format(i, uuid, artist['uuid']))
