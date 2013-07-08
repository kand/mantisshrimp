import geopy, json

class GeocoderResult(object):

    def __init__(self, geocoder = geopy.geocoders.GoogleV3):
        # class properties init 
        self.geocoder = geocoder()
        self.raw_place = None
        self.place = None
        self.coords = None
        self.success = False
        self.fail_message = ''

    def find(self, location,
             print_exception = False,
             geocoder = None):
        '''
        Populate instance with data from geocoder using given location.
        '''

        # make sure geocoder is set
        if geocoder is None:
            geocoder = self.geocoder

        self.raw_place = location
        
        try:
            # use geocoder to find data
            geocode_result = self.geocoder.geocode(location)

            # no exceptions, set class variables
            self.success = True
            self.place = geocode_result[0]
            self.coords = geocode_result[1]
            
        except Exception as e:
            # a failure occured, set variables as necessary
            self.fail_message = e
            if print_exception:
                print('Tried "%s" and failed: %s' %(location, e))

        return self

    def __str__(self):
        return self.__repr__

    def __repr__(self):
        return str({
            "success": 1 if self.success else 0,
            "raw_place": self.raw_place,
            "place": self.place,
            "coords": self.coords,
            "fail_message": self.fail_message,
            "geocoder_domain": self.geocoder.domain
            })

