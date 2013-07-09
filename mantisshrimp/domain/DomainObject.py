
class DomainObject(object):
    '''
    DomainObject is the base for all other objects in this domain.
    '''

    COLLECTION_NAME = None

    def __init__(self):
        # unique id for this domain object
        self._id = ''

    def toDict(self):
        return self.__dict__

