
import json

def log_alarm_created(alarm_type, threshold, condition):
    

    new_alarm = {
        "type": alarm_type,
        "threshold": threshold,
        "condition": condition
    }
    
    
    try:
        with open("alarm_log.json", "r") as file:
            alarms = json.load(file)
    except:
    
        alarms = []

  
    alarms.append(new_alarm)

    
    with open("alarm_log.json", "w") as file:
        json.dump(alarms, file, indent=2) 
