# School-Task-
A up comming school task for a survaillence application 

Project Description

This project is a system monitoring application written in Python. The program runs in the console and provides a simple menu interface that allows the user to:

Start monitoring of CPU, memory, and disk usage

List current monitoring status

Create and configure alarms (e.g., CPU > 80%)

View all configured alarms, sorted by type

Enter a monitoring mode where system resources are checked continuously and alarms are triggered if thresholds are exceeded



├── main.py                 # Körbar fil med huvudmenyn

├── monitor.py              # Funktioner för att övervaka systemresurser

├── alarm_manager.py        # Skapa, visa, ta bort larm

├── logger.py               # Loggning av händelser

├── persistence.py          # Spara/ladda larm till/från JSON

├── utils.py                # Hjälpfunktioner (validering, formatering etc.)
├── logs/
│   └── log_2024-09-20_15-05.txt

├── alarms.json             # Sparade larm

└── README.md               # Denna fil
