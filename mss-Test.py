import mss
import mss.tools
from PIL import Image
import pyautogui
import time

# Timer, return the time upon call
def timer():
    return time.time()

# Locate an element on the screen
def locateOnScreen(filename, confidence=0.7):
    posX, posY, width, height = pyautogui.locateOnScreen(filename, confidence=confidence)
    return int(posX), int(posY), int(width), int(height)

# Take a screenshot of the region
def screenshot(top, left, width, height):
    with mss.mss() as sct:
        monitor = {
            "left" : left,
            "top" : top,
            "width" : width,
            "height" : height
        }
        screenshot = sct.grab(monitor)
        mss.tools.to_png(screenshot.rgb, screenshot.size, output="img/mss-test.png")
        return sct.grab(monitor)
    
# Convert screenshot to PIL image and grayscale
def convertToPILImage(screenshot):
    # Convert screenshot to PIL image
    img = Image.frombytes('RGB', screenshot.size, screenshot.bgra, "raw", "BGRX")
    # Convert to grayscale
    return img.convert("L")

# Find the left and right hand
leftHand = locateOnScreen("img/leftHand.png")
rightHand = locateOnScreen("img/rightHand.png")

# Defining the region to capture
left = leftHand[0] + leftHand[2]
top = leftHand[1] + 10
width = rightHand[0] - rightHand[2] - leftHand[0]
height = 1
pyautogui.moveTo(leftHand[0] + leftHand[2], leftHand[1] + 10)
pyautogui.moveTo(rightHand[0], leftHand[1]+10)
# Take screenshot based on region
img = screenshot(left, top, width, height)
    
imgGray = convertToPILImage(img)

imgGray.save("test.png")

# Get pixel value into list
pixelValues = []
# For each pixel within the width
for y in range(imgGray.width):
    # Get pixel value
    pixelValue = imgGray.getpixel((y, 0))
    # Store pixel value
    pixelValues.append(pixelValue)

