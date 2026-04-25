import requests
import pprint
import getpass
from get_current_device import get_current_device

var_router = get_current_device()

def interfaces_rest():
    
    while True:
       
        try:
            usernm = input("Username: ")
            passwd = getpass.getpass("Password: ")
            
            HOST = var_router["host"]
            URL_BASE = f"https://{HOST}/restconf/data"
            AUTH = (usernm, passwd)
            HEADERS = {
            'Content-Type': 'application/yang-data+json',
            'Accept': 'application/yang-data+json'
            }

            url = f"{URL_BASE}/ietf-interfaces:interfaces-state/"
            response = requests.get(url, auth=AUTH, headers=HEADERS, verify=False)
            pprint.pprint(response.json())
            break
   
        except: 
            print("Unexpected Error in: interfaces_rest")
            break
