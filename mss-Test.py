import mss
import mss.tools
from PIL import Image
import pyautogui
import time

def timer():
    """
    Start a timer

    Returns:
        float: return the time
    """
    return time.time()

def locateOnScreen(filename, confidence=0.7):
    """
    Locate an element on the screen based on an image

    Args:
        filename (string): String containing image path
        confidence (float, optional): Determine the confidence. Defaults to 0.7.

    Returns:
        int: Return coordinate, width and height of the element
    """
    posX, posY, width, height = pyautogui.locateOnScreen(filename, confidence=confidence)
    return int(posX), int(posY), int(width), int(height)

def screenshot(posX, posY, width, height):
    """
    Take a screenshot of a certain region

    Args:
        posX (_type_): Left most position
        posY (_type_): Top most position
        width (_type_): Width desired
        height (_type_): height desired

    Returns:
        image: standard image
    """
    with mss.mss() as sct:
        monitor = {
            "left" : posX,
            "top" : posY,
            "width" : width,
            "height" : height
        }
        screenshot = sct.grab(monitor)
        #mss.tools.to_png(screenshot.rgb, screenshot.size, output="img/mss-test.png")
        return screenshot
    
def convertToPILImage(screenshot):
    """ 
    Convert an image to a PIL Image

    Args:
        screenshot (image): standard image

    Returns:
        image: PIL Image (Grayscale)
    """
    # Convert screenshot to PIL image
    img = Image.frombytes('RGB', screenshot.size, screenshot.bgra, "raw", "BGRX")
    # Convert to grayscale
    return img.convert("L")

def detectPixelInRange(pixelList, minValue=97, maxValue=105):
    """
    Detect pixel values within a specified range.

    Args:
        pixelList (list of int): List of grayscale pixel values.
        minValue (int): Minimum value of the range (inclusive).
        maxValue (int): Maximum value of the range (inclusive).

    Returns:
        list of int: List of positions where pixel values are within the range.
    """
    positions = []
    
    for i, value in enumerate(pixelList):
        if minValue <= value <= maxValue:
            positions.append(i)
    
    return positions

def getPixelValuePIL(img):
    """
    Get the pixel value within an image 

    Returns:
        list of ints: Return a list of pixel value
    """
    # Get pixel value into list
    pixelValues = []
    # For each pixel within the width
    for y in range(img.width):
        # Get pixel value
        pixelValue = img.getpixel((y, 0))
        # Store pixel value
        pixelValues.append(pixelValue)
    return pixelValues
        
        
# Find the left and right hand
leftHand = locateOnScreen("img/leftHand.png")
rightHand = locateOnScreen("img/rightHand.png")

# Defining the region to capture
left = leftHand[0] + leftHand[2]
top = leftHand[1] + 10
width = rightHand[0] - rightHand[2] - leftHand[0]
height = 1

# Take a screenshot of the region
img = screenshot(left, top, width, height)

# Convert the image into a pil grayscale image
imgGray = convertToPILImage(img)
imgGray.save("img/test.png")

print(detectPixelInRange(getPixelValuePIL(imgGray)))
    
#print(pixelValues)

