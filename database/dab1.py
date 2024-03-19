# relational vs non relational database
#connect mysql database on your own
import sqlite3
connection_=sqlite3.connect("employee.db")
cur = connection_.cursor()
try:
    cur.execute("CREATE TABLE profile(name,age, department)")
except sqlite3.OperationalError:
    pass
cur.execute("INSERT INTO profile VALUES('Ram','21','science')")

connection_.commit()

connection_.close()