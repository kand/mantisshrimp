import oauth2, requests, time

input_text = 'testing new york city, testing'

APP_ID = 'GkY6za70'
PUBLIC_KEY = 'dj0yJmk9TTg2TmNjUUNjbk1uJmQ9WVdrOVIydFpObnBoTnpBbWNHbzlNVGc0TWpJeU1UWTJNZy0tJnM9Y29uc3VtZXJzZWNyZXQmeD02NA--'
PRIVATE_KEY = '4eb1dcfb62a47801855813ecdca921a963ffcb67'

if len(input_text) > 0:
    # set up oauth for YBOSS
    RESOURCE_URL = 'http://yboss.yahooapis.com/geo/placespotter'
    yboss_url = RESOURCE_URL

    # make request to YBOSS to parse text for location info
    
    METHOD = 'PUT'
    consumer = oauth2.Consumer(key=PUBLIC_KEY,secret=PRIVATE_KEY)
    params = {
        'oauth_version': '1.0',
        'oauth_nonce': oauth2.generate_nonce(),
        'oauth_timestamp': int(time.time())
    }
    oauth_request = oauth2.Request(method=METHOD, url=RESOURCE_URL, parameters=params)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, None)
    oauth_header = oauth_request.to_header(realm='yahooapis.com')

    data = {
        'appId': APP_ID,
        'documentType': 'text/plain',
        'documentContent': input_text
    }
    for k in oauth_request:
        data[k] = oauth_request[k]
    
    headers = {
        #'Content-Type': 'multipart/form-data'
    }
    for k in oauth_header:
        headers[k] = oauth_header[k]
    resp = requests.put(yboss_url, data=data, headers=headers)
else:
    print('No value given for input_text')

