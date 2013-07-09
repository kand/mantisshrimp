
from mantisshrimp.domain.DomainObject import *

class Document(DomainObject):
    '''
    Documents are used to store information on a particular piece of text that
    has location information within it. This location information can probably
    be used to assign one or many locations to this document.
    '''

    COLLECTION_NAME = 'documents'

    def __init__(self):
        DomainObject.__init__(self)
        
        # source this document was taken from
        self.source = ''
        # direct link to this document
        self.href = ''
        # stripped content used to search for terms
        self.stripped_content = ''
        # terms used to describe location of this document
        self.terms = []
        # probability this document has the right locations singled out
        self.likelyhood = 0.5
