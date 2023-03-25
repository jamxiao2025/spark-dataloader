import requests

# guide to uploading files 
# Uploading:
#   open file
#   stream content 
# These two processes are achievable with the open() function
# open(a,b)
#   a: path of file
#   b: mode 
#       rb = read binary
# Note: it's important to read the file in binary mode. The requests library typically determines the Content-Length header, which is a value in bytes. If the file is not read in bytes mode, the library may get an incorrect value for Content-Length, which would cause errors during file submission.
#For this tutorial, we'll make requests to the free httpbin service. This API allows developers to test their HTTP requests. Let's create a variable that stores the URL we'll post our files to:
#https://www.w3schools.com/python/ref_requests_post.asp good for looking at possible post parameters and requirements
test_url = "http://demo.ckan.org/api/3/action/group_list"
test_response = requests.post(test_url, data={}) #files takes a dictionary, the key is the name of the form field that accepts the file. The value is the bytes of the opened file that you want to read
test_response_dict = test_response.json() #equivalent to response_dict = json.loads(response.read())
if test_response.ok:
    print("Upload completed successfully!")
    print(test_response_dict)
else:
    print("Something went wrong!")
