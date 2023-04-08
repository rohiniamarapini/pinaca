from flask import Flask, request, jsonify, render_template
import sqlite3
import pandas as pd

#create a flask app
app = Flask(__name__)
#connect to sqlite database  
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row 
    return conn
 #define a route 
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
  
  

@app.route('/result', methods=['GET', 'POST'])
def result():
    conn = get_db_connection()
    output = request.form.to_dict()
    print(output)
    continent = output['continent']
    field = output['field']
    
     # Query the database for matching records
    try:
        query = f"SELECT {field} FROM company WHERE Continent = '{continent}' AND {field} IS NOT NULL"
        response = conn.execute(query).fetchall()
        #print(results)
        num_of_records = len(response)
        print(num_of_records)
    except:
        return "Invalid Field data. Provided field doesn't exist in the database"
        

    # Return the response as JSON
    return render_template('result.html', headings = field, data = response, records = num_of_records)
  
 # run the app 
if __name__ == '__main__':
    app.run(debug=True)