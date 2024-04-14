# countdown timer using python
import time

def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        t -= 1
    print("Time is Up!")
t = int(input('Enter a time in secs: '))
countdown(t)
