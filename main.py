import cv2
import random
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)

CATCH_FACES = False # сохранять лица в кадре

while True:
    ret, img = cap.read()

    k = cv2.waitKey(30) # номер введеной кнопки

    # кнопка выхода (ESC)
    if k == 27:
        break
    
    # кнопка захвата экрана (ENTER)
    if k == 13:
        filename = f'faces/ENTER_{random.randint(100000, 999999)}.jpg'
        cv2.imwrite(filename, img)
    
    # преобразование картинки в ч/б
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.1, 4) # все лица в кадре
    if len(faces) > 0 and CATCH_FACES:
        # сохранение лиц в папке faces
        number = len(os.listdir('faces'))
        filename = f'faces/{number}.jpg'

        cv2.imwrite(filename, img)

    # отрисовка прямоугольника
    for (x, y, w, h) in faces:
        color = (255, 255, 0) # BGR COLOUR
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
    
    cv2.imshow('img', img)

cap.release() 