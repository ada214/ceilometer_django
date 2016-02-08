"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from vminfo import views
from django.conf.urls import include



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'vminfo.views.login_user',name = 'home'),
#    url(r'^$',views.login, name='login'),
    url(r'^vmlist/',views.vmlist, name='vmlist'),
    url(r'^login/$','vminfo.views.login_user',name='login'),
    url(r'^logout/$','vminfo.views.logout_user',name='logout'),
    url(r'^alarm/',views.alarmList, name='alarmList'),
    url(r'^create_alarm/',views.getAlarmPara, name='createAlarm'),
    url(r'^update_alarm/',views.updateAlarm, name='updateAlarm'),
    url(r'^delete_alarm/',views.deleteAlarm, name='deleteAlarm')
	
#    url(r'^vminfo/', include('vminfo.url', namespace='vminfo')),	
#    url(r'^login/$','django.contrib.auth.views.login',name='login',kwargs={'template_name': 'vminfo/login.html'})
]
