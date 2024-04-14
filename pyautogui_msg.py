import pyautogui as p
import time
time.sleep(5)
for _ in range(100):
    p.write('Hello!')
    p.press('enter')