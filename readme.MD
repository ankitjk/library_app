Group Members: Ankit Kulshrestha, Vue Thao

To run the library management system, some python packages such as flask and sqlalchemy may need to be installed. 
1) python -m venv venv
2) .\venv\Scripts\activate
3) pip install flask
4) pip install flask_sqlalchemy
5) pip install flask_login
6) to run do: python run.py

When done:
deactivate

Also, if you want to create the tables from scratch, comment out the lines of code in run.py where specified to recreate the tables and load all the data. Running 'python3 run.py' in your shell should start the server and the webpage will be accessible through http://127.0.0.1:5000/.
