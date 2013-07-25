
from mantisshrimp.domain.DomainObject import *

class Location(DomainObject):
    '''
    Locations are used to store information on potential locations for terms.
    '''

    class Coordinate(object):
        '''
        Stores latitude/longitude information.
        '''
        
        def __init__(self, latitude, longitude):
            self.latitude = latitude
            self.longitude = longitude

    def __inti__(self):
        DomainObject.__init__(self)

        # domain of geocoder used to get this location
        self.geocoder_domain = ''
        # name of location
        self.place = ''
        # lat/lng of location
        self.coords = None
        
