import cv2 as cv

# Reading images
# img = cv.imread('/vscode/Opencvnew/photos/cat_large.jpg')

# cv.imshow('cat', img)
# cv.waitKey(0)


# Reading Videos 
capture = cv.VideoCapture('/vscode/Opencvnew/videos/dog.mp4')
# VideoCapture(0) for webcam

while True:
    isTrue, frame = capture.read()

# Grabss video frame by frame, and the boolean isTrue says whether video was successfully read it or not
    cv.imshow('Video', frame) #to display video

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
# if we press the letter d then breaks out of the loop

capture.release()
#finally release
cv.destroyAllWindows()


