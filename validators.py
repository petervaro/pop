## INFO ##
## INFO ##

# Import python modules
from itertools import islice

# Import flask modules
from flask import jsonify


#------------------------------------------------------------------------------#
class ParamError(Exception):

    CODE = 0
    TEXT = ''

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self, parameter, got, expected):
        self.name = parameter
        self.text = self.TEXT.format(parameter, expected, got)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def jsonify(self):
        return jsonify({'error': {'code': self.CODE,
                                  'text': self.text,
                                  'name': self.name}})



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
def range_value_validator(name,
                          type,
                          type_name,
                          minimum,
                          maximum,
                          default):
    # Create new validator function
    def validator(value, force):
        # If defined
        try:
            try:
                value = type(value)
            # If value is invalid for `type`
            except ValueError:
                raise ParamTypeError(name, value, type_name)

            # Check if value is in desired range
            if value < minimum:
                raise ParamIsLesserError(name, value, minimum)
            elif value > maximum:
                raise ParamIsGreaterError(name, value, maximum)

            # Return checked and converted value
            return value

        # If value is None => not defined
        except TypeError:
            return default
        # If invalid or out of range
        except ParamError as error:
            if force:
                return default
            raise error
    # Return new validator
    return validator



#------------------------------------------------------------------------------#
def minimum_value_validator(name,
                            type,
                            type_name,
                            minimum,
                            default):
    # Create new validator function
    def validator(value, force):
        # If defined
        try:
            try:
                value = type(value)
            # If value is invalid for `type`
            except ValueError:
                raise ParamTypeError(name, value, type_name)

            # Value check
            if value < minimum:
                raise ParamIsLesserError(name, value, minimum)

            # Return checked and converted value
            return value

        # If value is None => not defined
        except TypeError:
            return default
        # If invalid
        except ParamError as error:
            if force:
                return default
            raise error

    # Return new validator
    return validator



#------------------------------------------------------------------------------#
def enum_value_validator(name,
                         default,
                         enums):
    keys   = tuple(enums.keys())
    values = (', '.join(map(repr, islice(keys, len(keys) - 1))) +
              ' or ' + repr(keys[-1]))

    # Create new validator function
    def validator(value, force):
        try:
            return enums[value]
        except KeyError:
            if value is None or force:
                return default
            raise ParamValueError(name, value, values)

    # Return new validator
    return validator
