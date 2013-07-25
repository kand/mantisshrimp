
from mantisshrimp.domain.DomainObject import *

class Location(DomainObject):
    '''
    Locations are used to store information on potential locations for terms.
    '''

    def __init__(self):
        DomainObject.__init__(self)

        # domain of geocoder used to get this location
        self.geocoder_domain = ''
        # name of location
        self.place = ''
        # latitude of location
        self.latitude = 0.0
        # logitude of location
        self.logitude = 0.0
        
