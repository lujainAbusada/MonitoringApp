import mysql.connector as mysql
import os
import wrapper
 
db = mysql.connect(
    host = os.environ['host'],
    user = os.environ['user'],
    port  = os.environ['port'],
    passwd = os.environ['passwd'],
    database = os.environ['db']
)
cursor = db.cursor()

@wrapper.wrap(wrapper.entering, wrapper.exiting)
def retrieve_CPU_data():
    cursor = db.cursor()    
    CPU = [] 	
    query = "SELECT * FROM CPU"
    cursor.execute(query)
    records = cursor.fetchall()

    for record in records:
        CPU.append({"CPU Utilization" : record[1],"Time" : str(record[2])})
    db.commit()
    cursor.close()
    return(CPU)     

@wrapper.wrap(wrapper.entering, wrapper.exiting)
def retrieve_CPUNow_data():
    cursor = db.cursor()
    query = "SELECT * FROM `CPUNow` ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    records = cursor.fetchone();
    db.commit()
    cursor.close()
    return ({"CPU Utilization" : records[1],"Time" : str(records[2])})

def retrieve_Memory_data():
    cursor = db.cursor()
    Memory = []
    query = "SELECT * FROM Memory"
    cursor.execute(query)
    records = cursor.fetchall()
    db.commit()
    for record in records:
        Memory.append({"Used" : record[1], "Total" : record [2], "Free": record [3],"Time" : str(record[4])})
    cursor.close()
    return(Memory)

def retrieve_MemoryNow_data():
    cursor = db.cursor()
    query = "SELECT * FROM `MemoryNow` ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    record = cursor.fetchone()
    db.commit()
    cursor.close()
    return ({"Used" : record[1], "Total" : record [2], "Free": record [3],"Time" : str(record[4])})


def retrieve_Disk_data():
    cursor = db.cursor()
    Disk = []
    query = "SELECT * FROM Disk"
    cursor.execute(query)
    records = cursor.fetchall()
    db.commit()
    cursor.close()
    for record in records:
        Disk.append({"Used" : record[1], "Total" : record [2], "Free": record [3],"Time" : str(record[4])})
    return(Disk)


def retrieve_DiskNow_data():
    cursor = db.cursor()
    query = "SELECT * FROM `MemoryNow` ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    record = cursor.fetchone()
    db.commit()
    cursor.close()
    return({"Used" : record[1], "Total" : record [2], "Free": record [3],"Time" : str(record[4])})


