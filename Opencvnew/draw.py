import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv2.imshow('blank',blank)

#1. paint the image a color

blank[200:300,300:400] = 0,255,0
cv2.imshow('Green', blank)

#2. Draw a rectangle

cv2.rectangle(blank, (0,0),(250,500),(0,255,0), thickness=2)
#blank.shape[1]//2, blank.shape[0]//2
cv2.imshow('rectangle',blank)
cv2.waitKey()

# img = cv2.imread('/vscode/Opencvnew/photos/cat.jpg')
# cv2.imshow('img',img)
# cv2.waitKey(0)

#Write text
cv2.putText(blank, 'Hello', (225,225), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv2.imshow('Text', blank)