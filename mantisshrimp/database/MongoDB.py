import json

from pymongo import MongoClient

from mantisshrimp.database.Database import Database
from mantisshrimp.utils.CustomJSONEncoder import CustomJSONEncoder

# TODO : replace stuff with app settings

class MongoDB(Database):

    def __init__(self):
        Database.__init__(self)

        self.connection = MongoClient('localhost', 27017)
        self.database = self.connection['mantisshrimp-test']

    def insert(self, domain_object):
        # get collection to insert into
        collection = self.database.collection[domain_object.COLLECTION_NAME]

        # create a json string with the dict _id property removed
        domain_dict = domain_object.toDict().copy()
        domain_dict.pop('_id', None)
        json_str = json.dumps(domain_dict, cls = CustomJSONEncoder)

        # insert the object
        _id = collection.insert(json_str)

        # set id on domain object
        domain_object._id = _id
