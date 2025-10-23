import logger 


class Alarm: #Alarm class to hold alarm details
    def __init__(self, monitor_type, threshold, condition): #
        self.monitor_type = monitor_type  # 'cpu', 'memory', or 'disk'
        self.threshold = threshold  # percentage value
        self.condition = condition  # 'above' or 'below'

    def __str__(self): #String representation of the alarm
        return f"Alarm: {self.monitor_type} {self.condition} {self.threshold}%"

def add_alarm(alarm_list, alarm):
    alarm_list.append(alarm)
    logger.log_alarm_created(alarm.monitor_type, alarm.threshold, alarm.condition)

def list_alarms(alarm_list):
    return alarm_list

def remove_alarm(alarm_list, number):  # Removes an alarm by its index
    if 0 <= number < len(alarm_list):  # Check if the alarm number is valid
        del alarm_list[number]  # Remove the alarm from the list
        return True  # Indicate success
    return False  # Indicate failure if index is invalid



def create_alarm_menu(alarm_list): 
    while True:
        print("\n--- Create Alarm ---")
        print("1. CPU usage")
        print("2. Memory usage")
        print("3. Disk usage")
        print("0. Back to main menu")

        choice = input("Choose alarm type: ").strip()
        if choice == "0":
            break

        if choice in ["1", "2", "3"]:
            alarm_type = {"1": "cpu", "2": "memory", "3": "disk"}[choice]
            configure_alarm_details(alarm_list, alarm_type)
        else:
            print("Invalid choice.")

def configure_alarm_details(alarm_list, alarm_type):
    # Hanterar konfigurering av alarm-detaljer (nivå och villkor)
    try:  # Försök att sätta alarmnivå
        level = int(input("Set alarm level (1–100): "))  # Sätt alarmnivå
        if 1 <= level <= 100:
            print("1. Above threshold (alarm when usage goes over X%)")
            print("2. Below threshold (alarm when usage goes under X%)")
            condition = input("Choose alarm condition: ").strip()
            if condition == "1":
                add_alarm(alarm_list, Alarm(alarm_type, level, "above"))
            elif condition == "2":
                add_alarm(alarm_list, Alarm(alarm_type, level, "below"))
            else:
                print("Invalid condition.")
        else:
            print("Value must be between 1–100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

        
def show_alarms_menu(alarm_list):
    print("\n--- Active Alarms ---")
    if not alarm_list:
        print("No active Alarms.")
    else:
        for idx, alarm in enumerate(alarm_list, start=1): # Enumerate alarms for display
            print(f"{idx}. {alarm}")
    input("\nPress Enter to continue...")
    
def check_alarms(alarm_list, cpu, memory, disk):
    current_values = {"cpu": cpu, "memory": memory, "disk": disk}
    triggered_alarms = []

    for alarm in alarm_list:
        current_value = current_values[alarm.monitor_type]
        
        is_triggered = (alarm.condition == "above" and current_value > alarm.threshold) or \
                      (alarm.condition == "below" and current_value < alarm.threshold)
        
        if is_triggered:
            triggered_alarms.append(f"Warning Alarm is activated! {alarm.monitor_type.upper()}: {current_value}% (limit: {alarm.threshold}%)")

    return triggered_alarms
