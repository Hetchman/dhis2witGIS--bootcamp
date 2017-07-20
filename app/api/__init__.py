
import requests

# dict for authentication
auth = {
   "username": "admin",
   "password": "district"
}

# get json given url
def get_json(endpoint):
   user = auth['username']
   passwd = auth['password']

   # get document
   r = requests.get(endpoint["url"], auth=(user, passwd), params=endpoint["payload"])

   return r.json()
