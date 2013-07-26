
from mantisshrimp.domain.DomainObject import *

class Location(DomainObject):
    '''
    Locations are used to store information on potential locations for terms.
    '''

    def __init__(self):
        DomainObject.__init__(self)

        # name of location, should be unique identifier of a Location
        self.place = ''
        # domain of geocoder used to get this location
        self.geocoder_domain = ''
        # latitude of location
        self.latitude = 0.0
        # logitude of location
        self.logitude = 0.0

        self.key_name = 'place'
