
from mantisshrimp.domain.DomainObject import *

class Term(DomainObject):
    '''
    Terms are used to store information on possible locations. Included are:
    - the actual term used for the location search
    - the probability this term is actually a location
    - information on the location associated with this term
    - terms that probably better describe the location of this term
    - articles this term is found in
    '''
    
    def __init__(self):
        DomainObject.__init__(self)
        
        # raw input term used for geolocation
        self.raw_term = ''
        # true if geocoder has successfully located this term
        self.success = False
        # failure message if geocoder has failed to locate this term
        self.fail_message = ''
