import cv2
from random import randrange
train_face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#img=cv2.imread('rdj.png')
webcam=cv2.VideoCapture('video.mkv')
while True:
    successful_frame_read,frame=webcam.read()
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_coordinates=train_face.detectMultiScale(gray_img)

    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,randrange(128,256)),5)

#print(face_coordinates)
    cv2.imshow('face detected',frame)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break;
webcam.release() 


print("code completed")