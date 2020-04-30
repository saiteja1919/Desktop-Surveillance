'''
program to test a cropped image 
'''
import cv2 as cv
import numpy as np
import os

# all modules should be installed
'''
 https://www.iloveimg.com/crop-image
 crop any image in above website for requied icon size
'''

if __name__ == '__main__':
    # source image
    img1 = cv.imread(r'...\test images\incog.png')
    img = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

    # changing directory to cropped icon
    os.chdir(r'...\test images\favicon1')
    i = os.listdir()[0]
    temp = cv.imread(i)  # reading icon

    tempt = temp  # retaining colour image
    temp = cv.cvtColor(temp, cv.COLOR_BGR2GRAY)  # conversion to grey

    w, h = temp.shape[::-1]  # obtaining dimensions for further use
    # print('width : {}, height : {}'.format(w, h))
    result = cv.matchTemplate(img, temp, cv.TM_CCOEFF_NORMED)  # template matching
    loc = np.where(result >= 0.85)

    if len(loc[0]) != 0:
        fn, _ = os.path.splitext(i)
        print('► opened : {}'.format(fn))
        for pt in zip(*loc[::-1]):
            cv.rectangle(img1, pt, (pt[0] + w, pt[1] + h), (255, 0, 255), 2)

    
    '''
    save the image in favicon directory if the icon size is accurate for measurment
    '''
    cv.imshow('tempt', tempt)
    cv.imshow('img', img1)

    cv.waitKey(0)
    cv.destroyAllWindows()

# drawback--> full screen screenshots cannot be detected
