import pyautogui
import time

time.sleep(2)                                   #delays the program to get mouse postion from wherever we want

#mouse functions

'''
print(pyautogui.size())                         #gets the resoution of monitor

print(pyautogui.position())                     #gives position of mouse

#pyautogui.moveTo(1764,28)                      #first 2 arguments are postions and the last argument is the time over which it will move

#pyautogui.moveRel(100,-100,3)                  #moves relative to current position, +Ve x is right, +ve y is down      #remember r is capital

#first 2 arguments can be like moveTo to save lines of code,3rd argument is number of clicks, duration of clicks(if more than 1 clicks) is 4th argument default of button is left
#pyautogui.click(1118,398,3,3,button='right')                 
'''
#more functions which can be used are doubleclick leftclick rightclick tripleclick

#scrolling,+ is up, - is down
#pyautogui.scroll(400)

#how to drag (mouse down means holding button)
'''pyautogui.mouseDown(500,500,button="left")
pyautogui.moveTo(800,500,2)
pyautogui.mouseUp()                                  #these 3 lines would draw a horizontal line in paint\
'''


#KEYBOARD FUNCTIONS
'''
pyautogui.write("hello")
pyautogui.press("enter")
'''

#MESSAGE BOX

#pyautogui.alert("Showing information")
#print(pyautogui.confirm("Also has an ok or cancel button"))   #returns OK or Cancel
#pyautogui.prompt("Asks the user")

#SCREENSHOT

#pyautogui.screenshot("ss.jpg")
#obj1=pyautogui.locateOnScreen("image")   #returns (left, top, width, height) of first place it is found     #left,top=starting x and y   #width,height= ending x,y (relative) that is why width and height
#obj2=list(pyautogui.locateAllOnScreen("image"))  #returns all positions, better to convert to list
x,y=pyautogui.locateCenterOnScreen("image", confidence=0.7 , region=(100,10,102,102))   #returns center x and y   #confidence is the % match between image and element on screen betweeen 0 and 1

