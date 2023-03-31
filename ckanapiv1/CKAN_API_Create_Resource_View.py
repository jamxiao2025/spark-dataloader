import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
my_API_KEY = os.getenv("API_KEY")
resource_id = ''
# put the details of the dataset we're going to create into a dict
resource_dict = {
    'resource_id': resource_id,
    'title': 'covid average cases value resource',
    'description': "covid resource view",
    'view_type': 'recline_view'
}

# use the json module to dump the dictionary to a string for posting, encoding the URL
# creating a dataset requires an authorization header
headers = {
    'Authorization': my_API_KEY,
    #'Content-Type': 'multipart/form-data'
}
# we'll use the package_create function to create a new dataset.
url = 'http://data.buspark.io/api/3/action/resource_view_create'
#ckan.logic.action.update.resource_view_update(
# making HTTP request 
response = requests.post(url, data=resource_dict, headers=headers)

# use the json module to load CKAN's response into a dictionary
response_dict = response.json()
print(response_dict)


