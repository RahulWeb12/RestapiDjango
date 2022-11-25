import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# --------------------------------------------------------------------
# Read the data
def get_data(id=None):
    data = {}
    herders={'content-Type':'application/json'}
    
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    # r = requests.get(url=URL, data=json_data)
    r = requests.get(url = URL, headers=herders ,data = json_data)
    data = r.json()
    print(data)

get_data()

# --------------------------------------------------------------------
# write a Post method (create data)
def post_data():
    data = {'name': 'Kajal Kumari',
            'roll': 104,
            'city': 'Goa'
            }
        
    herders={'content-Type':'application/json'}

 # my data is dictionary form then change to json formate
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=herders ,data = json_data)
    data = r.json()
    print(data)

# post_data()


# ------------------------------------------------------------------
# update data
def update_data():
    data = {
        'id':21,
        'name':'Rahul kumar',
        'city':'New Delhi'
    }
    herders={'content-Type':'application/json'}

 # my data is dictionary form then change to json formate
    json_data = json.dumps(data)
    r = requests.put(url = URL,herders=herders, data = json_data)
    data = r.json()
    print(data)
    
# update_data()


# -------------------------------------------------------------------
# Delete Data 
def delete_data():
    data = {'id': 22}

 # my data is dictionary form then change to json formate
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
    
# delete_data()