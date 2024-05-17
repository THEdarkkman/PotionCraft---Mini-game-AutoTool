# OpenCV
import OpenCV
#Load an image using fileName, -1 ignore transparency, 0 load in grayscale, 1 load image as is
#img = cv2.imread("img/leftHand.png", -1)
#img = cv2.resize(img, (0, 0), fx=2, fy=2)

#cv2.imshow("image", img)
#cv2.waitKey(0)                              # Wait for a key input for x seconds, 0 = infinte
#cv2.destroyAllWindows()                     # Close all OpenCV windows

img = cv2.imread("img/zoneToCapture.png", 0)
template = cv2.imread("img/zoneSmall1.png", 0)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) 
    print(min_loc, max_loc)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
        
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow("Match", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()