import mysql.connector as mysql
from  StoreStatistics import StoreUsage
from FindStatistics import GetCPUUsage, GetMemoryUsage, GetDiskUsage

CPU_query = "INSERT INTO CPU(Utilization,time) VALUES(%s,%s)"
Disk_query = "INSERT INTO Disk(used,total,free,time) VALUES(%s,%s,%s,%s)"
Memory_query = "INSERT INTO Memory(used,total,free,time) VALUES(%s,%s,%s,%s)"

CPU_values = GetCPUUsage()
Disk_values= GetDiskUsage()
Memory_values = GetMemoryUsage()

db = mysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "root",
    database = "Statistics"
)

limit = 23

StoreUsage(db,CPU_values,CPU_query,'CPU',limit)
StoreUsage(db,Memory_values,Memory_query,'Memory',limit)
StoreUsage(db,Disk_values,Disk_query,'Disk',limit)
