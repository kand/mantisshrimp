import geopy, json

from mantisshrimp.utils.CustomJSONEncoder import *

from mantisshrimp.domain.Term import Term as DomainTerm

class Term(DomainTerm):

    def __init__(self):
        DomainTerm.__init__(self)

    def find(self, location, geocoder, print_exception = False):
        '''
        Populate instance with data from geocoder using given location.
        '''
        
        # set raw term
        self.raw_term = location

# TODO : search db for this term, allow us to skip over geocoding

        # prepare geocoder
        ready_geocoder = geocoder()
        self.geocoder_domain = ready_geocoder.domain
        
        try:
            # use geocoder to find data
            geocode_result = ready_geocoder.geocode(location)

            # no exceptions, set class variables
            self.success = True
            self.place = geocode_result[0]
            self.coords = geocode_result[1]
            
        except Exception as e:
            # a failure occured, set variables as necessary
            self.fail_message = str(e)
            if print_exception:
                print('Tried "%s" and failed: %s' % (location, e))

        return self
