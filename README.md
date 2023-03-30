# COMP353FinalProject
COMP353 Final Project folder using Django framework


Some basic tips on running this project are found below: 
This project uses a virtual environment that may need ExecutionPolicies to be changed on your windows machine before running.
Open the project folder in visual studio code and open a terminal. 

Run the following commands to set up the virtual environment. 
'python -m venv venv'
'venv\Scripts\activate' \\ This command may require execution policies. 
Run 'pip install django' in the virtual environment.

Run 'pip install mysqlclient' in the virtual environment.

Running 'python manage.py runserver' will run the server and on a webbrowser enter "localhost:8000" to load the default webpage. 
                                                                         "localhost:8000/index" will print "Hello World!"
Running 'python manage.py migrate' will update the database with all the newest changes.

Running 'python manage.py inspectdb > models.py' will create all the models for the tables found in our database and output them in the models.py file.
