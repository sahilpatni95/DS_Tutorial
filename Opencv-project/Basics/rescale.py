import cv2 as cv

# Reading Image
git_url = 'https://raw.githubusercontent.com/sahilpatni95/Opencv-projects/main/Data/Photos/cat_large.jpg'

def rescaleFrame(frame, scale=0.75):
    # Work with Image, Videos and live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions,interpolation = cv.INTER_AREA)

def changeRes(width, height):
    # only work with live videos(cum)
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread(git_url)
cv.imshow('Cat', img)

resized_image = rescaleFrame(img, scale = .2)
cv.imshow('Image', resized_image)

cv.waitKey(0)


#Reading Videos
capture = cv.VideoCapture('https://raw.githubusercontent.com/sahilpatni95/Opencv-projects/main/Data/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale = .5)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)
