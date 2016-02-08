# Ceilometer based Alarm creation, updation and deletion using Django framework
Contains source code for "Ceilometer based Alarm creation, updation and deletion using Django framework"

Requirements to run project
-------
* Django 1.9
* Python 3.x

To run this project in your environment follow these steps
-------
Create the project directory
-------
* mkdir project
* cd project

Create a virtualenv and activate it
* virtualenv project
* source project/bin/activate 

Install Django and Django REST framework into the virtualenv
-----
* pip install django
* pip install djangorestframework

Now, as we have to use existing project, instead of creating new project, copy "project" into virual environment. After copying, your directory will have bin, lib, local, pip-selfcheck.json, project. (except project all other files and folders are created after creating virtual env. "Project" is existing project which we want to run)

* cd project

Now, this directory has manage.py file. To run project on development server use
----
* python manage.py runserver 0.0.0.0:8000

To see home page, http://ip_address:8000, here you will see login page, Enter creds,admin/gsLab123
