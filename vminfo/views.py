from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
import json
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import getAlarmList
import createAlarm
import getMeterList
import doUpdateAlarm 
import doDeleteAlarm


listOfVmsUrl='https://icoset1cs1.ad2lab.com:8443/orchestrator/v2/instancetypes/openstackvms/instances/'
username = "admin"
password = "passw0rd"

vm_name= []
zone = []
ipaddress = []
status = []
region = []

final_list = []
##########

meterSet = ()


def getListOfVms(json_vm_list):
	parsed_list_of_vms = json.loads(json_vm_list)
	length = len(parsed_list_of_vms['items'])
	vm_name= []
	zone = []
	ipaddress = []
	status = []
	region = []

	final_list = []

	for index in range(0,length):
#		print(parsed_list_of_vms['items'][index]['href'])
#		print( parsed_list_of_vms['items'][index]['item']['parm']['name'])

	
#		print(parsed_list_of_vms['items'][index]['item']['parm']['id'])
#		vm_name.append(parsed_list_of_vms['items'][index]['item']['parm']['id'])
	
#		print(parsed_list_of_vms['items'][index]['item']['parm']['name'])
		global vm_name
		vm_name.append(parsed_list_of_vms['items'][index]['item']['parm']['name'])
	
			
#		print(parsed_list_of_vms['items'][index]['item']['availabilityZone'])
		global zone
		zone.append(parsed_list_of_vms['items'][index]['item']['availabilityZone'])

#		print(parsed_list_of_vms['items'][index]['item']['parm']['addresses']['demo'][0]['addr'])
		global ipaddress
		ipaddress.append(parsed_list_of_vms['items'][index]['item']['parm']['addresses']['demo'][0]['addr'])
	
#		print(parsed_list_of_vms['items'][index]['item']['parm']['status'])
		global status
		status.append(parsed_list_of_vms['items'][index]['item']['parm']['status'])

#		print(parsed_list_of_vms['items'][index]['item']['region'])
		global region
		region.append(parsed_list_of_vms['items'][index]['item']['region']) 
	
	global final_list
	final_list = zip(vm_name,zone,ipaddress,status,region)

	return		
'''
	ll = len(vm_name)
	for index in range(0,ll):
		print(vm_name[index])
		print(region[index])
		print(ipaddress[index])
'''
#	return




##############


# Create your views here.
def login_re(request):
#	form = LoginForm()
	context = {
		"form":"Abhinay",
	}
	return render(request,'login.html',context)


def vmlist(request):

	try:
		response = requests.get(listOfVmsUrl,auth=HTTPBasicAuth('admin','passw0rd'),verify=False)
		json_vm_list = response.content
		getListOfVms(json_vm_list)
		context = {
			"vm_name" :vm_name,
			"zone":	zone,
			"ipaddress": ipaddress,
			"status" : status,
			"region" : region,
		}
		ct = {
			"final_list" : final_list
		}
	
	#	final_list = zip(vm_name,zone,ipaddress,status,region)
	
	except requests.exceptions.SSLError as e:
		print("SSL Certificate error")

	return render(request,'vmlist.html',ct)


def login_user(request):
	state = "Please log in below..."
        username = password = ''
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    state = "You're successfully logged in!"
#		    return HttpResponseRedirect(reverse('views.vmlist'))
		    return redirect('vminfo.views.vmlist')	
                else:
                    state = "Your account is not active, please contact the site admin."
            else:
                state = "Your username and/or password were incorrect."

	return render_to_response('auth.html',{'state':state, 'username': username},RequestContext(request))



def alarmList(request):
	alarm_list =getAlarmList.AlarmList()
	
	cont = {
			"alarm_list" : alarm_list
		}
	print("In the view : length")
	print(len(alarm_list))
	return render(request,'alarmlist.html',cont)


def getAlarmPara(request):
	state = " "	
	if request.POST:
            alarm_name = request.POST.get('alarmname')
            description = request.POST.get('description')
	    meter_name  = request.POST.get('meter_name')

	    threshold = request.POST.get('threshold')
	    comparison_operator = request.POST.get('comparison_operator')
	    statistic = request.POST.get('statistic')
	    resource_id = request.POST.get('resource_id')

	    data_action = {"alarm_actions": ["log:///tmp/tst.txt"], "description": description, "threshold_rule": {"meter_name": meter_name, "evaluation_periods": 2, "period": 10, "statistic": statistic, "threshold": threshold, "query": [{"field": "resource_id", "type": "", "value": resource_id, "op": "eq"}], "comparison_operator": comparison_operator }, "repeat_actions": False, "type": "threshold", "name": alarm_name}


	

	    data =  {"threshold_rule": {"meter_name": meter_name , "evaluation_periods": 3, "period": 600, "statistic": statistic, 			"threshold": threshold, "query": [{"field": "resource_id", "type": "",
			 "value": "500a1594-4972-7968-2914-c333201585bd", "op": "eq"}],
                         "comparison_operator": comparison_operator }, "repeat_actions": False,
	                "type": "threshold",
        	        "description": description,
#			"alarm-action": 'log:///tmp/tst.txt',
	              	"name": alarm_name }
	
#	    print(username)
#	    print(description) 		
	    status_code = createAlarm.createAlarm(data_action)			
#	    print("$$$$$$$$$$$$")
 #           print(status_code)			
	    if status_code == 201 :
	  	  state = "Alarm sucessfully created."			
	    elif status_code == 409 :
		  state = "Alarm is not created because name already exists."	

		
	global meterSet
	meterSet, resourceSet = getMeterList.MeterList()

	ct = {
		"meterSet":meterSet,
		"resourceSet": resourceSet,
		"state":state
	}

	return render(request,'getpara.html',ct)

def logout_user(request):
    logout(request)
    return redirect('home')



def updateAlarm(request):
	status = ""	
	alarm_list =getAlarmList.AlarmList()
	
	if request.POST :
		alarm_id = request.POST.get('alarm_name')
		threshold= request.POST.get('threshold')
		comparison_operator = request.POST.get('comparison_operator' )
		statistics = request.POST.get('statistic')
		

		update_data = {
			"alarm_id" : alarm_id,
			 "threshold" : threshold,
			"comparison_operator" : comparison_operator,
			"statistics" : statistics 	
			}		

		status=	doUpdateAlarm.putAlarm(update_data)
		
	cont = {
		"state" : status,
		"alarm_list":alarm_list

		}	
	return render(request,'update_alarm.html',cont)

def deleteAlarm(request):
	status = ""	
	alarm_list =getAlarmList.AlarmList()
		
	if request.POST :
		alarm_id = request.POST.get('alarm_id')
		data = {
			"alarm_id" : alarm_id
		}
		status = doDeleteAlarm.delAlarm(data)	
		print("i$$$$$$$$")
		print(status)
	


	cont = {
		"status" : status,
		"alarm_list":alarm_list

	}	


		
	return render(request,'delete_alarm.html',cont)
