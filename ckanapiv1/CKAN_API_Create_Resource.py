import requests
import json
from dotenv import load_dotenv
import os 
load_dotenv()
my_API_KEY = os.getenv("API_KEY")
# read our file in bytes because of requests library functionality
csv_file = open("data.csv", "rb")

package_id = 'd0a61c19-3ca8-4247-8440-79d9dc2f174d'
# 
#189a11f0-5500-4984-9b02-ae97c619cd7f
# put the details of the dataset we're going to create into a dict

resource_dict = {
    'package_id': package_id,
    'name': 'test_resourcev3',
    'description': 'New resource with working url (hopefully)',
}

# use the json module to dump the dictionary to a string for posting, encoding the URL
# creating a dataset requires an authorization header
headers = {
    'Authorization': my_API_KEY,
    #'Content-Type': 'multipart/form-data'
}
# we'll use the package_create function to create a new dataset.
url = 'http://data.buspark.io/api/3/action/resource_create'

# making HTTP request 
response = requests.post(url, data=resource_dict, headers=headers, files={"upload":csv_file})

# use the json module to load CKAN's response into a dictionary
response_dict = response.json()
print(response_dict)


