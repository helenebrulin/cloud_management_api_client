import rest_client as rest_client
import config as config

API_BASE_URL = config.API_BASE_URL
API_KEY = config.API_KEY
API_SECRET_KEY = config.API_SECRET_KEY

#get logs
logs = rest_client.get(API_BASE_URL + "/logs", API_KEY, API_SECRET_KEY)
print(logs)

'''
#task status
task = rest_client.get(API_BASE_URL + "/tasks/" + task_id, API_KEY, API_SECRET_KEY)
tjson = json.loads(task)
status = tjson['status']

#subscription creation
data = { "name" : name,
"paymentMethodId" : find_payment_method(),
"cloudProviders" : {
"cloudAccountId" : find_cloud_account("EDU"),
"regions" : [
 {"region" : region, "networking" : { "deploymentCIDR": cidr}}
 ]
 },
"databases" : [{"name" : db_name, "memoryLimitInGb" : db_size }]
 }
task = rest_client.post(API_BASE_URL + "/subscriptions", data, API_KEY, API_SECRET)

#database deletion
subId = find_subscription(subName)
dbId = find_db(subName, dbName)
url = API_BASE_URL + "/subscriptions/{0}/databases/{1}".format(subId, dbId)
task = rest_client.delete(url, API_KEY, API_SECRET_KEY)

#subscription deletion
subId = find_subscription(subName)
url = API_BASE_URL + "/subscriptions/{0}".format(subId)
task = rest_client.delete(url, API_KEY, API_SECRET_KEY)
'''
