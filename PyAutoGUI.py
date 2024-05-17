# This file is not meant to be used but rather for testing.
print("\nThis file is not meant to be used")

# Import of library
import pyautogui
import time     # This is used for benchmark the code

# Function

# Timer, return the time upon call
def timer():
    return time.time()

# Code

# This will disable the failsafe protocol.
# This protocol will enable a user to slam his mouse into a corner of the screen to forcefully stop the program.
#pyautogui.FAILSAFE = False

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