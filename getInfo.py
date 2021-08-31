import rest_client as rest_client
import config as config

API_BASE_URL = config.API_BASE_URL
API_KEY = config.API_KEY
API_SECRET_KEY = config.API_SECRET_KEY
line = "-" * 10


print("## Logs ##")
logs = rest_client.get(API_BASE_URL + "/logs", API_KEY, API_SECRET_KEY)
print(logs)

print(line)

print("## Payment methods ##")
pmethods = rest_client.get(API_BASE_URL + "/payment-methods", API_KEY, API_SECRET_KEY)
print(pmethods)

print(line)

print("## Cloud accounts ##")
accounts = rest_client.get(API_BASE_URL + "/cloud-accounts", API_KEY, API_SECRET_KEY)
print(accounts)

print(line)
