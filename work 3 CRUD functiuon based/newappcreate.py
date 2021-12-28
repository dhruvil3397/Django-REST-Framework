import requests
import json

URL = "http://127.0.0.1:8001/myapp/studentcreate/"
data = {'name':"Elon",
        'roll':28,
        "city":"California"}

# Convert the python data into json data
json_data = json.dumps(data)
print(json_data)

# Send the data through request  post method to create the model instance
# Also this request gets some response in form of data,which is stored in r
r = requests.post(url = URL,data = json_data)

print(r)
# Extract the data in json format
data = r.json()
print(data)


# This Third-party application  communicate with th API, and collect the data
