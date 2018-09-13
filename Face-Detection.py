import cv2
import time
dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
while True:
    ret, img = capture.read()
    if ret:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 4)
            cv2.imshow('img',img)
        time.sleep(5)     
        if cv2.waitKey(1) == 27:
            break
    else:
        print ("The Code says Camera not Working")
capture.release()
cv2.destroyAllWindows()
