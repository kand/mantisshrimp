import bleach, bs4, nltk, operator, urllib2

from mantisshrimp.parsing_engine.GeocoderResult import *

class Document(object):

    def __init__(self, source, href):
        # class properties init
        self.source = source
        self.href = href
        self.html_content = ''
        self.stripped_content = ''
        self.search_terms = {}
        self.ordered_search_terms = []
        self.locations = []

    def grabContent(self, content_search_function):
        '''
        Open url provided at init time and attempt to grab content based
        on the given content_search_function.

        content_search function = a function that takes one argument, raw html
            to search through, and returns the block of html containing the text
            to perform the location search on.
        '''

        # open url and get html
        response = urllib2.urlopen(self.href)
        html = response.read()

        # use provided search function to find content containing locations
        self.html_content = content_search_function(html)

        return self

    def buildWordCollections(self):
        '''
        Build a word collection to perform location searches on. Uses the
        content property on this object.
        '''

        # make sure there is content to gather data from
        if len(self.html_content) < 1:
            print('There is no content to build word collection from!')
            return
        
        # clean up html out of content
        stripped_content = bleach.clean(self.html_content, tags=[], strip=True)
        
        # split up content into words
        all_words = ''.join(e for e in stripped_content \
                          if e.isalpha() or e.isspace() or e == '.').split()
        
        # search for proper nouns
        proper_nouns = {}
        for i in range(len(all_words)):
            word = all_words[i]
            if word[0].isupper():
                # consume as many capitalized words as possible to get full noun
                while word[-1] != '.' \
                      and i + 1 < len(all_words) \
                      and all_words[i + 1][0].isupper():
                    i += 1
                    word += ' ' + all_words[i]

                # remove periods at end of words
                if word[-1] == '.':
                    word = word[0:-1]

                # try to clean out words that are clearly not nouns
                if word.lower() not in nltk.corpus.stopwords.words('english'):
                    # add to count
                    if word in proper_nouns:
                        proper_nouns[word] += 1
                    else:
                        proper_nouns[word] = 1

        # get a list of proper nouns sorted by frequency
        by_freq = sorted(proper_nouns.iteritems(),
                         key=operator.itemgetter(1),
                         reverse=True)

        # set properties on class
        self.stripped_content = stripped_content
        self.search_terms = proper_nouns
        self.ordered_search_terms = by_freq

        return self
        
    def findLocations(self, num_locations_to_test):
        '''
        Search through ordered list of search terms up to
        num_locations_to_test and use a geocoder service to attempt to get
        lat/lng coordinates.
        '''

        # loop through search and access geocoder services to get lat/lng
        count = 0
        for kv in self.ordered_search_terms:
            
            # keep track of how many locations we've tested
            count += 1
            if count > num_locations_to_test:
                break

            location = kv[0]

            # test location using geocoder
            result = GeocoderResult(geopy.geocoders.GoogleV3()).find(location)
            self.locations.append(result)

        return self
