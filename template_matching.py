import cv2 as cv
import numpy as np
import os
# all modules should be installed

if __name__ == '__main__':

    # path of source image should be secified
    img1 = cv.imread(r'...\test images\test19june.png')
    img = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

    # changing directory to favicon dir for verification
    os.chdir(r'...\test images\favicon')
    flag = 0
    for i in os.listdir():
        temp = cv.imread(i, cv.IMREAD_GRAYSCALE)
        w, h = temp.shape[::-1]
        # print('width : {}, height : {}'.format(w, h))

        result = cv.matchTemplate(img, temp, cv.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.85)
        if len(loc[0]) != 0:
            fn, _ = os.path.splitext(i)
            print('► opened : {}'.format(fn))
            flag = 1
            for pt in zip(*loc[::-1]):
                cv.rectangle(img1, pt, (pt[0] + w, pt[1] + h), (255, 79, 138), 2)
    if not flag:
        print('► Person is clear')
        # in case if its a screenshot of plane desktop
    cv.imshow('img', img1)
    cv.waitKey(0)
    cv.destroyAllWindows()


# applicable in : chrome, opera mini, mozilla
