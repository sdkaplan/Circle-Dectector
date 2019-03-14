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

image = cv.imread(filename, cv.IMREAD_COLOR)

Range = 10
numcircles = 0
print("boundaries = [")
width, height = image.shape[:2]
if circles is not None:
    # print(circles)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        numcircles = numcircles + 1

        # print(center)
        colorCenter = image[i[0], i[1]]
        radius = i[2]
        x = i[0]
        y = i[1]

        x_bound_upper = x + radius - 10
        x_bound_lower = x - radius + 10
        y_bound_upper = y + radius - 10
        y_bound_lower = y - radius + 10

        b, g, r, num = 0, 0, 0, 0
        for j in range(x_bound_lower, x_bound_upper):
            for k in range(y_bound_lower, y_bound_upper):
                if j < 0 or j >= width or k < 0 or k >= height:
                    continue
                if abs(j - x) > radius or abs(k - y) > radius:
                    continue
                b = b + image.item(j, k, 0)  # access the blue part of the pixel at center point
                g = g + image.item(j, k, 1)  # access the green part of the pixel at center point
                r = r + image.item(j, k, 2)  # access the red part of the pixel at center point
                num = num + 1

        red = round(r/num)
        green = round(g/num)
        blue = round(b/num)
        # print(str(red) + ' ' + str(green) + ' ' + str(blue))

        # Find the upper and lower boundaries
        RedUpper = red + Range
        RedLower = red - Range

        GreenUpper = green + Range
        GreenLower = green - Range

        BlueUpper = blue + Range
        BlueLower = blue - Range

        center = (i[0], i[1])


        cv.circle(src, center, radius, (int(blue), int(green), int(red)), 36)
        # number circles
        cv.putText(src, str(numcircles), center, cv.FONT_HERSHEY_PLAIN, 10, (0, 0, 0), 2)


        # Prints the Proper Format for detect_color
        # print(numcircles)
        print("    ([%d, %d, %d], [%d, %d, %d])," % (BlueLower, GreenLower, RedLower, BlueUpper, GreenUpper, RedUpper))
else:
    print("no cicles found")

print(']')
src = cv.resize(src, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
cv.imshow("detected circles", src)
cv.waitKey(0)