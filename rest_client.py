import urllib.request as http
import json

# Pretty print JSON
def json_pp(data):
    j = {}
    if not type(data) is dict:
        j = json.loads(data)
    else:
        j = data

    jstr = json.dumps(j, indent=4, sort_keys=True)

    return jstr


# Get a resource by providing the response as string
def get(url, api_key, api_secret_key):

    req = http.Request(url)
    req.add_header('x-api-key', api_key)
    req.add_header('x-api-secret-key', api_secret_key)
    resp = http.urlopen(req)

    return json_pp(resp.read())


# Post data to a resource by providing the response as string
def post(url, data_obj, api_key, api_secret_key):

    data = json.dumps(data_obj).encode('utf-8')

    req = http.Request(url)
    req.add_header('x-api-key', api_key)
    req.add_header('x-api-secret-key', api_secret_key)
    req.add_header('Content-Type', 'application/json')

    #Passing data turns this into a POST
    resp = http.urlopen(req, data)

    return json_pp(resp.read())


# Get a resource by providing the response as string
def delete(url, api_key, api_secret_key):

    req = http.Request(url)
    req.method = 'DELETE'
    req.add_header('x-api-key', api_key)
    req.add_header('x-api-secret-key', api_secret_key)
    resp = http.urlopen(req)

    return json_pp(resp.read())