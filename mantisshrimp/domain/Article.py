
from mantisshrimp.domain.DomainObject import *

class Article(DomainObject):
    '''
    Article are used to store information on a particular piece of text that
    has location information within it. This location information can probably
    be used to assign one or many locations to this document.
    '''

    def __init__(self):
        DomainObject.__init__(self)
        
        # source this article was taken from
        self.source = ''
        # direct link to this article
        self.href = ''
        # stripped content used to search for terms
        self.stripped_content = ''
