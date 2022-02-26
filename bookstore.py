import pyautogui as p
import time

time.sleep(5)

def tab(x = 1):
    for _ in range(x):
        p.press('tab')

tab(2)
classes = ['CSC 6800 10695', 'CSC 6580 14425', 'STA 5030 18289', 'CSC 5430 12016', 'CSC 5431 12017']
i = 0.05
def enterClass(x):
    p.write(x.split()[0], interval = i)
    tab()
    p.write(x.split()[1], interval = i)
    tab()
    p.write(x.split()[2], interval = i)
    tab(4)

for c in classes:
    enterClass(c)
