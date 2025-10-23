#Huvudmeny för för övervakningssystemet och larm

import monitor # Import the monitor module to access system monitoring functions
from alarm import create_alarm_menu, remove_alarm, show_alarms_menu, check_alarms # Import alarm functions from alarm module

def main_menu(): 

    alarms = [] # List to hold active alarms

    while True: # Main menu loop
        print("\n--- Main Menu ---")
        print("1. Start monitoring ") #visar en över blick över systemets nuvarande status
        print("2. List active monitoring") #Visar en lista över aktiva övervakningsparametrar
        print("3. Create alarm")
        print("4. Show alarms")
        print("5. Remove alarm")
        print("6. Start monitoring mode") #Startar kontinuerlig övervakning med larm 
        print("7. Exit")

        choice = input("\nChoose an option: ").strip()

        match choice:
            case "1":
                # Show current CPU, memory, and disk usage
                print("Monitoring has started!")
                cpu = monitor.get_cpu_usage()
                mem_pct, mem_used, mem_total = monitor.get_memory_usage() # Get current memory usage
                disk_pct, disk_used, disk_total = monitor.get_disk_usage() # Get current disk usage
                print(f"CPU Usage: {cpu}%")
                print(f"Memory Usage: {mem_pct}% ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB used)") # 1024**3 converts bytes to GB 
                print(f"Disk Usage: {disk_pct}% ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB used)")
                press_enter_to_continue()

            case "2":
                print("\nActive Monitoring:")
                print("- CPU Usage")
                print("- Memory Usage") 
                print("- Disk Usage")
                press_enter_to_continue()

            case "3":
                create_alarm_menu(alarms) # Create a new alarm from the list of alarms

            case "4":
                show_alarms_menu(alarms) # Show the list of active alarms

            case "5":
                show_alarms_menu(alarms)
                try:
                    alarm_number = int(input("Enter alarm number to remove: ")) - 1
                    if remove_alarm(alarms, alarm_number):
                        print("Alarm removed successfully.")
                    else:
                        print("Invalid alarm number.")
                except ValueError:
                    print("Please enter a valid number.")
                press_enter_to_continue()

            case "6":
                monitor.start_continuous_monitoring(alarms, check_alarms, press_enter_to_continue)
                
            case "7":
                print("Exiting...")
                break
                
            case _:
                print("Invalid option. Please try again.")

def press_enter_to_continue():
    input("\nPress Enter to continue...")
if __name__ == "__main__": # Run the main menu if this script is executed directly
    main_menu() # start the menu and activates all the functions
