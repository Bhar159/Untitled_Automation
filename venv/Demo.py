
import cx_Oracle
import os
#import sys
#print(sys.version)
#print(os.environ['oracle_home'])
os.environ['PATH']='C:\\Oracle\\instantclient-basiclite-nt-19.9.0.0.0dbru\\instantclient_19_9'
connection=cx_Oracle.connect("System","Welcome12345","localhost/Xe")
print("connected")

cur=connection.cursor()
#query1="Select * from usercredential"
query1="SELECT * FROM usercredential where username='vikkrams'"
cur.execute(query1)
b=cur.fetchall()
print(b[0][2])
#print(b[2][2])
#connection.commit()
#cur.close()
#connection.close()
print("Final")
#print(data)









