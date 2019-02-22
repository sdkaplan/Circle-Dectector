import cv2 as cv
import numpy as np

filename = cv.imread('Frame2.1.jpg')

# Hough transform
src = cv.imread(filename, cv.IMREAD_COLOR)  # Reads the file name and stores it as src
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=100, param2=15,
                                  minRadius=20, maxRadius=100)

Range = 10
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # finds center and stores the value
        center = (i[0], i[1])
        blue = filename(i[0], i[1], 0)  # access the blue part of the pixel at center point
        green = filename(i[0], i[1], 1)  # access the green part of the pixel at center point
        red = filename(i[0], i[1], 0)  # access the red part of the pixel at center point

        # Find the upper and lower boundaries
        RedUpper = red + Range
        RedLower = red - Range

        GreenUpper = green + Range
        GreenLower = green - Range

        BlueUpper = blue + Range
        BlueLower = blue - Range

        # Prints the Proper Format for detect_color
        print("([%d , %d , %d] , [%d , %d , %d])" % (BlueLower, GreenLower, RedLower, BlueUpper, GreenUpper, RedUpper))
else:
    print("no cicles found")