import sys
import cv2 as cv
import numpy as np
import random
from PIL import Image


def main(argv):

    radii = [85, 70, 79, 52, 65, 62, 66, 57, 41, 42, 26, 43]    # known radii values, refers to number of pixels
    centerPoints = [[] for i in range(12)]    # creates a list of 12 lists, one per circle
    colors = []
    for i in range(0, 12):
        # fills colors[] with random colors
        colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    frames = ['Frame1.png', 'Frame2.png']
    frames2 = ['1.jpg', '2.jpg']
    frames3 = frames2

    j = 0
    for frame in frames3:
        im = Image.open(frame)
        name = str(j+1) + '.png'
        im.save(name)
        frames3[j] = name
        print(frames3)
        j = j+1

    for frameNumber in frames3:
        filename = frameNumber
        # Loads an image
        src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)

        # preps image color for searching for circles
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        gray = cv.medianBlur(gray, 5)

        # searches for circles
        circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=10, maxRadius=100)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            circleNum = 0
            for i in circles[0, :]:
                radius = i[2]
                print('radii ' + str(i) + ' ' + str(radius))
                # Finds out which circle number it is
                for k in range(len(radii)):
                    if radii[k] == radius:
                        circleNum = k

                # finds center
                center = (i[0], i[1])
                centerPoints[circleNum].append(center)

                # draws circles
                cv.circle(src, center, radius, colors[circleNum], -3)

                # numbers circles
                cv.putText(src, str(circleNum + 1), center, cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

        # resize & prints frames with circles drawn and numbered
        src = cv.resize(src, None, fx=0.75, fy=0.75, interpolation=cv.INTER_CUBIC)
        cv.imshow(frameNumber, src)

    # prints out our array of center points
    print('center points')
    j = 1
    for i in centerPoints:
        print('circle #', j, ' ', i)
        j = j + 1

    cv.waitKey(0)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])