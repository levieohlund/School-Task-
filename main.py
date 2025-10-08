#Huvudmeny för för övervakningssystemet och larm

import time
<<<<<<< HEAD
import monitor  # Add this import
from alarm import create_alarm_menu, show_alarms_menu, check_alarms
=======
import monitor  

>>>>>>> e7d6feda869cb517ba93a40a8238d4d9822b7097
#Första menyn som även är huvumenyn i programmet 
def main_menu():

    while True: 
        print("\n=== Main Menu ===")
        print("1. Start monitoring (show current values)")
        print("2. List active monitoring")
        print("3. Create alarm")
        print("4. Show alarms")
        print("5. Start continuous monitoring")
        print("6. Exit")

        choice = input("\nChoose an option: ").strip()
        if choice == "6":
            print("Exiting...")
            break
        elif choice == "1":
<<<<<<< HEAD
            # Show current CPU, memory, and disk usage
=======
>>>>>>> e7d6feda869cb517ba93a40a8238d4d9822b7097
            
            cpu = monitor.get_cpu_usage()
            mem_pct, mem_used, mem_total = monitor.get_memory_usage()
            disk_pct, disk_used, disk_total = monitor.get_disk_usage()
            print(f"CPU Usage: {cpu}%")
            print(f"Memory Usage: {mem_pct}% ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB used)")
            print(f"Disk Usage: {disk_pct}% ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB used)")
            press_enter_to_continue()
        elif choice == "2":
            # List active monitoring (in this case, just show current values)
            print("\n--- Active Monitoring ---")
            cpu = monitor.get_cpu_usage()
            mem_pct, mem_used, mem_total = monitor.get_memory_usage()
            disk_pct, disk_used, disk_total = monitor.get_disk_usage()
            print(f"CPU Usage: {cpu}%")
            print(f"Memory Usage: {mem_pct}% ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB used)")
            print(f"Disk Usage: {disk_pct}% ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB used)")
            press_enter_to_continue()

        elif choice == "3":
            create_alarm_menu()

        elif choice == "4":
            show_alarms_menu()
        elif choice == "5":
            start_continuous_monitoring()
        else:
            print("Invalid option. Please try again.")

def press_enter_to_continue():
    input("\nPress Enter to continue...")

def start_continuous_monitoring():
    print("\nStarting continuous monitoring. Press Ctrl+C to stop.")
    try:
        while True:
            cpu = monitor.get_cpu_usage()
            mem_pct, mem_used, mem_total = monitor.get_memory_usage()
            disk_pct, disk_used, disk_total = monitor.get_disk_usage()
            print(f"\nCPU Usage: {cpu}%")
            print(f"Memory Usage: {mem_pct}% ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB used)")
            print(f"Disk Usage: {disk_pct}% ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB used)")

            # Check and display any triggered alarms
            triggered_alarms = check_alarms(cpu, mem_pct, disk_pct)
            for alarm in triggered_alarms:
                print(alarm)

            time.sleep(5)  # Wait for 5 seconds before the next update
    except KeyboardInterrupt:
        print("\nContinuous monitoring stopped.")
        press_enter_to_continue()

if __name__ == "__main__":
    main_menu()
