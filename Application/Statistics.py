import psutil
import shutil
import json
import mysql.connector as mysql
from datetime import datetime



CPU_query = "INSERT INTO CPU(Utilization,time) VALUES(%s,%s)"
Disk_query = "INSERT INTO Disk(used,total,free,time) VALUES(%s,%s,%s,%s)"
Memory_query = "INSERT INTO Memory(used,total,free,time) VALUES(%s,%s,%s,%s)"

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

db = mysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "root",
    database = "Statistics"
)
cursor = db.cursor()


def check_table(number,table):
    if (number > 23):
       query=("DELETE FROM `" + table + "`ORDER BY time LIMIT 1")
       cursor.execute(query)


def CPU_Usage():
    
    values = ( psutil.cpu_percent(4),current_time )
    cursor.execute("SELECT COUNT(*) FROM CPU")
    result = cursor.fetchone()
    check_table(result[0],"CPU")
    cursor.execute(CPU_query, values)
    db.commit()

def Disk_Usage():
   
    total, used, free = shutil.disk_usage(__file__)
    values = (used,total,free ,current_time )
    cursor.execute("SELECT COUNT(*) FROM Disk")
    result = cursor.fetchone()
    check_table(result[0],"Disk")
    cursor.execute(Disk_query, values)
    db.commit()

def Memory_Usage():
   
    total = psutil.virtual_memory()[0] 
    used = psutil.virtual_memory()[1]
    free = psutil.virtual_memory()[3]
    values = (used,total,free ,current_time )
    cursor.execute("SELECT COUNT(*) FROM Memory")
    result = cursor.fetchone()
    check_table(result[0],"Memory")
    cursor.execute(Memory_query, values)
    db.commit()


CPU_Usage()
Disk_Usage()
Memory_Usage()

