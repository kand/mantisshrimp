import geopy

class GeocoderResult(object):

    def __init__(self, geocoder):
        # class properties init 
        self.geocoder = geocoder
        self.place = None
        self.coords = None
        self.success = False
        self.fail_message = None

    def find(self, location, print_exception=False):
        '''
        Populate instance with data from geocoder using given location.
        '''
        
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
        return str(self.success) + ','\
               + str(self.place) + ',' \
               + str(self.coords) + ',' \
               + str(self.fail_message) + ',' \
               + str(self.geocoder)

    def __repr__(self):
        return self.__str__()
