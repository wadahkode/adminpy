from config import database as creds
import psycopg


credentials = "host="+creds.HOSTNAME+" port="+creds.PORT+" dbname="+creds.DATABASE+" user="+creds.USER+" password="+creds.PASSWORD
connection=psycopg.connect(credentials)

cursor = connection.cursor()

def read(sql) -> None:
  result = cursor.execute(sql)
  
  if result is None:
    return None
  else:
    return result.fetchone()