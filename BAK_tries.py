import pyodbc
import pandas as pd
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'Asus-PC' 
database = 'PEC_ENERGA2' 
username = 'wroszu' 
password = 'kvgyzqkQ1!'  
cnxn = pyodbc.connect('DRIVER={{ODBC Driver 18 for SQL Server}};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
# select 26 rows from SQL table to insert in dataframe.
query = "SELECT TOP (1000) [Urzadzenie] FROM [PEC_ENERGA2].[dbo].[modbus]"
df = pd.read_sql(query, cnxn)
print(df.head(26))