#Huvudmeny för för övervakningssystemet och larm

import time
import monitor  

#Första menyn som även är huvumenyn i programmet 
def main_menu():

    while True: 
        print("\n=== Main Menu ===")
        print("1. Start monitoring (show current values)")
        print("2. List active monitoring")
        print("3. Create alarm")
        print("4. Show alarms")
        print("5. Start continuous monitoring")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()
        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            
            cpu = monitor.get_cpu_usage()
            mem_pct, mem_used, mem_total = monitor.get_memory_usage()
            disk_pct, disk_used, disk_total = monitor.get_disk_usage()
            print(f"CPU Usage: {cpu}%")
            print(f"Memory Usage: {mem_pct}% ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB used)")
            print(f"Disk Usage: {disk_pct}% ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB used)")
            press_enter_to_continue()
        else:
            print("Invalid option. Please try again.")

def press_enter_to_continue():
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
