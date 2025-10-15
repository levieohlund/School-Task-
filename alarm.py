#list for alarm 
alarms = []

class Alarm: #Alarm class to hold alarm details
    def __init__(self, monitor_type, threshold, condition): 
        self.monitor_type = monitor_type  # 'cpu', 'memory', or 'disk'
        self.threshold = threshold  # percentage value
        self.condition = condition  # 'above' or 'below'

    def __str__(self): #String representation of the alarm
        return f"Alarm: {self.monitor_type} {self.condition} {self.threshold}%"

def add_alarm(alarm):
    alarms.append(alarm)

def list_alarms():
    return alarms 


def create_alarm_menu():
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

            try: # Försök att sätta alarmnivå
                level = int(input("Set alarm level (1–100): ")) # Sätt alarmnivå
                if 1 <= level <= 100:
                    print("1. Above threshold (alarm when usage goes over X%)")
                    print("2. Below threshold (alarm when usage goes under X%)")
                    condition = input("Choose alarm condition: ").strip()
                    if condition == "1":
                        add_alarm(Alarm(alarm_type, level, "above"))
                    elif condition == "2":
                        add_alarm(Alarm(alarm_type, level, "below"))
                    else:
                        print("Invalid condition.")
                else:
                    print("Value must be between 1–100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice.")


def show_alarms_menu():
    print("\n--- Active Alarms ---")
    if not alarms:
        print("No active Alarms.")
    else:
        for idx, alarm in enumerate(alarms, start=1): # Enumerate alarms for display 
            print(f"{idx}. {alarm}")
    input("\nPress Enter to continue...")
    
def check_alarms(cpu, memory, disk):
    current_values = {"cpu": cpu, "memory": memory, "disk": disk}
    triggered_alarms = []

    for alarm in alarms:
        if alarm.monitor_type in current_values: # Kontrollera om alarmets monitor_type finns i current_values
            current_value = current_values[alarm.monitor_type] # Hämta det aktuella värdet för monitor_type
            if alarm.condition == "above" and current_value > alarm.threshold: # Kontrollera om villkoret är uppfyllt
                triggered_alarms.append(f" Warning Alarm is Activated: {alarm.monitor_type.upper()} is {current_value}% (above {alarm.threshold}%)")
            elif alarm.condition == "below" and current_value < alarm.threshold:
                triggered_alarms.append(f" Warning Alarm is Activated: {alarm.monitor_type.upper()} is {current_value}% (below {alarm.threshold}%)")

    return triggered_alarms

    # Returnera listan
