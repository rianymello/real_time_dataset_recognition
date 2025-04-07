import cv2
import numpy as np
from PIL import Image
import os

path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        if not imagePath.lower().endswith('.jpg'):
            continue
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(imageNp)
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y+h, x:x+w])
            ids.append(id)
    return faceSamples, ids

print("\n [INFO] Treinando... Aguarde.")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

if not os.path.exists('trainer'):
    os.makedirs('trainer')
recognizer.write('trainer/trainer.yml')
print(f"\n [INFO] {len(np.unique(ids))} rosto(s) treinado(s).")
