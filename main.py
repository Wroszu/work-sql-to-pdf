"""
Connects to a SQL database using pyodbc
"""

import pyodbc

SERVER = '127.0.0.1'
DATABASE = 'master'
USERNAME = 'wroszu'
PASSWORD = 'kvgyzqkQ1!'

conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};'
                      f'Server={SERVER};'
                      f'Database={DATABASE};'
                      f'UID={USERNAME};'
                      f'PWD={PASSWORD};'
                      'TrustServerCertificate=yes;')

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r.CustomerID}\t{r.OrderCount}\t{r.CompanyName}")