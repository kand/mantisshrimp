import feedparser

from mantisshrimp.parsing_engine import ContentSearchFunctions
from mantisshrimp.parsing_engine.Document import *

SOURCE = 'http://news.yahoo.com/rss/us'
MAX_ARTICLES = 10
MAX_LOCATIONS_TO_SEARCH = 4

# get sample data
feed = feedparser.parse(SOURCE)

# search each entry in feed up to given amount
docs = []
articles_searched = 0
for i in range(len(feed.entries)):
    
    entry = feed.entries[i]

    # check if we should be done
    articles_searched += 1
    if articles_searched > MAX_ARTICLES:
        break

    # build document info
    doc = Document(SOURCE, entry.link)
    doc \
        .grabContent(ContentSearchFunctions.yahoo) \
        .buildWordCollections() \
        .findLocations(MAX_LOCATIONS_TO_SEARCH)

    docs.append(doc)

# write locations out
