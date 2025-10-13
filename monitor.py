#System statistik 

import psutil # Import the psutil library to access system details and process utilities


def get_cpu_usage(): # Get CPU usage percentage over 1 second interval
    return psutil.cpu_percent(interval=1) # Get CPU usage percentage over 1 second interval

def get_memory_usage():
    mem = psutil.virtual_memory()  # Get memory usage statistics
    return mem.percent, mem.used, mem.total # Return percentage, used and total memory

def get_disk_usage():
    disk = psutil.disk_usage('/') # Get disk usage statistics
    return disk.percent, disk.used, disk.total # Return percentage, used and total disk space
