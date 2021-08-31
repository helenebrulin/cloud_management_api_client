import rest_client as rest_client
import config as config

API_BASE_URL = config.API_BASE_URL
API_KEY = config.API_KEY
API_SECRET_KEY = config.API_SECRET_KEY
line = "-" * 10


#subscription creation
data = {
    "name": "helene-ex",
    "paymentMethodId": 9605,
    "cloudProviders": [
      {
        "cloudAccountId": 1,
        "regions": [
          {
            "region": "us-east-1",
            "networking": {
              "deploymentCIDR": "10.10.1.0/24"
            }
          }
        ]
      }
    ],
    "databases": [
      {
        "name": "Redis-database-example",
        "memoryLimitInGb": 1
      }
    ]
}

task = rest_client.post(API_BASE_URL + "/subscriptions", data, API_KEY, API_SECRET_KEY)
print(task)

#task status
print("# GET TASKS #")

task = rest_client.get(API_BASE_URL + "/tasks/", API_KEY, API_SECRET_KEY)
#tjson = json.loads(task)
#status = tjson['status']
print(task)


