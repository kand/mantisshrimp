
from mantisshrimp.domain.DomainObject import *

class Article(DomainObject):
    '''
    Article are used to store information on a particular piece of text that
    has location information within it. This location information can probably
    be used to assign one or many locations to this document.
    '''

    def __init__(self):
        DomainObject.__init__(self)

        # direct link to this article, should be unique identifier of this Article
        self.href = ''
        # source this article was taken from
        self.source = ''
        # stripped content used to search for terms
        self.stripped_content = ''

        self.key_name = 'href'
