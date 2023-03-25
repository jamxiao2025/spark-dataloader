import requests
urlsrc = 'https://github.com/BU-Spark/summer2021internship/blob/master/State%20Surplus/parcel-geoData.csv'
rsrc = requests.get(urlsrc)
print(rsrc.content)
