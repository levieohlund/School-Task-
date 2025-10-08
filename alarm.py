#list for alarm 
alarms = []

class Alarm:
    def __init__(self, metric, threshold, condition):
        self.metric = metric  # 'cpu', 'memory', or 'disk'
        self.threshold = threshold  # percentage value
        self.condition = condition  # 'above' or 'below'

    def __str__(self):
        return f"Alarm: {self.metric} {self.condition} {self.threshold}%"

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
            try:
                level = int(input("Set alarm level (1–100): "))
                if 1 <= level <= 100:
                    print("1. Above threshold (alarm when usage goes OVER X%)")
                    print("2. Below threshold (alarm when usage goes UNDER X%)")
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
        for idx, alarm in enumerate(alarms, start=1):
            print(f"{idx}. {alarm}")
    input("\nPress Enter to continue...")
    
def check_alarms(cpu, memory, disk):
    current_values = {"cpu": cpu, "memory": memory, "disk": disk}
    triggered_alarms = []

    for alarm in alarms:
        if alarm.metric in current_values:
            if alarm.condition == "above" and current_values[alarm.metric] > alarm.threshold:
                triggered_alarms.append(f"Triggered: {alarm}")
            elif alarm.condition == "below" and current_values[alarm.metric] < alarm.threshold:
                triggered_alarms.append(f"Triggered: {alarm}")

    return triggered_alarms

    # Returnera listan
