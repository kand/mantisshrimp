import json

class CustomJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        json_dict = None

        # get dictionary to turn into json
        if hasattr(obj, 'toDict'):
            json_dict = obj.toDict()
        else:
            json_dict = json.JSONEncoder.default(self, obj)
                
        return json_dict
