# This file is not meant to be used but rather for testing.
print("\nThis file is not meant to be used")

# Import of library
import pyautogui
import time     # This is used for benchmark the code
import pyscreeze

# This will disable the failsafe protocol.
# This protocol will enable a user to slam his mouse into a corner of the screen to forcefully stop the program.
pyautogui.FAILSAFE = False

# Function

# Timer, return the time upon call
def timer():
    return time.time()

# Code

# Find the left hand
posX, posY, width, height = pyautogui.locateOnScreen("img/leftHand.png", confidence=0.8)
leftHand = int(posX), int(posY), int(width), int(height)
pyautogui.moveTo(leftHand[0]+leftHand[2], leftHand[1]+10)

# Find the right hand
posX, posY, width, height = pyautogui.locateOnScreen("img/rightHand.png", confidence=0.8)
rightHand = int(posX), int(posY), int(width), int(height)
pyautogui.moveTo(rightHand[0], leftHand[1]+11)

pyscreeze.screenshot("img/test.png", region=(leftHand[0]+leftHand[2], leftHand[1]+10, rightHand[0], rightHand[1]+10))

# Get length between left and right
section1 = (rightHand[0]) - (leftHand[0]+leftHand[2])
print(section1)

# Get pixel list
print(type(leftHand[0]))
print(type(leftHand[1]))
print(type(leftHand[2]))
print(type(leftHand[3]))

pixelList = []
i=0
while i < section1:
    value = pyautogui.pixel(int(leftHand[0] + leftHand[2] + i), int(leftHand[1] + 10))
    pixelList.insert(i, value)
    
    i = i + 1
    
print(pixelList[0])
print(pixelList)
    




# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()

# Get current mouse position.
currentMouseX, currentMouseY = pyautogui.position()

# Move mouse to new position.
#pyautogui.moveTo(100, 50)

# Move mouse to new position based on image
# If the image the app compare to isn't exact it will throw an error
#pyautogui.moveTo('img/search.png')
#pyautogui.moveTo('img/commit.png')
#pyautogui.moveTo('img/run.png')
#pyautogui.moveTo('img/extension.png')
#pyautogui.click()

# Make an alert box and pause the program until ok is selected.
#pyautogui.alert("This is the display message")

# Printing to terminal.
#print("Screen width:", screenWidth)
#print("Screen height:", screenHeight)
#print("Mouse X pos:", currentMouseX)
#print("Mouse Y pos:", currentMouseY)
print() # Last print, to prevent terminal clutter and improve readability.