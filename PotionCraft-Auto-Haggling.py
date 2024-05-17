# Importation of library.
import pyautogui
import time

#   TODO:
#   - Testing mapping 1 pixel large screenchot to find the corresponding color, map cursor and compare.
#       - Done with PyAutoGUIn for fast screenshot processing and ease of use
#   - Using PyAutoGUI for automatically find the correct position for different resolution.
#   - Creation of an AI model and train to recognise zone.
#       - Might be to heavy for purpose of this tool.
    

# Disable failsafe for faster code, remove the 0.1s delay after each pyautogui function
pyautogui.FAILSAFE= False

# Function

# Code

# Main loop
while True:
    try:
        # Search for the profit text on the screen
        posX, posY, width, height = pyautogui.locateOnScreen("img/profit.png", confidence=0.9)
        pyautogui.moveTo(posX, posY)
        
        # Locate the zone to capture and set the capture zone
        left, top, width, height  = pyautogui.locateOnScreen("img/zoneToCapture.png", confidence=0.7) # Confidence set to 0.7 for icon not matching
        regionToCapture = int(left), int(top), int(width), int(height) # Set the region to capture, force int into value
        
        # Locate the left and right hand in the region.
        posX, posY, width, height = pyautogui.locateOnScreen("img/leftHand.png", confidence=0.9, region=regionToCapture)
        pyautogui.moveTo(posX, posY)
        posX, posY, width, height = pyautogui.locateOnScreen("img/rightHand.png", confidence=0.9, region=regionToCapture)
        pyautogui.moveTo(posX, posY)
        
        # Find zoneMedium1 in the region.
        posX, posY, width, height = pyautogui.locateOnScreen("img/zoneDisapear1.png", confidence=0.5 , region=regionToCapture)
        pyautogui.moveTo(posX, posY)
        i =0
        while i<20:
            posX, posY, width, height = pyautogui.locateOnScreen("img/cursor.png", confidence=0.5, region=regionToCapture)
            pyautogui.moveTo(posX, posY)
            i = i+1
        
    except pyautogui.ImageNotFoundException:
        print("Image not found!, make sure the game is visible on main screen")
    except Exception:
        print("An Error occurred!")
    break


