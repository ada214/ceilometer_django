import requests
from requests.auth import HTTPBasicAuth
import json
import getToken

listOfAlarmsUrl = 'http://icoset1cs1.ad2lab.com:8777/v2/alarms'

list_of_alarms = []
alarm_list = []
alarm_desc = []
alarm_meter_name = [] 

alarm_details = []

token_value = ''

def getAlarm(alarm_list_response):
	global list_of_alarms
	json_alarm_list = json.loads(alarm_list_response) 

	list_of_alarms = []
	alarm_list = []
	alarm_desc = []
	alarm_meter_name = [] 

	alarm_details = []
	
	alarm_id = []
	alarm_state = []
	alarm_condition = []



	print(type(json_alarm_list))
	length = len(json_alarm_list)
	global alarm_list
	global alarm_desc
	global alarm_meter_name
	for index in range(0,length):
#		print(json_alarm_list[index]['name'])
		alarm_list.append( json_alarm_list[index]['name'] )

#		print(json_alarm_list[index]['description'])
		alarm_desc.append( json_alarm_list[index]['description'] )

		alarm_id.append( json_alarm_list[index]['alarm_id'] )
		alarm_state.append( json_alarm_list[index]['state'] )



#		print(json_alarm_list[index]['threshold_rule']['meter_name'])
		alarm_meter_name.append(json_alarm_list[index]['threshold_rule']['meter_name'])  

		
		
	global alarm_details 
	alarm_details = zip(alarm_id, alarm_list,alarm_desc,alarm_meter_name,alarm_state)	
	print(len(alarm_list))
	return



def forward_token():
	
	return  token_value


def AlarmList():
	try:
		getToken.main()
		global token_value
		token_value = getToken.token_value
		headers = {
			'Accept': 'application/json',
			'X-Auth-Token': token_value
		}

		response = requests.get(listOfAlarmsUrl,verify=False,headers=headers)
		
		print(response.status_code)
		alarm_list_response = response.content
	
		getAlarm(alarm_list_response)

#		print(forward_token())	
	#	print(type(alarm_list_response))
		
	except requests.exceptions.SSLError as e:
		print("SSL Certificate error")
	
	global alarm_details  
	
	return alarm_details    


if __name__ == '__main__':
	AlarmList()

