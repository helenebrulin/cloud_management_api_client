import rest_client as rest_client
import config as config
import json

API_BASE_URL = config.API_BASE_URL
API_KEY = config.API_KEY
API_SECRET_KEY = config.API_SECRET_KEY


print("# DELETE SUB #")


#subscription deletion
subId = find_subscription(subName)
url = API_BASE_URL + "/subscriptions/{0}".format(subId)
task = rest_client.delete(url, API_KEY, API_SECRET_KEY)
print(task)