
import pyodbc
import matplotlib.pyplot as plt
import pandas as pd

user = 'DESKTOP-3QJN7S3'+"\)" + "user"  # sql server user name

user_rep = user.replace(")" , "")

conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=DESKTOP-3QJN7S3;" # Server name
                      f"uid={user_rep}"
                      "Database=grolab_store;" # selected database
                      "Trusted_Connection=yes;")

# Fetching the data from the selected table using SQL query
rawdata = pd.read_sql_query('''select * from [grolab_store].[dbo].[test_database]''', conn)
print(rawdata['Row_ID'])
