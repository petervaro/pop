## INFO ##
## INFO ##

# Import python modules
from math import radians, pi

# Import flask modules
from flask import jsonify


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Module level constants
YOUNGEST     = 16
OLDEST       = 74
CHEAPEST     = 10.00
PRICIEST     = 39.97
GENDER       = 'male', 'female', 'both'
SORT         = 'age', 'rate', 'gender', 'distance'
ORDER        = {'ascending': 'asc', 'descending': 'desc'}
COUNT        = 999
LONGITUDE    = radians(-0.1802461)
LATITUDE     = radians(51.5126064)
RADIUS       = 1
EARTH_RADIUS = 3963
MAX_DISTANCE = pi*EARTH_RADIUS


#------------------------------------------------------------------------------#
class ParamError(Exception):

    CODE = 0
    TEXT = ''

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self, parameter, got, expected):
        self.name = parameter
        self.text = self.TEXT.format(parameter, expected, got)



#------------------------------------------------------------------------------#
class ParamTypeError(ParamError):

    CODE = 1
    TEXT = "Invalid type for '{}': expected {}, but got '{}'"



#------------------------------------------------------------------------------#
class ParamValueError(ParamError):

    CODE = 2
    TEXT = "Invalid value for '{}': expected {}, but got '{}'"



#------------------------------------------------------------------------------#
class ParamIsGreaterError(ParamError):

    CODE = 3
    TEXT = ("Out of range value for '{}': expected to "
            "be lesser than or equal to {}, but got {}")



#------------------------------------------------------------------------------#
class ParamIsLesserError(ParamError):

    CODE = 4
    TEXT = ("Out of range value for '{}': expected to "
            "be greater than or equal to {}, but got {}")



#------------------------------------------------------------------------------#
def jsonify_error(error):
    return jsonify({'error': {'code': error.CODE,
                              'text': error.text,
                              'name': error.name}})



#------------------------------------------------------------------------------#
def youngest(value, force):
    # If defined
    try:
        try:
            value = int(value)
        except ValueError:
            raise ParamTypeError('youngest', value, 'integer')

        if value < YOUNGEST:
            raise ParamIsLesserError('youngest', value, YOUNGEST)

        return value
    # If not defined
    except TypeError:
        return YOUNGEST
    # If invalid value defined
    except ParamError as error:
        if force:
            return YOUNGEST
        raise error


#------------------------------------------------------------------------------#
def oldest(value, force):
    # If defined
    try:
        try:
            value = int(value)
        except ValueError:
            raise ParamTypeError('oldest', value, 'integer')

        if value > OLDEST:
            raise ParamIsGreaterError('oldest', value, OLDEST)
        return value
    # If not defined
    except TypeError:
        return OLDEST
    # If invalid value defined
    except ParamError as error:
        if force:
            return OLDEST
        raise error


#------------------------------------------------------------------------------#
def rate(value, force):
    # If defined
    try:
        try:
            value = float(value)
        except ValueError:
            raise ParamTypeError('rate', value, 'float')

        if value < CHEAPEST:
            raise ParamIsLesserError('rate', value, CHEAPEST)
        elif value > PRICIEST:
            raise ParamIsGreaterError('rate', value, PRICIEST)

        return value
    # If not defined
    except TypeError:
        return CHEAPEST
    # If invalid value defined
    except ParamError as error:
        if force:
            return CHEAPEST
        raise error


#------------------------------------------------------------------------------#
def gender(value, force):
    # If not defined
    if value is None:
        return 'both'
    # If defined
    elif value in GENDER:
        return value
    # If invalid value defined
    elif force:
        return 'both'
    else:
        raise ParamValueError('gender', value, "'male', 'female' or 'both'")


#------------------------------------------------------------------------------#
def longitude(value, force):
    # If defined
    try:
        try:
            value = float(value)
        except ValueError:
            raise ParamTypeError('longitude', value, 'float')

        if value < -180:
            raise ParamIsLesserError('longitude', value, -180)
        elif value > 180:
            raise ParamIsGreaterError('longitude', value, 180)

        return radians(value)
    # If not defined
    except TypeError:
        return LONGITUDE
    # If invalid value defined
    except ParamError as error:
        if force:
            return LONGITUDE
        raise error


#------------------------------------------------------------------------------#
def latitude(value, force):
    # If defined
    try:
        try:
            value = float(value)
        except ValueError:
            raise ParamTypeError('latitude', value, 'float')

        if value < -90:
            raise ParamIsLesserError('latitude', value, -90)
        elif value > 90:
            raise ParamIsGreaterError('latitude', value, 90)

        return radians(value)
    # If not defined
    except TypeError:
        return LATITUDE
    # If invalid value defined
    except ParamError as error:
        if force:
            return LATITUDE
        raise error


#------------------------------------------------------------------------------#
def radius(value, force):
    # If defined
    try:
        try:
            value = float(value)
        except ValueError:
            raise ParamTypeError('radius', value, 'float')

        if value < 0:
            raise ParamIsLesserError('radius', value, 0)
        elif value > MAX_DISTANCE:
            raise ParamIsGreaterError('radius', value, MAX_DISTANCE)

        return radians(value)
    # If not defined
    except TypeError:
        return RADIUS
    # If invalid value defined
    except ParamError as error:
        if force:
            return RADIUS
        raise error


#------------------------------------------------------------------------------#
def sort(value, force):
    # If not defined
    if value is None:
        return 'rate'
    # If defined
    elif value in SORT:
        return value
    # If invalid value defined
    elif force:
        return 'rate'
    else:
        raise ParamValueError('gender', value, "'age', 'rate', "
                                               "'gender' or 'distance'")


#------------------------------------------------------------------------------#
def order(value, force):
    # If defined
    try:
        return ORDER[value]
    except KeyError:
        # If not defined
        if value is None or force:
            return 'asc'
        # If invalid value defined
        raise ParamValueError('order', value, "'ascending' or 'descending'")


#------------------------------------------------------------------------------#
def count(value, force):
    # If defined
    try:
        try:
            value = int(value)
        except ValueError:
            if value == 'all':
                return COUNT
            raise ParamTypeError('count', value, 'integer')

        if value < 1:
            raise ParamIsLesserError('count', value, 1)

        return value
    # If not defined
    except TypeError:
        return COUNT
    # If invalid value defined
    except ParamError as error:
        if force:
            return COUNT
        raise error


#------------------------------------------------------------------------------#
def start(value, force):
    # If defined
    try:
        try:
            value = int(value)
        except ValueError:
            raise ParamTypeError('start', value, 'integer')

        if value < 0:
            raise ParamIsLesserError('start', value, 0)

        return value
    # If not defined
    except TypeError:
        return 0
    # If invalid value defined
    except ParamError as error:
        if force:
            return 0
        raise error
