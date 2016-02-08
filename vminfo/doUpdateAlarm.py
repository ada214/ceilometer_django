import requests
from requests.auth import HTTPBasicAuth
import json
import getToken
import getAlarmList


#url = 'http://icoset1cs1.ad2lab.com:8777/v2/alarms/0ef49b14-804a-409d-81b9-e2a7d1cac4a6'

def putAlarm(data):
#	getAlarmList.AlarmList()

	alarm_id = data['alarm_id']
	update_url = 'http://icoset1cs1.ad2lab.com:8777/v2/alarms/' + alarm_id 

	getToken.main()
	global token_value
        token_value = getToken.token_value
#	data = json.loads(data)

	headers = {
                        'Accept': 'application/json',
			'Content-Type' : 'application/json',
                        'X-Auth-Token': token_value
                }

	
	old_body = requests.get(update_url,verify=False,headers=headers)

#	print(type(old_body.content))
	json_body = json.loads(old_body.content)
#	print(type(json_body))
		
	json_body['threshold_rule']['threshold'] = data['threshold']
	json_body['threshold_rule']['comparison_operator'] = data['comparison_operator']
#	print(data['comparison_operator'])
#	print("***********")
	json_body['threshold_rule']['statistic'] = data['statistics']
	
	
	
	response = requests.put(update_url,verify=False,headers=headers,data = json.dumps(json_body))
	print(response.status_code)	
	status = ""
	if response.status_code == 200 :
		status = "Alarm "+ alarm_id + "  updated"
	else :
		status = "Alarm "+ alarm_id + " not updated. Code : " + response.status_code 
	
	return status

if __name__ == '__main__':
	putAlarm()
