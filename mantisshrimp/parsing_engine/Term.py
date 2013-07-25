import geopy

from mantisshrimp.domain.ProbabilityRelation import *
from mantisshrimp.domain.Term import Term as DomainTerm
from mantisshrimp.parsing_engine.Location import *

class Term(DomainTerm):

    def __init__(self):
        DomainTerm.__init__(self)

    def find(self, location, geocoder):
        '''
        Populate instance with data from geocoder using given location.
        '''
        
        # set raw term
        self.raw_term = location

# TODO : search db for this term, allow us to skip over geocoding
               
        geocoded_location = Location()
        failed = geocoded_location.resolve(location, geocoder)
        if not failed:
            # successfully geocoded, add a relationship
            self.success = True
            relationship = ProbabilityRelation(self, geocoded_location)
            self.relationships.append(relationship)
        else:
            self.fail_message = failed
# TODO : logging here
            print "Given location '" + location + "' was not resolved."

        return self
