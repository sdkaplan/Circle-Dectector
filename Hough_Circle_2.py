import sys
import cv2 as cv
import numpy as np
import random


def main(argv):
    default_file = 'Test13.png'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    gray = cv.medianBlur(gray, 5)

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20,
                              param1=100, param2=30,
                              minRadius=10, maxRadius=100)

    radii = []
    centerPoints = [[] for i in range(15)]
    colors = []
    for i in range(0, 15):
        #fills colors[] with random colors
        colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    if circles is not None:
        circles = np.uint16(np.around(circles))
        j = 0
        for i in circles[0, :]:
            # if i == 1:
                # centerPoints[j]= np.zeros()
            center = (i[0], i[1])
            centerPoints[j].append(center)
            # circle center
            cv.circle(src, center, 1, colors[j], 3)
            # circle outline
            radius = i[2]
            radii.append(radius)
            cv.circle(src, center, radius, colors[j], 3)
            #number circles
            cv.putText(src, str(j+1), center, cv.FONT_HERSHEY_PLAIN, 2, colors[j], 2)
            j = j + 1

    #print('center points', centerPoints)
    print('radii ', radii)
    print(colors)

    #src = cv.resize(src, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
    cv.imshow("detected circles", src)
    cv.waitKey(0)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])