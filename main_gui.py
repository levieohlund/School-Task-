import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
import monitor
from alarm import create_alarm_menu, show_alarms_menu, check_alarms, alarms, add_alarm

class MonitoringGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitoring Application")
        self.root.geometry("800x600")
        
        # Variables
        self.monitoring = False
        self.monitoring_thread = None
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="System Monitoring Application", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Current Values Frame
        values_frame = ttk.LabelFrame(main_frame, text="Current System Values", padding="10")
        values_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.cpu_label = ttk.Label(values_frame, text="CPU Usage: ---%")
        self.cpu_label.grid(row=0, column=0, sticky=tk.W, pady=2)
        
        self.memory_label = ttk.Label(values_frame, text="Memory Usage: ---%")
        self.memory_label.grid(row=1, column=0, sticky=tk.W, pady=2)
        
        self.disk_label = ttk.Label(values_frame, text="Disk Usage: ---%")
        self.disk_label.grid(row=2, column=0, sticky=tk.W, pady=2)
        
        # Buttons Frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0))
        
        ttk.Button(buttons_frame, text="Update Values", 
                  command=self.update_values).grid(row=0, column=0, padx=5)
        
        ttk.Button(buttons_frame, text="Create Alarm", 
                  command=self.create_alarm_dialog).grid(row=0, column=1, padx=5)
        
        ttk.Button(buttons_frame, text="Show Alarms", 
                  command=self.show_alarms).grid(row=0, column=2, padx=5)
        
        self.monitor_btn = ttk.Button(buttons_frame, text="Start Monitoring", 
                                     command=self.toggle_monitoring)
        self.monitor_btn.grid(row=0, column=3, padx=5)
        
        # Output Text Area
        output_frame = ttk.LabelFrame(main_frame, text="Output Log", padding="10")
        output_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=15, width=80)
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        # Initial update
        self.update_values()
        
    def log_message(self, message):
        """Add message to output text area"""
        self.output_text.insert(tk.END, f"{time.strftime('%H:%M:%S')} - {message}\n")
        self.output_text.see(tk.END)
        
    def update_values(self):
        """Update system values display"""
        try:
            cpu = monitor.get_cpu_usage()
            mem_pct, mem_used, mem_total = monitor.get_memory_usage()
            disk_pct, disk_used, disk_total = monitor.get_disk_usage()
            
            self.cpu_label.config(text=f"CPU Usage: {cpu}%")
            self.memory_label.config(text=f"Memory Usage: {mem_pct}% ({mem_used/1024**3:.1f} GB out of {mem_total/1024**3:.1f} GB)")
            self.disk_label.config(text=f"Disk Usage: {disk_pct}% ({disk_used/1024**3:.1f} GB out of {disk_total/1024**3:.1f} GB)")
            
            self.log_message(f"Values updated - CPU: {cpu}%, Memory: {mem_pct}%, Disk: {disk_pct}%")
            
            # Check alarms
            triggered_alarms = check_alarms(cpu, mem_pct, disk_pct)
            for alarm_msg in triggered_alarms:
                self.log_message(f"🚨 {alarm_msg}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update values: {e}")
            
    def create_alarm_dialog(self):
        """Open dialog to create new alarm"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Create Alarm")
        dialog.geometry("300x200")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Alarm type
        ttk.Label(dialog, text="Alarm Type:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        alarm_type = ttk.Combobox(dialog, values=["cpu", "memory", "disk"])
        alarm_type.grid(row=0, column=1, padx=10, pady=5)
        alarm_type.set("cpu")
        
        # Threshold
        ttk.Label(dialog, text="Threshold (%):").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        threshold_var = tk.StringVar()
        threshold_entry = ttk.Entry(dialog, textvariable=threshold_var)
        threshold_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Condition
        ttk.Label(dialog, text="Condition:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        condition = ttk.Combobox(dialog, values=["above", "below"])
        condition.grid(row=2, column=1, padx=10, pady=5)
        condition.set("above")
        
        def create_alarm():
            try:
                threshold = int(threshold_var.get())
                if 1 <= threshold <= 100:
                    alarm = Alarm(alarm_type.get(), threshold, condition.get())
                    add_alarm(alarm)
                    self.log_message(f"Alarm created: {alarm}")
                    dialog.destroy()
                else:
                    messagebox.showerror("Error", "Threshold must be between 1-100")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")
        
        ttk.Button(dialog, text="Create", command=create_alarm).grid(row=3, column=0, columnspan=2, pady=20)
        
    def show_alarms(self):
        """Show all current alarms"""
        if not alarms:
            self.log_message("No alarms configured")
        else:
            self.log_message("Current Alarms:")
            for i, alarm in enumerate(alarms, 1):
                self.log_message(f"  {i}. {alarm}")
                
    def toggle_monitoring(self):
        """Start or stop continuous monitoring"""
        if not self.monitoring:
            self.start_monitoring()
        else:
            self.stop_monitoring()
            
    def start_monitoring(self):
        """Start continuous monitoring in separate thread"""
        self.monitoring = True
        self.monitor_btn.config(text="Stop Monitoring")
        self.log_message("Started continuous monitoring")
        
        self.monitoring_thread = threading.Thread(target=self.monitoring_loop, daemon=True)
        self.monitoring_thread.start()
        
    def stop_monitoring(self):
        """Stop continuous monitoring"""
        self.monitoring = False
        self.monitor_btn.config(text="Start Monitoring")
        self.log_message("Stopped continuous monitoring")
        
    def monitoring_loop(self):
        """Continuous monitoring loop"""
        while self.monitoring:
            # Update values in main thread
            self.root.after(0, self.update_values)
            time.sleep(5)

def main():
    try:
        import monitor
        import alarm
    except ImportError as e:
        messagebox.showerror("Error", f"Missing required modules: {e}")
        return
        
    root = tk.Tk()
    app = MonitoringGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()