import sqlite3
import pandas as pd
#to create a new database and connect to sqlite3
connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Load the data from the CSV file
data_url = 'https://csvbase.com/meripaterson/stock-exchanges'
df = pd.read_csv(data_url)

cur = connection.cursor()
# Insert the data into the table
# Convert DataFrame to a structured array of records
records = df.to_records(index=False)
cur.executemany('''INSERT INTO company
                   (ROWID, Continent, Country, Name, MIC, LastChanged)
                   VALUES (?, ?, ?, ?, ?, ?)''', records)
connection.commit()
connection.close()
  