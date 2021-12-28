import json
import requests


URL = "http://127.0.0.1:8001/myapp/studentdetail/"

# Send the request through get method to read the data

def get_data(id = None):
    data = {}
    if data is not None:
        data = {'id':id}
        print(data)
    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.get(url=URL,headers= headers,data= json_data)
    print(r)
    # extract the data in json format
    data = r.json()
    print(data)

get_data(1)

# Send the request through post method to insert the data
def post_data():
    data = {'name':'Elon',
        'roll':28,
        'city':'California'}

    
    # Convert the python data into json data
    json_data = json.dumps(data)
    print(json_data)

    # Send the data through request  post method to create the model instance
    # Also this request gets some response in form of data,which is stored in r
    headers = {'content-type':'application/json'}
    r = requests.post(url = URL,headers= headers,data = json_data)

    print(r)
    # Extract the data in json format
    data = r.json()
    print(data)

#post_data()

# Send the request through patch method to partial update the data
def partial_update_data():
    data = {'id':9,
            'name':'Jack',
            'city':'London'}
    
    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.patch(url=URL,headers= headers,data = json_data)
    print(r)
    response = r.json()
    print(response)


#partial_update_data()

# Send the request through put method to update the data
def complete_update_data():
    data = {'id':10,
            'name':'Jack',
            'roll': 15,
            'city':'London'}
    
    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.put(url=URL,headers= headers,data = json_data)
    print(r)
    response = r.json()
    print(response)


#complete_update_data()

# Send the request through delete method to delete the data
def delete_data():
    data = {'id':8}
    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.delete(url= URL,headers=headers,data = json_data)
    data = r.json()
    print(data)

#delete_data()