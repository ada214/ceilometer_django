import requests
from requests.auth import HTTPBasicAuth
import json
import getToken



Url = 'http://icoset1cs1.ad2lab.com:8777/v2/alarms'


def createAlarm(data):

        try:
		getToken.main()
		head= {'Content-Type': 'application/json',
		        'Accept': 'application/json',
			'X-Auth-Token': getToken.token_value 
		        }


		old_data = 	{"threshold_rule": {

			"meter_name": "cpu_usage_high", "evaluation_periods": 3, "period": 600, "statistic": "avg", "threshold": 40.0,
			 "query": [{"field": "resource_id", "type": "", "value": "500a1594-4972-7968-2914-c333201585bd", "op": "eq"}], 
			 "comparison_operator": "gt" }, 
		"repeat_actions": False, 
		"type": "threshold", 
		"description": " Test of CPU usage high", 
		"name": "cpu_high_alarm_ada_007"}




		print(getToken.token_value)
#		print(type(payLoad))
#		print(type(json.dumps(payLoad))
		
#                response = requests.post(Url,auth=HTTPBasicAuth('admin','passw0rd'),verify=False,headers=head,data=json.dumps(payLoad))
                response = requests.post(Url,verify=False,headers=head,data=json.dumps(data))

		
		print(response.status_code)

        except requests.exceptions.SSLError as e:
                print("SSL Certificate error")
	print (response.status_code)
	return response.status_code

if __name__ == "__main__":
        createAlarm()

