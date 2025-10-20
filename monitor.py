#System statistik 

import psutil # Import the psutil library to access system details and process utilities
import time # Import the time module to use sleep function


def get_cpu_usage(): # Get CPU usage percentage over 1 second interval
    return psutil.cpu_percent(interval=1) # Get CPU usage percentage over 1 second interval

def get_memory_usage():
    mem = psutil.virtual_memory()  # Get memory usage statistics
    return mem.percent, mem.used, mem.total # Return percentage, used and total memory

def get_disk_usage():
    try:
        disk = psutil.disk_usage('/') # Get disk usage statistics
    except:
        disk = psutil.disk_usage('C:\\') # For Windows systems, use C:\
    percent = (disk.used / disk.total) * 100 # Calculate disk usage percentage
    return percent, disk.used, disk.total # Return percentage, used and total disk space


def list_active_monitoring(active):
    active_monitoring = []
    if active: # If monitoring is active, get current stats
        cpu = get_cpu_usage()
        _, mem_used, mem_total = get_memory_usage()
        _, disk_used, disk_total = get_disk_usage()
        active_monitoring.append(f"CPU usage: {cpu}%")
        active_monitoring.append(f"Memory usage: ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB used)")
        active_monitoring.append(f"Disk usage: ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB used)")
    else:
        active_monitoring.append("No active monitoring")

    return active_monitoring


def start_continuous_monitoring(alarm, check_alarms_func, press_enter_func):

    # Start continuous monitoring with alarm checking.

    print("\nStarting continuous monitoring. Press Ctrl+C to stop.")
    try: 
        while True: 
            cpu = get_cpu_usage() # Get current CPU usage
            mem_pct, mem_used, mem_total = get_memory_usage() # Get current memory usage
            disk_pct, disk_used, disk_total = get_disk_usage() # Get current disk usage
            print(f"\nCPU Usage: {cpu}%")
            print(f"Memory Usage: {mem_pct}% ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB used)") # Memory usage
            print(f"Disk Usage: {disk_pct}% ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB used)")

            # Check and display any triggered alarms
            triggered_alarms = check_alarms_func(alarm, cpu, mem_pct, disk_pct)
            for alarm_message in triggered_alarms: # Display each triggered alarm
                print(alarm_message)

            time.sleep(5)  # Wait for 5 seconds before the next update
    except KeyboardInterrupt: # Allow user to stop with Ctrl+C
        print("\nContinuous monitoring stopped.")
        press_enter_func()
