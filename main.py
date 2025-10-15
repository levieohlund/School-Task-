#Huvudmeny för för övervakningssystemet och larm

import time # Import the time module to use sleep function
import monitor # Import the monitor module to access system monitoring functions
from alarm import create_alarm_menu, show_alarms_menu, check_alarms # Import alarm functions from alarm module

def main_menu(): 

    active = False # Track if monitoring is active

    while True: # Main menu loop
        print("\n--- Main Menu ---")
        print("1. Start monitoring ") #visar en över blick över systemets nuvarande status
        print("2. List active monitoring") #Visar en lista över aktiva övervakningsparametrar
        print("3. Create alarm")
        print("4. Show alarms")
        print("5. Start monitoring mode") #Startar kontinuerlig övervakning med larm 
        print("6. Exit")

        choice = input("\nChoose an option: ").strip()
        if choice == "6":
            print("Exiting...")
            break
        elif choice == "1":
            # Show current CPU, memory, and disk usage
            active = True  # Activate monitoring
            print("Monitoring has started!")

            cpu = monitor.get_cpu_usage()
            mem_pct, mem_used, mem_total = monitor.get_memory_usage() # Get current memory usage
            disk_pct, disk_used, disk_total = monitor.get_disk_usage() # Get current disk usage
            print(f"CPU Usage: {cpu}%")
            print(f"Memory Usage: {mem_pct}% ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB used)") # 1024**3 converts bytes to GB 
            print(f"Disk Usage: {disk_pct}% ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB used)")
            press_enter_to_continue()

        elif choice == "2":
            monitoring_status = monitor.list_active_monitoring(active) # Get active monitoring status
            print("\nActive Monitoring:")
            for status in monitoring_status: # Display each active monitoring status
                print(f"- {status}") # Display each active monitoring status
            press_enter_to_continue() #
        
            

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
            cpu = monitor.get_cpu_usage() # Get current CPU usage
            mem_pct, mem_used, mem_total = monitor.get_memory_usage() # Get current memory usage
            disk_pct, disk_used, disk_total = monitor.get_disk_usage() # Get current disk usage
            print(f"\nCPU Usage: {cpu}%")
            print(f"Memory Usage: {mem_pct}% ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB used)") # Memory usage
            print(f"Disk Usage: {disk_pct}% ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB used)")

            # Check and display any triggered alarms
            triggered_alarms = check_alarms(cpu, mem_pct, disk_pct)
            for alarm in triggered_alarms: # Display each triggered alarm
                print(alarm)

            time.sleep(5)  # Wait for 5 seconds before the next update
    except KeyboardInterrupt: # Allow user to stop with Ctrl+C
        print("\nContinuous monitoring stopped.")
        press_enter_to_continue()

if __name__ == "__main__": # Run the main menu if this script is executed directly
    main_menu() # Start the main menu
