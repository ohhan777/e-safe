import time
import pyautogui

# user-specific positions
next_button = (4910, 390)
ok_button = (4573, 176)
found_pos = True

while (True):
    if found_pos == True:
        pos = pyautogui.position()
        pyautogui.moveTo(next_button[0], next_button[1])
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(ok_button[0], ok_button[1])
        pyautogui.click()
        pyautogui.moveTo(pos.x, pos.y)
        time.sleep(60)
    else:
        pos = pyautogui.position()
        print(pos)
        time.sleep(0.01)


