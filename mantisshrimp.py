import feedparser, geopy

from py2neo import neo4j

from mantisshrimp.databases.neo4j.Neo4j import *
from mantisshrimp.parsing_engine import ContentSearchFunctions
from mantisshrimp.parsing_engine.Article import *

SOURCE = 'http://news.yahoo.com/rss/us'
MAX_ARTICLES = 10
MAX_LOCATIONS_TO_SEARCH = 5

# get sample data
feed = feedparser.parse(SOURCE)

# search each entry in feed up to given amount
db = Neo4j()
docs = []
articles_searched = 0
for i in range(len(feed.entries)):
    
    entry = feed.entries[i]

    # check if we should be done
    articles_searched += 1
    if articles_searched > MAX_ARTICLES:
        break

    # build document info
    doc = Article(SOURCE, entry.link)
    doc.digest(ContentSearchFunctions.yahoo,
               MAX_LOCATIONS_TO_SEARCH,
               geopy.geocoders.GoogleV3,
               db)

    docs.append(doc)

# TODO : save docs to database
def saveDomainObjectAndRelations(obj):
    node1 = db.processNode(obj)
    obj.id = node1._id
    for rel in obj.relationships:
        node2 = saveDomainObjectAndRelations(rel.object2)
        db_rel = db.processRelation(node1, node2, rel)
        rel.id = db_rel._id
    return node1

for doc in docs:
    saveDomainObjectAndRelations(doc)

# TODO: start a flask webservice to allow results to be viewed
#from mantisshrimp.webservice import app
#app.run(host='localhost', port=5000)
