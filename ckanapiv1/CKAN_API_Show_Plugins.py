import requests

# API endpoint to get CKAN status
url = 'http://data.buspark.io/api/3/action/status_show'

# send GET request to get CKAN status
response = requests.get(url)

# extract the list of installed plugins from the CKAN status response
plugins = response.json()
print(plugins)