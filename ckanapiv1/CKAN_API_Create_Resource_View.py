import requests
import json

# grab resource_id
resource_id = '7bc8100e-5c5b-4e78-8c62-bbd99bd69624'
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
    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjV1c2WUcwQmJNYXYyanE1clBQeEZjVWZNRjB2emVmTWF1a19laUZ4bDJjIiwiaWF0IjoxNjc3ODI2NzAyfQ.7ivzMXrnyDsjFa9ZF6QMI73TqpAZgYoaxFzIZQlXj7I',
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


