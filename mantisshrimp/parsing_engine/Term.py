import geopy

from mantisshrimp.domain.ProbabilityRelation import *
from mantisshrimp.domain.Term import Term as DomainTerm
from mantisshrimp.parsing_engine.Location import *

class Term(DomainTerm):

    def __init__(self):
        DomainTerm.__init__(self)

    def buildFromNode(self, node):
        '''
        Set properties from a node.
        '''
        
        props = node.get_properties()

        self.id = node._id
        self.raw_term = props['raw_term']
        self.fail_message = props['fail_message']
        self.likelyhood = props['likelyhood']

        # try to get locations this may be already associated with
        location_nodes = term_node.match("LOCATION")
        for location_node in location_nodes:
            location = Location().buildFromNode(location_node)
            self.relationships.append(
                ProbabilityRelation(self, location, "LOCATION"))
            
        return self

    def find(self, location, geocoder, db_conn):
        '''
        Populate instance with data from geocoder using given location.
        '''

        # check db to see if this term has already been created
        term_nodes = db_conn.find("Terms", "raw_term", location)
        if len(term_nodes) > 0:
            term_node = term_nodes[0]
            self.buildFromNode(term_node)
            #return self
        
        # set raw term
        self.raw_term = location
               
        geocoded_location = Location()
        failed = geocoded_location.resolve(location, geocoder)
        if not failed:
            # Double check here that the location doesn't exist already in
            #   db. This way relationships can be build appropriately.
            location_nodes = db_conn.find("Locations", "place",
                                          geocoded_location.place)
            if location_nodes and len(location_nodes) > 0:
                location_node = location_nodes[0]
                geocoded_location = Location().buildFromNode(location_node)

            # successfully geocoded, add a relationship
            relationship = ProbabilityRelation(self, geocoded_location,
                                               "LOCATION")
            self.relationships.append(relationship)
        else:
            self.fail_message = failed
# TODO : logging here
            print "Given location '" + location + "' was not resolved: " + failed

        return self
