## INFO ##
## INFO ##

# Import python modules
from math        import radians, pi
from collections import OrderedDict

# Import pop modules
from validators import (enum_value_validator,
                        range_value_validator,
                        minimum_value_validator,
                        ParamTypeError,
                        ParamValueError,
                        ParamIsLesserError,
                        ParamIsGreaterError)


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Module level constants
YOUNGEST     = 16
OLDEST       = 74
CHEAPEST     = 10.00
PRICIEST     = 39.97
GENDER       = OrderedDict(((v,v) for v in ('male', 'female', 'both')))
SORT         = 'age', 'rate', 'gender', 'distance'
ORDER        = OrderedDict((('ascending', 'asc'), ('descending', 'desc')))
COUNT        = 999
START        = 1
LONGITUDE    = radians(-0.1802461)
LATITUDE     = radians(51.5126064)
MILE_IN_KM   = 1.60934
EARTH_RADIUS = 6371
RADIUS       = 5*MILE_IN_KM
MAX_DISTANCE = pi*EARTH_RADIUS/MILE_IN_KM



#------------------------------------------------------------------------------#
youngest = range_value_validator(name      = 'youngest',
                                 type      = int,
                                 type_name = 'integer',
                                 minimum   = YOUNGEST,
                                 maximum   = OLDEST,
                                 default   = YOUNGEST)



#------------------------------------------------------------------------------#
oldest = range_value_validator(name      = 'oldest',
                               type      = int,
                               type_name = 'integer',
                               minimum   = YOUNGEST,
                               maximum   = OLDEST,
                               default   = OLDEST)



#------------------------------------------------------------------------------#
rate = range_value_validator(name      = 'rate',
                             type      = float,
                             type_name = 'floating point number',
                             minimum   = CHEAPEST,
                             maximum   = PRICIEST,
                             default   = PRICIEST)



#------------------------------------------------------------------------------#
gender = enum_value_validator(name    = 'gender',
                              default = 'both',
                              enums   = GENDER)



#------------------------------------------------------------------------------#
longitude = range_value_validator(name      = 'longitude',
                                  type      = float,
                                  type_name = 'floating point number',
                                  minimum   = -180,
                                  maximum   = +180,
                                  default   = LONGITUDE)



#------------------------------------------------------------------------------#
latitude = range_value_validator(name      = 'latitude',
                                 type      = float,
                                 type_name = 'floating point number',
                                 minimum   = -90,
                                 maximum   = +90,
                                 default   = LATITUDE)



#------------------------------------------------------------------------------#
_radius = range_value_validator(name      = 'radius',
                               type      = float,
                               type_name = 'floating point number',
                               minimum   = 0,
                               maximum   = MAX_DISTANCE,
                               default   = RADIUS)
def radius(value, force):
    return _radius(value, force)*MILE_IN_KM



#------------------------------------------------------------------------------#
def sort(values, force):
    weights = {'age'      : 0.0,
               'rate'     : 0.0,
               'gender'   : 0.0,
               'distance' : 0.0}
    try:
        for weight in values.split(','):
            try:
                key, weight = weight.split('*')
            # If weight is missing
            except ValueError:
                if force:
                    continue
                raise ParamValueError('sort', weight,
                                      'weight value, eg. age*0.8')

            if key in weights:
                try:
                    weight = float(weight)
                # If weight is not a number
                except ValueError:
                    if not force:
                        raise ParamTypeError(key, weight, 'float')

                if weight > 1.0:
                    if force:
                        weight = 1.0
                    else:
                        raise ParamIsGreaterError(key, weight, 1.0)
                elif weight < 0.0:
                    if force:
                        weight = 0.0
                    else:
                        raise ParamIsLesserError(key, weight, 0.0)

                # Set weight
                weights[key] = float(weight)
            # If key is not valid
            else:
                if not force:
                    raise ParamValueError('sort', key, "'age', 'rate', "
                                                       "'gender' or 'distance'")
    # If not defined
    except AttributeError:
        pass

    return weights



#------------------------------------------------------------------------------#
order = enum_value_validator(name    = 'order',
                             default = 'asc',
                             enums   = ORDER)



#------------------------------------------------------------------------------#
count = minimum_value_validator(name      = 'count',
                                type      = int,
                                type_name = 'integer',
                                minimum   = 1,
                                default   = COUNT)



#------------------------------------------------------------------------------#
start = minimum_value_validator(name      = 'start',
                                type      = int,
                                type_name = 'integer',
                                minimum   = START,
                                default   = START)
