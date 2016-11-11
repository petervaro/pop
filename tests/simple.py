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
