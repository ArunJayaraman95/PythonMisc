import pyautogui as pg
import time
print(pg.size())

#time.sleep(10)
#pg.moveTo(1858, 108, duration = 0.5)
#pg.click()
#pg.moveTo(1805, 1005)
for i in range(6):
    if i == 9:
        print("NEW CYCLE")
    pg.moveTo(1858, 108, duration = 0.5)
    pg.click()
    time.sleep(2.5)
    pg.click(1850, 1005)
    time.sleep(30)
# for j in range(12):
#     NUM_EMAILS = 10
#     for i in range(NUM_EMAILS):
#         pg.click(105,191)
#         time.sleep(0.1)
#         pg.click(1562, 132)
#         time.sleep(0.5)
#         pg.click(1056, 184)
#     pg.click(87,52)
#     time.sleep(1)
time.sleep(3)
print(pg.position())