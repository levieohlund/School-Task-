#System statistik 

import psutil # Import the psutil library to access system details and process utilities


def get_cpu_usage(): # Get CPU usage percentage over 1 second interval
    return psutil.cpu_percent(interval=1) # Get CPU usage percentage over 1 second interval

def get_memory_usage():
    mem = psutil.virtual_memory()  # Get memory usage statistics
    return mem.percent, mem.used, mem.total # Return percentage, used and total memory

def get_disk_usage():
    try:
        disk = psutil.disk_usage('/') # Get disk usage statistics
    except:
        disk = psutil.disk_usage('C:\\')  # For Windows systems, use C:\
    percent = (disk.used / disk.total) * 100
    return percent, disk.used, disk.total # Return percentage, used and total disk space


def list_active_monitoring(active):
    active_monitoring = []
    if active:
        cpu = get_cpu_usage()
        mem_used, mem_total = get_memory_usage()
        disk_used, disk_total = get_disk_usage()
        active_monitoring.append(f"CPU usage: {cpu}%")
        active_monitoring.append(f"Memory usage: ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB used)")
        active_monitoring.append(f"Disk usage: ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB used)")
    else:
        active_monitoring.append("No active monitoring")

    return active_monitoring
