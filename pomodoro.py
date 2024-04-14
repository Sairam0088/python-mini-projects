#pomodoro timer using python
import time
import winsound

def pomodoro_timer(work_minutes=25, short_break=5, long_break=15, cylces=4, cylces_completed=0):
    for i in range(cylces):
        print(f"Work for {work_minutes} minutes.")
        time.sleep(work_minutes * 60)
        print(f"Take a short break for {short_break} minutes.")
        time.sleep(short_break * 60)
        cylces_completed += 1
        if cylces_completed % 4 == 0:
            print(f"Take a long break for {long_break} minutes.")
            time.sleep(long_break * 60)
    print("Pomodoro timer completed")
    for i in range(3):
        winsound.Beep(1000, 1000)

pomodoro_timer(1,0.25,0.5)
