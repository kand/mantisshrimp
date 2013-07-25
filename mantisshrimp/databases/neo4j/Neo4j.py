from py2neo import neo4j, node, rel

class Neo4j(object):

    def __init__(self):

# TODO : put stuff in app settings
        HOST = "localhost"
        PORT = 7474
        DB_NAME = "data"
        
        self.conn = neo4j.GraphDatabaseService("http://%s:%d/db/%s/" \
                                                % (HOST, PORT, DB_NAME))

    def saveNode(self, domain_object):
        new_node = self.conn.create(domain_object.toDict())
        return new_node

    def saveRelation(self, node1, node2, relation_object):

# TODO : remove node arguments
        
        new_relation = self.conn.create(rel((node1,
                                         relation_object.name,
                                         node2,
                                         {"likelyhood": relation_object.likelyhood}))) 
        return new_relation
        
        
