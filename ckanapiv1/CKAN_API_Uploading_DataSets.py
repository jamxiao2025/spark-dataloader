import requests
import json
from dotenv import load_dotenv
import os 

load_dotenv()
my_API_KEY = os.getenv("API_KEY")
# put the details of the dataset we're going to create into a dict
dataset_dict = {
    'name': 'new_ds',
    'notes': 'Hoping the url changes for resources',
    'owner_org': 'buspark'
}

# use the json module to dump the dictionary to a string for posting, encoding the URL
data_string =json.dumps(dataset_dict)

# creating a dataset requires an authorization header
headers = {
    'Authorization': my_API_KEY,
    'Content-Type': 'application/json'
    }
# we'll use the package_create function to create a new dataset.
url = 'http://data.buspark.io/api/action/package_create'

# making HTTP request 
response = requests.post(url, data=data_string, headers=headers)

# use the json module to load CKAN's response into a dictionary
response_dict = response.json()
print(response_dict)
# package_create returns the created package as a result
created_package = response_dict['result']
print(created_package)

