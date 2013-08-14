from py2neo import neo4j, node, rel

from mantisshrimp.domain.Article import Article as DomainArticle
from mantisshrimp.domain.Term import Term as DomainTerm
from mantisshrimp.domain.Location import Location as DomainLocation

class Neo4j(object):

    CONN_STR = "http://%s:%d/db/%s/"

    class Indexes():
        N_ARTICLES = "Articles"
        N_TERMS = "Terms"
        N_LOCATIONS = "Locations"
        R_RELATIONS = "Relations"

    class Relations():
        CONTAINS = "CONTAINS"
        LOCATIONS = "LOCATIONS"

    def __init__(self, host='localhost', port=7474, db_name='data'):

        # get connection
        self.conn = neo4j.GraphDatabaseService(self.CONN_STR % (host, port, db_name))

        # build indexes
        self.articles = self.conn.get_or_create_index(
            neo4j.Node,
            self.Indexes.N_ARTICLES
        )
        self.terms = self.conn.get_or_create_index(
            neo4j.Node,
            self.Indexes.N_TERMS
        )
        self.locations = self.conn.get_or_create_index(
            neo4j.Node,
            self.Indexes.N_LOCATIONS
        )
        self.relationships = self.conn.get_or_create_index(
            neo4j.Relationship,
            self.Indexes.R_RELATIONS
        )

    def findArticle(href):
        domain_article = None
        
        db_nodes = self.articles.get(DomainArticle.UNIQUE_ID, href)
        if len(db_nodes) > 0:
            props = db_nodes[0].get_properties()
            domain_article = DomainArticle()
            domain_article.href = props['href']
            domain_article.source = props['source']
            domain_article.stripped_content = props['stripped_content']

        return domain_article

    def find(self, index_type, key, value):

# TODO : this function sucks
        db_object = None

        try:
            if index_type is self.Indexes.N_ARTICLES:
                db_object = self.articles.get(key, value)
            elif index_type is self.Indexes.N_TERMS:
                db_object = self.terms.get(key, value)
            elif index_type is self.Indexes.N_LOCATIONS:
                db_object = self.locations.get(key, value)
            elif index_type is self.Indexes.R_RELATIONS:
                db_object = self.relationships.get(key, value)
        except Exception as e:
            print "Failed finding object in index '%s' with k,v = ('%s','%s')" \
                  % (index_type, key, value)
        
        return db_object

    def processNode(self, domain_object):
        
# TODO : this function sucks

        new_node = None
        
        if isinstance(domain_object, DomainArticle):
            new_node = self.articles.get_or_create(domain_object.UNIQUE_ID,
                                                   domain_object.href,
                                                   domain_object.toDict())
        elif isinstance(domain_object, DomainTerm):
            new_node = self.terms.get_or_create(domain_object.UNIQUE_ID,
                                                domain_object.raw_term,
                                                domain_object.toDict())
        elif isinstance(domain_object, DomainLocation):
            new_node = self.locations.get_or_create(domain_object.UNIQUE_ID,
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
        
        
