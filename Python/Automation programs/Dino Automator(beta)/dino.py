import pyautogui as gui
import time
import keyboard
time.sleep(2)
gui.press("space")
while True:
    x1,x2,x3,x4=0,0,0,0
    try:
        x1,y1=gui.locateCenterOnScreen("double small.png", confidence=0.55  ,region=(562,350,323,175))
    except:
        x1=0
    try:
        x2,y2=gui.locateCenterOnScreen("single big.png", confidence=0.55  ,region=(562,350,323,175))
    except:
        x2=0
    try:
        x3,y3=gui.locateCenterOnScreen("single small.png", confidence=0.55  ,region=(562,350,323,175))
    except:
        x3=0
    try:
        x4,y4=gui.locateCenterOnScreen("triple small.png", confidence=0.55  ,region=(562,350,323,175))
    except:
        x4=0
    if x1>0 or x2>0 or x3>0 or x4>0:
        gui.press("space")
    if keyboard.is_pressed('p'):
        break

