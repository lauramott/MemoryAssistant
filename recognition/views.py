from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2
import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('base dir ', BASE_DIR)


@csrf_exempt
def add(request):
    userId = request.POST['userId']
    name, num = os.path.basename(userId).split('.')
    id= int(num)
    print(id)
    data = {"success": False}
    detector = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml");
    cam = cv2.VideoCapture(0)
    sampleNum = 0
    while (True):
        factor = 0.75
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            sampleNum = sampleNum + 1
            print(sampleNum)
            cv2.imwrite("images/" +str(name) + "." + str(id) + "." + str(
                sampleNum) + ".png", cv2.resize(gray[y:y + h, x:x + w], (70, 70)))
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('frame', img)
        cv2.waitKey(100)
        if (sampleNum > 250):
            break
    cam.release()
    cv2.destroyAllWindows()
    return redirect('/contact')


#OPENCV
@csrf_exempt
def train(request):
    # initialize the data dictionary to be returned by the request
    data = {"success": False}

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # recognizer = cv2.face.EigenFaceRecognizer_create()
    # recognizer = cv2.face.FisherFaceRecognizer_create()
    path = 'images/'

    def getImagesWithID(path):
        folderPaths=[os.path.join(path,f) for f in os.listdir(path)]
        faces=[]
        IDs=[]
        name=[]
        print(folderPaths)
        for imagePath in folderPaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            name, ID, ID2, extention = os.path.basename(imagePath).split('.')
            faces.append(faceNp)
            print (ID)
            recognizer.setLabelInfo(int(ID), name)
            IDs.append(int(ID))
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)
        return IDs, faces

    Ids, faces = getImagesWithID(path)
    recognizer.train(faces, np.array(Ids))
    recognizer.write('C:/users/laura/desktop/src/trainer/trainer.yml')

    return redirect('/')


@csrf_exempt
def detect(request):
    data = {"success": False}

    recognizer = cv2.face.LBPHFaceRecognizer_create()  # LBPH Face Recognizer
    # recognizer = cv2.face.EigenFaceRecognizer_create()  # LBPH Face Recognizer
    # recognizer = cv2.face.FisherFaceRecognizer_create()  # LBPH Face Recognizer
    recognizer.read('C:/users/laura/desktop/src/trainer/trainer.yml')
    faceCascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX

    userId = 0
    count = 0
    while True:

        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE)
        for (x, y, w, h) in faces:
            print('predicting')
            getId, conf = recognizer.predict(cv2.resize(gray[y:y+h,x:x+w], (70,70)))
            cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)
            if conf < 100:
                userId = getId
                getName = recognizer.getLabelInfo(userId)
                print(conf, getName)
                cv2.putText(img, "Detected", (x, y + h), font, 2, (0, 255, 0), 2)
            else:
                cv2.putText(img, "Unknown", (x, y + h), font, 2, (0, 0, 255), 2)
                count+=1
                print(count)
                if(count==100):
                    cam.release()
                    cv2.destroyAllWindows()
                    return redirect('/')

        cv2.imshow("Face", img)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break
        elif userId != 0:
            cv2.waitKey(1000)
            cam.release()
            cv2.destroyAllWindows()
            return redirect('/contact/'+ str(getName)+'/detail/')

    cam.release()
    cv2.destroyAllWindows()
    return redirect('/')
