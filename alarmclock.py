import tkinter as tk
from datetime import datetime
import winsound  # Use winsound on Windows for sound
# Alternatively, use the cross-platform playsound
# from playsound import playsound

class AlarmClock:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        
        # Create widgets
        self.time_label = tk.Label(self.root, text="Set Alarm Time (HH:MM):")
        self.time_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.time_entry = tk.Entry(self.root)
        self.time_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.set_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.set_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)
        
        # Initialize variables
        self.alarm_time = None
        self.alarm_active = False
        
        # Start checking the time
        self.check_time()
        
        # Start the main loop
        self.root.mainloop()
    
    def set_alarm(self):
        # Get the alarm time from the entry
        alarm_time_str = self.time_entry.get()
        try:
            # Convert the time string to a datetime.time object
            alarm_hour, alarm_minute = map(int, alarm_time_str.split(":"))
            self.alarm_time = datetime.now().replace(hour=alarm_hour, minute=alarm_minute, second=0)
            
            # Update alarm state
            self.alarm_active = True
            self.set_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            print(f"Alarm set for {alarm_time_str}")
        except ValueError:
            print("Invalid time format. Please enter time as HH:MM.")
    
    def stop_alarm(self):
        # Stop the alarm
        self.alarm_active = False
        self.set_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        print("Alarm stopped.")
    
    def check_time(self):
        # Check the current time
        current_time = datetime.now()
        
        if self.alarm_active and current_time >= self.alarm_time:
            # Alarm time reached, play sound and stop the alarm
            winsound.Beep(1000, 1000)  # Frequency: 1000 Hz, Duration: 1000 ms
            self.stop_alarm()
        
        # Schedule the next time check
        self.root.after(1000, self.check_time)

# Create the alarm clock
alarm_clock = AlarmClock()
