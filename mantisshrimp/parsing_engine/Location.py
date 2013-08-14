import geopy

from mantisshrimp.domain.Location import Location as DomainLocation

class Location(DomainLocation):

    def __init__(self):
        DomainLocation.__init__(self)

    def buildFromNode(self, node):
        props = node.get_properties()
        for name in props:
            setattr(self, name, props[name])

        return self

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

# TODO : this method sucks, return self somehow
# TODO : having multiple results for one location is an error, will not
#   be tracked currently, this is incorrect behavior on my part

        try:
            # use geocoder to find data
# TODO : take multiple results and turn them all into lcoations
            geocode_result = ready_geocoder.geocode(location, exactly_one=False)

            # no exceptions, set class variables
            self.place = geocode_result[0][0]
            self.latitude = geocode_result[0][1][0]
            self.longitude = geocode_result[0][1][1]
            
        except Exception as e:
            # a failure occured, set variables as necessary
            fail_message = str(e)

        return fail_message
