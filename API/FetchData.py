import mysql.connector as mysql
import os

db = mysql.connect(
    host = os.environ['host'],
    user = os.environ['user'],
    port  = os.environ['port'],
    passwd = os.environ['passwd'],
    database = os.environ['db']
)

cursor = db.cursor()

def retrieve_CPU_data():
    
    CPU = [] 	
    query = "SELECT * FROM CPU"
    cursor.execute(query)
    records = cursor.fetchall()

    for record in records:
        CPU.append({"CPU Utilization" : record[1],"Time" : str(record[2])})
    db.commit()
    return(CPU)     

def retrieve_CPUNow_data():

    query = "SELECT * FROM `CPUNow` ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    records = cursor.fetchone();
    db.commit()
    return ({"CPU Utilization" : records[1],"Time" : str(records[2])})

def retrieve_Memory_data():
    
    Memory = []
    query = "SELECT * FROM Memory"
    cursor.execute(query)
    records = cursor.fetchall()
    db.commit()
    for record in records:
        Memory.append({"Used" : record[1], "Total" : record [2], "Free": record [3],"Time" : str(record[4])})
    return(Memory)

def retrieve_MemoryNow_data():

    query = "SELECT * FROM `MemoryNow` ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    record = cursor.fetchone()
    db.commit()
    return ({"Used" : record[1], "Total" : record [2], "Free": record [3],"Time" : str(record[4])})


def retrieve_Disk_data():

    Disk = []
    query = "SELECT * FROM Disk"
    cursor.execute(query)
    records = cursor.fetchall()
    db.commit()

    for record in records:
        Disk.append({"Used" : record[1], "Total" : record [2], "Free": record [3],"Time" : str(record[4])})
    return(Disk)


def retrieve_DiskNow_data():

    query = "SELECT * FROM `MemoryNow` ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    record = cursor.fetchone()
    db.commit()

    return({"Used" : record[1], "Total" : record [2], "Free": record [3],"Time" : str(record[4])})

