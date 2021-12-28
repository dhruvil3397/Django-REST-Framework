# Create Separate / Third-party application 
# import requests package
import requests

# Write the URL, where you want to send request
URL = "http://127.0.0.1:8000/myapp/studentlist/"

# Send the request through GET method to read the data
r = requests.get(url=URL)
# We will store the response in the object r
print(r)
# Extract the data in json format
data = r.json()
print(data)


# This Third-party application  communicate with th API, and collect the data