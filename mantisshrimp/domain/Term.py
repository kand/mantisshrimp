
from mantisshrimp.domain.DomainObject import *

class Term(DomainObject):
    '''
    Terms are used to store information on possible locations. Included are:
    - the actual term used for the location search
    - the probability this term is actually a location
    - information on the location associated with this term
    - terms that probably better describe the location of this term
    - documents this term is found in
    '''

    COLLECTION_NAME = 'terms'

    def __init__(self):
        DomainObject.__init__(self)
        
        # raw input term used for geolocation
        self.raw_term = ''
        # likelyhood that this location is correct
        self.likelyhood = 0.5
        # geocoder domain
        self.geocoder_domain = ''
        # true if geocoder has successfully located this term
        self.success = False
        # a string representing the place name returned by the geocoder
        self.place = ''
        # coordinates of given term
        self.coords = ()
        # failure message if geocoder has failed to locate this term
        self.fail_message = ''
        # a list of terms that can probably be better used to describe it
        self.more_likely_terms = []
        # a list of documents this term is included in
        self.documents = []
