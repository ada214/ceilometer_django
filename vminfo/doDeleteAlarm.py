import requests
from requests.auth import HTTPBasicAuth
import json
import getToken
import getAlarmList


def delAlarm(data):

        alarm_id = data['alarm_id']
        del_url = 'http://icoset1cs1.ad2lab.com:8777/v2/alarms/' + alarm_id

        getToken.main()
        global token_value
        token_value = getToken.token_value


        headers = {
                        'Accept': 'application/json',
                        'Content-Type' : 'application/json',
                        'X-Auth-Token': token_value
                }


        response = requests.delete(del_url,verify=False,headers=headers)
        print(response.status_code)
		
        status = ""
        if response.status_code == 204 :
                status = "Alarm "+ alarm_id + "  deleted"
        else :
                status = "Alarm "+ alarm_id + " not deleted Code : "

        return status

if __name__ == '__main__':
        delAlarm()

