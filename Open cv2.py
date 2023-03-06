import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(0)

while True:
    ret_,image=cam.read()
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, image3) = cv2.threshold(image2, 122.5, 255, cv2.THRESH_BINARY)
    cv2.imshow('Frame',image)
    cv2.imshow('Frame1', image3)

    if cv2.waitKey(20)&0xff==27:
        break
        cam.release()
        cv2.destroyAllWindows()

