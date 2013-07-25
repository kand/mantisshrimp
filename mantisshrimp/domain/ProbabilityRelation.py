
from mantisshrimp.domain.DomainObject import *

class ProbabilityRelation(DomainObject):
        '''
        Relationship between two domain objects representing the probability
        of their relationship being true.
        '''

        def __init__(self, object1, object2):
            # first object in the relation
            self.object1 = object1
            # second object in the relation
            self.object2 = object2
