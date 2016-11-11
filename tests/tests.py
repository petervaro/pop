## INFO ##
## INFO ##

# Import test modules
from utils  import Unexpected

# Import test cases
from errors  import *
from simple  import *
from complex import *


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Module level constants
PREFIX   = 'test_'


#------------------------------------------------------------------------------#
if __name__ == '__main__':
    name = value = None
    success = 0
    failure = 0
    for name, value in sorted(locals().items()):
        if name.startswith(PREFIX):
            print('test case:', name[len(PREFIX):], end=' => ')
            try:
                value()
                success += 1
                print('SUCCESS')
            except Unexpected as e:
                failure += 1
                print('FAILURE')
                print('   ', str(e))
            except Exception as e:
                print('FAILURE')
                raise e

    print('-'*80)
    if not failure:
        print('All {} test(s) have ran successfully!'.format(success))
    else:
        print('{} test(s) succeeded, {} test(s) failed.'.format(success, failure))
    print()
