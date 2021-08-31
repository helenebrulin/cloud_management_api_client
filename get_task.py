import rest_client as rest_client
import config as config
import json

API_BASE_URL = config.API_BASE_URL
API_KEY = config.API_KEY
API_SECRET_KEY = config.API_SECRET_KEY

task_id = 1

#task status
print("# GET TASKS #")

task = rest_client.get(API_BASE_URL + "/tasks/" + task_id, API_KEY, API_SECRET_KEY)
tjson = json.loads(task)
status = tjson['status']
print(task)
