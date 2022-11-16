import cv2
import face_recognition

import time
import os

import pickle

from api import Intercom

intercom = Intercom()

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(intercom.stream_url) # стрим

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml') # натренированный каскад


SAVE_FACES = False # сохранять лица
FACE_RECOGNITION_ENABLE = True # распознавать лица

with open('data.pickle', 'rb') as f:
    encodings_db = pickle.load(f) # кодировки всех лиц


frames_count = 0 # кол-во кадров

while True:
    frames_count += 1
    ret = cap.grab()

    if frames_count % 10 == 0:
        ret, frame = cap.retrieve()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # серая картинка

        faces = face_cascade.detectMultiScale(gray, 1.3, 2)
        
        for (x, y, w, h) in faces:
            face_image = frame[y:y+h, x:x+w] # обрезка изображения

            # сохранение лица в папку
            if SAVE_FACES:
                number = len(os.listdir('faces'))
                filename = f'faces/{number}.jpg'

                cv2.imwrite(filename, face_image)

            if FACE_RECOGNITION_ENABLE:
                try:
                    face_encodings = face_recognition.face_encodings(face_image)[0] # данные лица
                except IndexError:
                    continue

                compare_result = face_recognition.compare_faces(encodings_db, face_encodings) # сравнение лица с базой данных

            if FACE_RECOGNITION_ENABLE and True in compare_result:
                #intercom.open_door() # открытие домофона

                color = (0, 255, 0) # зеленый цвет в BGR
            else:
                color = (0, 0, 255) # красный цвет

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2) # отрисовка прямоугольника
        
        cv2.imshow('video', frame)
    
    # ESCAPE для выхода
    if cv2.waitKey(1) == 27:
        break

cap.release()