import geopy

from mantisshrimp.domain.Location import Location as DomainLocation

class Location(DomainLocation):

    def __init__(self):
        DomainLocation.__init__(self)

    def resolve(self, location, geocoder):
        '''
        Resolve location with a geocoder. Returns a failure message if
        something went wrong, otherwise returns None.
        '''

        # this will stay as None if geocoding was successful
        fail_message = None

        # prepare geocoder
        ready_geocoder = geocoder()
        self.geocoder_domain = ready_geocoder.domain

# TODO : search db for this location, allow skip over geocoding

        try:
            # use geocoder to find data
            geocode_result = ready_geocoder.geocode(location)

            # no exceptions, set class variables
            self.place = geocode_result[0]
            self.coords = DomainLocation.Coordinate(geocode_result[0][0],
                                                    geocode_result[0][1])
            
        except Exception as e:
            # a failure occured, set variables as necessary
            fail_message = str(e)

        return fail_message
