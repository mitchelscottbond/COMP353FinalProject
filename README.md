# COMP353FinalProject
COMP353 Final Project folder using Django framework


Some basic tips on running this project are found below: 
This project uses a virtual environment that may need ExecutionPolicies to be changed on your windows machine before running.
Open the project folder in visual studio code and open a terminal. 

Run the following commands to set up the virtual environment: 
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
This command above may require execution policies. 

Run the following command in the virtual environment.
```bash
pip install django
```

Run the following command in the virtual environment.
```bash
pip install mysqlclient
```

Running the following command will run the server and on a webbrowser enter "localhost:8000" to load the default webpage. (make sure you are in the root directory)
                                                                         "localhost:8000/index" will print "Hello World!"

```bash
python manage.py runserver
```

Running the following command will update the database with all the newest changes.

```bash
python manage.py migrate
```

Running the following command will create all the models for the tables found in our database and output them in the models.py file.

```bash
python manage.py inspectdb > models.py
```

If you are attempting this from home, you need to connect to the School via the Forticlient VPN. 

If you find that the python manage.py runserver is not working. Try deleting the venv folder and restarting from the beginning. 
