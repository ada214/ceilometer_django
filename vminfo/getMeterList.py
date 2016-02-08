import requests
from requests.auth import HTTPBasicAuth
import json
import getToken


listOfMetersUrl = "http://icoset1cs1.ad2lab.com:8777/v2/meters" 

list_of_meters= []
#meters_list = []
#alarm_desc = []
#alarm_meter_name = []

#alarm_details = []
meter_details = []
meter_list = []
token_value = ''
resourceList = []

meterSet = ()
resourceSet = ()
def getMeter(meter_list_response):
        global list_of_meters
        json_meter_list = json.loads(meter_list_response)
	global resourcelist
#        print(type(json_alarm_list))
        length = len(json_meter_list)
        global meter_list
#        global alarm_desc
 #       global alarm_meter_name
        for index in range(0,length):
#               print(json_alarm_list[index]['name'])
                meter_list.append( json_meter_list[index]['name'] )
		resourceList.append(json_meter_list[index]['resource_id'])
		
#		print(json_meter_list[index]['name'])
#               print(json_alarm_list[index]['description'])
#                alarm_desc.append( json_alarm_list[index]['description'] )

#               print(json_alarm_list[index]['threshold_rule']['meter_name'])
 #               alarm_meter_name.append(json_alarm_list[index]['threshold_rule']['meter_name'])
	
#	for index in range(0,length):
	#	print(meter_list[index])
	global meterSet
	meterSet = set(meter_list)

	global resourceSet 
	resourceSet = set(resourceList)




#	print("&&&&")
	print(type(meterSet))
#	for item in resourceSet :
#		print item
			
	print(type(resourceSet))

#        meter_details = zip(alarm_list,alarm_desc,alarm_meter_name)
#        print(len(meter_list))
        return



def MeterList():
        try:
                getToken.main()
                global token_value
                token_value = getToken.token_value
                headers = {
                        'Accept': 'application/json',
                        'X-Auth-Token': token_value
                }

                response = requests.get(listOfMetersUrl,verify=False,headers=headers)

                print(response.status_code)
                alarm_list_response = response.content

                getMeter(alarm_list_response)
		
#               print(forward_token())
        #       print(type(alarm_list_response))

        except requests.exceptions.SSLError as e:
                print("SSL Certificate error")

        global meterSet
	global resourceSet
	
        return meterSet, resourceSet


if __name__ == '__main__':
        MeterList()




