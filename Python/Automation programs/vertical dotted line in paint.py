import pyautogui
import time
import keyboard

time.sleep(2)
y=183
while True:
    y=y+20
    if pyautogui.position()[1]>950:
        pyautogui.scroll(-500)
        y=183
        pyautogui.moveTo(935,y+1)
    pyautogui.mouseDown(935,y,button='left')
    pyautogui.moveTo(935,y+1)
    pyautogui.mouseUp()
    if keyboard.is_pressed('p'):
        break