import cv2
import time
import os

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("https://video14.sputnik.systems/5da8b494-7f6e-45f1-b0f7-8e784b55415a/video1.ts")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

ct = 0 # кол-во кадров
while True:
    ct += 1
    ret = cap.grab()

    if ct % 15 == 0:
        ret, frame = cap.retrieve()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        
        for (x, y, w, h) in faces:
            face_image = frame[y:y+h, x:x+w]
            number = len(os.listdir('faces'))
            filename = f'faces/{number}.jpg'

            cv2.imwrite(filename, face_image)

            color = (255, 255, 0) # BGR COLOUR
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        
        cv2.imshow('VIDEO', frame)
    
    if cv2.waitKey(1) == 27:
        break
