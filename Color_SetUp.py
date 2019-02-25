import cv2 as cv
import numpy as np

filename = "Frame3.1.jpg"

# Hough transform
src = cv.imread(filename, cv.IMREAD_COLOR)  # Reads the file name and stores it as src
# src = cv.resize(src, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 150, param1=190, param2=15,
                            minRadius=200, maxRadius=250)

image = cv.imread(filename)

Range = 10
numcircles = 0
print("boundaries = [")
if circles is not None:
    print(circles)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        numcircles = numcircles + 1


        # print(center)
        colorCenter = image[i[0], i[1]]
        # blue = colorCenter[2]
        # green = colorCenter[1]
        # red = colorCenter[0]
        x = 846.5
        y = 1629.5
        blue = image.item(int(x), int(y), 0)  # access the blue part of the pixel at center point
        green = image.item(int(x), int(y), 1)  # access the green part of the pixel at center point
        red = image.item(int(x), int(y), 2)  # access the red part of the pixel at center point

        # print(str(red) + ' ' + str(green) + ' ' + str(blue))

        # Find the upper and lower boundaries
        RedUpper = red + Range
        RedLower = red - Range

        GreenUpper = green + Range
        GreenLower = green - Range

        BlueUpper = blue + Range
        BlueLower = blue - Range

        center = (i[0], i[1])
        radius = i[2]

        cv.circle(src, center, radius, (int(red), int(green), int(blue)), 36)
        # number circles
        cv.putText(src, str(numcircles), center, cv.FONT_HERSHEY_PLAIN, 10, (0, 0, 0), 2)


        # Prints the Proper Format for detect_color
        # print(numcircles)
        # print("    ([%d, %d, %d], [%d, %d, %d])," % (BlueLower, GreenLower, RedLower, BlueUpper, GreenUpper, RedUpper))
else:
    print("no cicles found")

print(']')
src = cv.resize(src, None, fx=0.25, fy=0.25, interpolation=cv.INTER_CUBIC)
cv.imshow("detected circles", src)
cv.waitKey(0)
