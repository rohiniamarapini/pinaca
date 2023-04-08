# Data ingestion in DB and response generation.

To ingest the data in SQlite db and generate the response according to the field given using python


## Acknowledgements

 - [Python SQlite](https://www.javatpoint.com/python-sqlite)
 - [Flask with SQlite](https://www.javatpoint.com/flask-sqlite)
 - [Sqlite3 Overview](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany)


## Demo



Flask APP running - 

![Screenshot (12)](https://user-images.githubusercontent.com/130124301/230705777-ff7e2d5c-2227-4ca5-b87e-e0028248ddfd.png)


Demo VIDEO :


https://user-images.githubusercontent.com/130124301/230705990-2b049c68-22b8-48d3-934e-6f4a9aa78723.mp4
## Deployment

To deploy this project run

```bash
#create database and insert data
python3 ingestion.py

#run python flask application
python3 pinacalabs_round2.py
flask --app pinacalabs_round2 run
```
'


## Installation

Install python3 with pip

```bash
  pip install python3
  pip install pandas
  pip install flask
  pip install sqlite3
  pip install requests
 
```
    
