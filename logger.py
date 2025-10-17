# Enkel logger för att spara alarm-historik
import json

def log_alarm_created(alarm_type, threshold, condition):
    """Sparar information när ett nytt alarm skapas"""
    
    # Skapa ny post med information om alarmet
    new_alarm = {
        "type": alarm_type,
        "threshold": threshold,
        "condition": condition
    }
    
    # Försök att läsa befintlig fil
    try:
        with open("alarm_log.json", "r") as file:
            alarms = json.load(file)
    except:
        # Om filen inte finns eller är fel, skapa tom lista
        alarms = []
    
    # Lägg till det nya alarmet
    alarms.append(new_alarm)
    
    # Spara tillbaka till fil
    with open("alarm_log.json", "w") as file:
        json.dump(alarms, file, indent=2)
