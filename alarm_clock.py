# simple alarm clock using python
import time
import winsound # this library is only used in windows for playing sound

def set_alarm():
    alarm_time = input('Enter the time in 24 hr format (HH:MM): ')
    current_time = time.strftime('%H:%M')
    
    while current_time != alarm_time:
        current_time = time.strftime('%H:%M')
        
    print(f'Alarm! Wakeup {current_time}')
    winsound.Beep(1000, 2000) #beep sound in 1000 hz for 2 secs

print('Simple Alarm Clock')
set_alarm()
