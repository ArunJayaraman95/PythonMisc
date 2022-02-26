import pyautogui as p
import time
time.sleep(1)
# print(p.position())
#1752, 316
#1646, 414
p.PAUSE = 0.3
for _ in range(27):
    p.click(x=1752, y = 316)
    p.click(x=1646, y = 414)
    time.sleep(.7)