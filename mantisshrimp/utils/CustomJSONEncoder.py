import json

class CustomJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if hasattr(obj, 'toDict'):
            return obj.toDict()
        else:
            return json.JSONEncoder.default(self, obj)
