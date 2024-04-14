#desktop notifier using python
from plyer import notification
#battery percentage notifier
import psutil
import time

def notifier(title, message):
    notification.notify(
        title = title,
        message = message,
        timeout = 10
    )

while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    title = "Develop with Python"
    message = f"{percent}% Battery Remaining"
    notifier(title, message) # notification after every hour
    time.sleep(60*60) # sleep for one hour
    continue
