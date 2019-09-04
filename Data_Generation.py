# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:24:50 2019

@author: GS-1854
"""
import cv2, os 

def face_database(directory, user_name):
    cascPath = 'haarcascade_frontalface_default.xml'  
    path = os.path.join(directory, user_name)
    faceCascade = cv2.CascadeClassifier(cascPath)
    mycamera = cv2.VideoCapture(0)
     
    count = 1
    while count < 50:  
        (_, image) = mycamera.read() 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        capture_faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE) 
        for (x, y, w, h) in capture_faces: 
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) 
            face = gray[y:y + h, x:x + w] 
            face_restructure = cv2.resize(face, (150, 120)) 
            cv2.imwrite('% s/% s.png' % (path, count), face_restructure) 
        count += 1
      
        cv2.imshow('Faces available', image) 
        input_key = cv2.waitKey(5) 
        if input_key == 25: 
            break
        return "Success"