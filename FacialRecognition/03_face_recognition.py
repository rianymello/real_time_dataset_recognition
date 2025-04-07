import cv2
import numpy as np
import os
import json

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)

# Carrega os nomes do arquivo JSON
if os.path.exists('names.json'):
    with open('names.json', 'r') as f:
        names = json.load(f)
else:
    names = {}

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()
    if not ret:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5, minSize=(int(minW), int(minH)))

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        name = names.get(str(id), "Desconhecido")

        if confidence < 100:
            text = f"{name} ({round(100 - confidence)}%)"
        else:
            text = "Desconhecido"
        cv2.putText(img, text, (x+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:  # ESC
        break

print("\n [INFO] Encerrando.")
cam.release()
cv2.destroyAllWindows()
