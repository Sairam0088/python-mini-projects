import pyautogui as p
import time
import random

time.sleep(5)
otp = [4568,9563,7895,8526,7852,2145,7412,5632,9563]
randotp = []
for i in range(25):
    randotp.append(random.choice(otp))
for j in randotp:
    p.write(f"your otp is {j}")
    p.press('enter')