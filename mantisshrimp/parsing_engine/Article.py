import bleach, bs4, json, nltk, operator, urllib2

from mantisshrimp.domain.ProbabilityRelation import *
from mantisshrimp.parsing_engine.Term import *

from mantisshrimp.domain.Article import Article as DomainArticle

class Article(DomainArticle):

    def __init__(self, source, href):
        DomainArticle.__init__(self)
        
        self.source = source
        self.href = href
        
    def digest(self, content_search_function, num_locations_to_test, geocoder):
        '''
        Open url provided at init time and attempt to grab content based
        on the given content_search_function.

        Then, build a word collection to perform location searches on. Uses the
        content property on this object.

        content_search function = a function that takes one argument, raw html
            to search through, and returns the block of html containing the text
            to perform the location search on.

        num_locations_to_test = the maximum number of locations to test against
            the geocoder.

        geocoder = the geocoder object to use to test locations.
        '''

        # open url and get html
        response = urllib2.urlopen(self.href)
        html = response.read()

        # use provided search function to find content containing locations
        html_content = content_search_function(html)

        # make sure there is content to gather data from
        if len(html_content) < 1:
            print('There is no content to build word collection from!')
            return
        
        # clean up html out of content
        stripped_content = bleach.clean(html_content,
                                        tags=[],
                                        attributes=[],
                                        styles=[],
                                        strip=True)
        
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

        # loop through search and access geocoder services to get lat/lng
        count = 0
        for kv in by_freq:
            
            # keep track of how many locations we've tested
            count += 1
            if count > num_locations_to_test:
                break

            location = kv[0]

            # test location using geocoder
            term = Term()
            term.find(location, geocoder)
            relationship = ProbabilityRelation(self, term)
            self.relationships.append(relationship)

        return self

