import requests
import json
from dotenv import load_dotenv
import os 
load_dotenv()
my_API_KEY = os.getenv("API_KEY")
# grab resource_id
resource_id = 'ddc36b3a-b39d-49a7-b503-352f404cdcf5'

# put the details of the dataset we're going to create into a dict
resource_dict = {
    'id': resource_id
}

# use the json module to dump the dictionary to a string for posting, encoding the URL
# creating a dataset requires an authorization header
headers = {
    'Authorization': my_API_KEY,
    #'Content-Type': 'multipart/form-data'
}
# we'll use the package_create function to create a new dataset.
url = 'http://data.buspark.io/api/3/action/resource_delete'
#ckan.logic.action.update.resource_view_update(
# making HTTP request 
response = requests.post(url, data=resource_dict, headers=headers)

# use the json module to load CKAN's response into a dictionary
response_dict = response.json()
print(response_dict)


