import cv2 as cv

# Reading Image
# img = cv.imread('https://raw.githubusercontent.com/sahilpatni95/Opencv-projects/main/Data/Photos/cat.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)


# Reading Videos
capture = cv.VideoCapture('https://raw.githubusercontent.com/sahilpatni95/Opencv-projects/main/Data/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

