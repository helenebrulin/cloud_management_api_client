# Access cloud management API

# config.py
```py
API_BASE_URL= 'https://api.redislabs.com/v1' / 'https://api-beta.redislabs.com/beta1'
API_KEY= 'global account key'
API_SECRET_KEY= 'my secret key'
```

# Usage
```sh
python3 tests.py
```

# Info about calls
- Task status : A 'create subscription' call will return a task id. The task id can be used to check if the task was already completed (e.g., processing or completed).

# Notes:
- troubleshoot certificate error : https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org # cloud_management_api_client
