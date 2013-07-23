
class DomainObject(object):
    '''
    DomainObject is the base for all other objects in this domain.
    '''

    COLLECTION_NAME = None

    def __init__(self):
        # unique id for this domain object
        self._id = ''

    def toDict(self):
        ret_dict = self.__dict__.copy()
        
        # remove _id string if it's empty
        if '_id' in ret_dict and len(ret_dict['_id'].strip()) < 1:
            ret_dict.pop('_id', None)
        
        return ret_dict

