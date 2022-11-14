import face_recognition
import pickle

try:
    with open('data.pickle', 'rb') as f:
        data = pickle.read(f)
except EOFError:
    data = []

    with open('data.pickle', 'wb') as f:
        data = pickle.dump(data, f)
finally:
    with open('data.pickle', 'rb') as f:
        data = pickle.read(f)

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