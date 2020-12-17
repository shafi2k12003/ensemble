# Ensemble

This is a simple REST web service project.

## Description

This simple REST web service project is created in Django Rest Framework with Python language. When the project is run, it serves an endpoint genes that returns list of genes. 

## Dependency
* PyCharm, Python 3.5+
* Django, djangorestframework, mysqlclient

### How to run in PyCharm

* Download and Unzip/Git clone the project in your PC
* Open the project in PyCharm
* Create virtual environment with Django, djangorestframework, mysqlclient installed
* Select Run | Edit Configurations from the main menu
* In the Run Configuration dialog, click + icon on the toolbar.Select Python as desired configuration type.
* Browse and set manage.py file from ensemble project to script path
* Set runserver in parameters option
* Click OK button to save and close configuration windows
* Click the Run button


### How to access endpoint
* In your browser browse the url http://localhost:8000/genes/?lookup=brc
* In Postman make GET request to the url http://localhost:8000/genes with lookup parameter value brc 


