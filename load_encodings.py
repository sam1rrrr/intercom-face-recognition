import face_recognition
import cv2

import pickle
import os

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')


frames_count = 0 # кол-во кадров
while True:
    frames_count += 1
    ret = cap.grab()

    if frames_count % 10 == 0:
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
        
        cv2.imshow('video', frame)

    if cv2.waitKey(1) == 27:
        break



try:
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
except EOFError:
    data = []

    with open('data.pickle', 'wb') as f:
        data = pickle.dump(data, f)
finally:
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)

FACES_ADDED = 0


while True:
    number = input('Введите номер фотографии (чтобы закончить напишите -1) :')
    if number == '-1':
        break

    image = face_recognition.load_image_file(f'faces/{number}.jpg')
    try:
        encodings = face_recognition.face_encodings(image)[0]
    except IndexError:
        print(f'[!] Ошибка. Не удается распознать лицо на фотографии {number}.jpg')
        continue
    
    data.append(encodings)
    print('[+] Лицо успешно добавлено!')
    FACES_ADDED += 1

with open('data.pickle', 'wb') as f:
    data = pickle.dump(data, f)    

print(f'Добавлено {FACES_ADDED} лиц')