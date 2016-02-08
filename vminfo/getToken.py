import requests
from requests.auth import HTTPBasicAuth
import json

#listOfVmsUrl='https://icoset1cs1.ad2lab.com:8443/orchestrator/v2/instancetypes/'
#listOfVmsUrl='https://icoset1cs1.ad2lab.com:8443/orchestrator/v2/instancetypes/openstackvms%20/instances/'
#listOfVmsUrl= 'https://icoset1cs1.ad2lab.com:8443/orchestrator/v2/instancetypes/openstackvms%20/instances/RegionKVM--1993988c-4faa-494d-a1d6-b11bda2b778f'
username = "admin"
password = "passw0rd"
head= {'Content-Type': 'application/json',
	'Accept': 'application/json',
	}
body= {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "admin",
                    "domain": {
                        "id": "default"
                    },
                    "password": "passw0rd"
                }
            }
        }
    }
}









tokenUrl='http://icoset1cs1.ad2lab.com:5000/v3/auth/tokens'
token_value = '' 

def main():

	try:
        	response = requests.post(tokenUrl,auth=HTTPBasicAuth('admin','passw0rd'),verify=False,headers=head,data=json.dumps(body))
		global token_value
		token_value = response.headers['X-Subject-Token']
#	print(response.headers['X-Subject-Token'])
		print(token_value)
	

	except requests.exceptions.SSLError as e:
        	print("SSL Certificate error")
	
	



if __name__ == "__main__":
	main()
