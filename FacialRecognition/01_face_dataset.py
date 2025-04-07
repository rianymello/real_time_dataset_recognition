import cv2
import os
import json

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Solicita ID e Nome
face_id = input('\nDigite o ID do usuário: ')
face_name = input('Digite o NOME do usuário: ')

# Salva ID e Nome no arquivo JSON
names = {}
if os.path.exists('names.json') and os.path.getsize('names.json') > 0:
    try:
        with open('names.json', 'r') as f:
            names = json.load(f)
    except json.JSONDecodeError:
        print("[AVISO] O arquivo names.json está corrompido. Será recriado.")


names[face_id] = face_name

with open('names.json', 'w') as f:
    json.dump(names, f)

print("\n [INFO] Inicializando captura. Olhe para a câmera...")

count = 0
while True:
    ret, img = cam.read()
    if not ret:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1
        if not os.path.exists("dataset"):
            os.makedirs("dataset")
        cv2.imwrite(f"dataset/User.{face_id}.{count}.jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    
    k = cv2.waitKey(100) & 0xff
    if k == 27 or count >= 30:  # ESC ou 30 imagens
        break

print("\n [INFO] Imagens capturadas.")
cam.release()
cv2.destroyAllWindows()
