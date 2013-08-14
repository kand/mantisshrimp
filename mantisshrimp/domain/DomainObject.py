
class DomainObject(object):
    '''
    DomainObject is the base for all other objects in this domain.
    '''

    # name of the field used as a unique key, defaults to id
    UNIQUE_ID = 'id'

# TODO : this put likelyhood default in app settings

    def __init__(self):
        
        # unique id for this domain object
        self.id = ''
        # a probabilistic measure that this object is correct
        self.likelyhood = 0.5
        # relationships with other domain objects
        self.relationships = []

    def toDict(self):
        ret_dict = self.__dict__.copy()

        # remove properties we don't need to save
        ret_dict.pop('relationships', None)
        ret_dict.pop('key_name', None)
        
        # remove id string if it's empty
        if 'id' in ret_dict and len(str(ret_dict['id']).strip()) < 1:
            ret_dict.pop('id', None)
        
        return ret_dict

