import MySQLdb
from jproperties import Properties
import glob, os
import _mysql_exceptions
import time

p = Properties()
with open("conf/azkaban.properties", "r+b") as f:
    p.load(f, "utf-8")

retry = 18
while True:
    try:
        db = MySQLdb.connect(host=p["mysql.host"].data,
                     user="root",
                     passwd=os.environ['MYSQL_ROOT_PASSWORD'],
                     db="mysql")
        break
    except _mysql_exceptions.OperationalError as e:
        if retry == 0:
            raise
    print "database is not ready, waiting.. " + str(retry) 
    time.sleep(10)
    retry -= 1

cursor = db.cursor()
cursor.execute("show databases")
numrows = cursor.rowcount

dbs = set()
# Get and display one row at a time
for x in range(0, numrows):
    row = cursor.fetchone()
    dbs.add(row[0])
cursor.close()

if p["mysql.database"].data in dbs:
    print p["mysql.database"].data+ " db is already created"
else:
    cursor = db.cursor()
    print "creating database and user..."
    cursor.execute("CREATE DATABASE " + p["mysql.database"].data)
    cursor.execute("CREATE USER '"+p["mysql.user"].data+"'@'%' IDENTIFIED BY '"+p["mysql.password"].data+"'")
    cursor.execute("GRANT SELECT,INSERT,UPDATE,DELETE ON "+p["mysql.database"].data+".* to '"+p["mysql.user"].data+"'@'%' WITH GRANT OPTION")
    cursor.close()
    db.close()
    db = MySQLdb.connect(host=p["mysql.host"].data,
                     user="root",
                     passwd="my-secret-pw",
                     db=p["mysql.database"].data)

    structurePath = "azkaban-db/src/main/sql"
    for file in os.listdir(structurePath):
        if file.endswith(".sql") and not file.startswith("upgrade") :
            fullFilePath = os.path.join(structurePath, file)
            print(fullFilePath)
            with open(fullFilePath, 'r') as currentFile:
                fileContent = currentFile.read().replace('\n', '')
                dataLines = fileContent.split(';')
                for l in dataLines:
                    if len(l) > 0:
                        cursor = db.cursor()
                        cursor.execute(l)
                        cursor.close()
    print "all scripts are executed, exiting." 


db.close()

