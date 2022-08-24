import psutil
import shutil
from datetime import datetime
import wrapper

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

@wrapper.wrap(wrapper.entering, wrapper.exiting)
def GetCPUUsage():

    return( psutil.cpu_percent(4),current_time)

@wrapper.wrap(wrapper.entering, wrapper.exiting)
def GetDiskUsage():

    total, used, free = shutil.disk_usage(__file__)
    return (used,total,free ,current_time)

@wrapper.wrap(wrapper.entering, wrapper.exiting)
def GetMemoryUsage():

    total = psutil.virtual_memory()[0] 
    used = psutil.virtual_memory()[1]
    free = psutil.virtual_memory()[3]
    return (used,total,free ,current_time )
    
