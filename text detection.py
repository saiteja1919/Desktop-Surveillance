''' program to find present tab in browser
'''
# both modules should be installed
import pytesseract
import cv2 as cv

# Tesseract OCR.exe is required to run the program
# path of tesseract ocr should be specified below
pytesseract.pytesseract.tesseract_cmd = r"...\Tesseract-OCR\tesseract.exe"

# path of image to be read
value = cv.imread('test images/test19june.png')

text = pytesseract.image_to_string(value)

'''
finds the index of https and prints the text after https:// and prints
upto next occurrence of /
'''
test_start = 0
flag = 0
try:
    while 1:
        bas = 'https'   # a case for http can be added if required
        start = (text[test_start:].index(bas))
        end = text[start+7:].index('/')
        end += start + 7
        for f in range(start, end-1):
            if ord(text[f]) == 47:
                req = f+1
        print('opened website :  ', text[start:end])
        flag = 1
        test_start += end
except ValueError:
    if flag == 0:
        print('Unknown website')

# image should be of better quality for accurate result
