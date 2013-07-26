from py2neo import neo4j, node, rel

from mantisshrimp.domain.Article import Article as DomainArticle
from mantisshrimp.domain.Term import Term as DomainTerm
from mantisshrimp.domain.Location import Location as DomainLocation

class Neo4j(object):

    def __init__(self):

# TODO : put stuff in app settings
        HOST = "localhost"
        PORT = 7474
        DB_NAME = "data"
        
        self.conn = neo4j.GraphDatabaseService("http://%s:%d/db/%s/" \
                                                % (HOST, PORT, DB_NAME))

        # build indexes
        self.articles = self.conn.get_or_create_index(neo4j.Node, "Articles")
        self.terms = self.conn.get_or_create_index(neo4j.Node, "Terms")
        self.locations = self.conn.get_or_create_index(neo4j.Node, "Locations")
        self.relationships = self.conn.get_or_create_index(neo4j.Relationship,
                                                           "Relations")

    def processNode(self, domain_object):
        
# TODO : this function sucks

        new_node = None
        
        if isinstance(domain_object, DomainArticle):
            new_node = self.articles.get_or_create(domain_object.key_name,
                                                   domain_object.href,
                                                   domain_object.toDict())
        elif isinstance(domain_object, DomainTerm):
            new_node = self.terms.get_or_create(domain_object.key_name,
                                                domain_object.raw_term,
                                                domain_object.toDict())
        elif isinstance(domain_object, DomainLocation):
            new_node = self.locations.get_or_create(domain_object.key_name,
                                                   domain_object.place,
                                                   domain_object.toDict())
    
        return new_node

    def processRelation(self, node1, node2, relation_object):

# TODO : remove node arguments, this fuction sucks

        uid = str(node1._id) + '-' + relation_object.name + '-' + str(node2._id)
        
        new_rel = self.relationships.get_or_create(
            'uid',
            uid,
            (
                node1,
                relation_object.name,
                node2,
                {
                    'uid': uid,
                    'likelyhood': relation_object.likelyhood
                }
            )
        )

        return new_rel
        
        
