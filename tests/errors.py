## INFO ##
## INFO ##

# Import test modules
from utils import get, Unexpected


#------------------------------------------------------------------------------#
def test_error_youngest_nan():
    expected = 'Expected ParamTypeError, code 1'
    try:
        received = get(youngest='hello')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 1:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_youngest_out_of_range_lesser():
    expected = 'Expected ParamIsLesserError, code 4'
    try:
        received = get(youngest=2)['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 4:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_youngest_out_of_range_greater():
    expected = 'Expected ParamIsGreaterError, code 3'
    try:
        received = get(youngest=99)['error']
    except (KeyError, TypeError):
        raise Unexpected(expected)

    if received['code'] != 3:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_oldest_nan():
    expected = 'Expected ParamTypeError, code 1'
    try:
        received = get(oldest='good-bye')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 1:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_oldest_out_of_range_lesser():
    expected = 'Expected ParamIsLesserError, code 4'
    try:
        received = get(oldest=2)['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 4:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_oldest_out_of_range_greater():
    expected = 'Expected ParamIsGreaterError, code 3'
    try:
        received = get(oldest=99)['error']
    except (KeyError, TypeError):
        raise Unexpected(expected)

    if received['code'] != 3:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_rate_nan():
    expected = 'Expected ParamTypeError, code 1'
    try:
        received = get(rate='free')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 1:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_rate_out_of_range_lesser():
    expected = 'Expected ParamIsLesserError, code 4'
    try:
        received = get(rate=2)['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 4:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_rate_out_of_range_greater():
    expected = 'Expected ParamIsGreaterError, code 3'
    try:
        received = get(rate=99)['error']
    except (KeyError, TypeError):
        raise Unexpected(expected)

    if received['code'] != 3:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_gender_invalid():
    expected = 'Expected ParamValueError, code 2'
    try:
        received = get(gender='boy')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 2:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_longitude_nan():
    expected = 'Expected ParamTypeError, code 1'
    try:
        received = get(longitude='here')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 1:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_longitude_out_of_range_lesser():
    expected = 'Expected ParamIsLesserError, code 4'
    try:
        received = get(longitude=-270.287778)['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 4:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_longitude_out_of_range_greater():
    expected = 'Expected ParamIsGreaterError, code 3'
    try:
        received = get(longitude=312.45698)['error']
    except (KeyError, TypeError):
        raise Unexpected(expected)

    if received['code'] != 3:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_latitude_nan():
    expected = 'Expected ParamTypeError, code 1'
    try:
        received = get(latitude='nowhere')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 1:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_latitude_out_of_range_lesser():
    expected = 'Expected ParamIsLesserError, code 4'
    try:
        received = get(latitude=-120.0001)['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 4:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_latitude_out_of_range_greater():
    expected = 'Expected ParamIsGreaterError, code 3'
    try:
        received = get(latitude=91.00)['error']
    except (KeyError, TypeError):
        raise Unexpected(expected)

    if received['code'] != 3:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_radius_nan():
    expected = 'Expected ParamTypeError, code 1'
    try:
        received = get(radius='near')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 1:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_radius_out_of_range_lesser():
    expected = 'Expected ParamIsLesserError, code 4'
    try:
        received = get(radius=-1)['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 4:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_radius_out_of_range_greater():
    expected = 'Expected ParamIsGreaterError, code 3'
    try:
        received = get(radius=13000)['error']
    except (KeyError, TypeError):
        raise Unexpected(expected)

    if received['code'] != 3:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_order_invalid():
    expected = 'Expected ParamValueError, code 2'
    try:
        received = get(order='whatever')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 2:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_count_nan():
    expected = 'Expected ParamTypeError, code 1'
    try:
        received = get(count='more')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 1:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_count_out_of_range_lesser():
    expected = 'Expected ParamIsLesserError, code 4'
    try:
        received = get(count=0)['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 4:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_start_nan():
    expected = 'Expected ParamTypeError, code 1'
    try:
        received = get(start='beginning')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 1:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_start_out_of_range_lesser():
    expected = 'Expected ParamIsLesserError, code 4'
    try:
        received = get(start=-1)['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 4:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_sort_invalid_keys():
    expected = 'Expected ParamValueError, code 2'
    try:
        received = get(sort='height*0.2')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 2:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_sort_correct_keys_no_weights():
    expected = 'Expected ParamValueError, code 2'
    try:
        received = get(sort='age')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 2:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_sort_correct_keys_and_weights_no_separator():
    expected = 'Expected ParamValueError, code 2'
    try:
        received = get(sort='age*0.1gender*0.2')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 2:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_sort_correct_keys_and_weights_missing_multiply():
    expected = 'Expected ParamValueError, code 2'
    try:
        received = get(sort='age0.1,gender0.2')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 2:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_sort_correct_keys_weights_out_of_range_lesser():
    expected = 'Expected ParamIsLesserError, code 4'
    try:
        received = get(sort='age*-0.2')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 4:
        raise Unexpected(expected)



#------------------------------------------------------------------------------#
def test_error_sort_correct_keys_weights_out_of_range_greater():
    expected = 'Expected ParamIsGreaterError, code 3'
    try:
        received = get(sort='age*12')['error']
    except KeyError:
        raise Unexpected(expected)

    if received['code'] != 3:
        raise Unexpected(expected)
