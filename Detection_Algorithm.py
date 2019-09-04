# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:36:20 2019

@author: GS-1854
"""

# It helps in identifying the faces 
import cv2, sys, numpy, os 

def face_recognition(directory):
    cascPath = 'haarcascade_frontalface_default.xml'
    
    (images, lables, names, id) = ([], [], {}, 0) 
	for (subdirs, dirs, files) in os.walk(directory): 
		for subdir in dirs: 
			names[id] = subdir 
			cat_path = os.path.join(directory, subdir) 
			for filename in os.listdir(cat_path): 
				dir = cat_path + '/' + filename 
				lable = id
				images.append(cv2.imread(dir, 0)) 
				lables.append(int(lable)) 
			id += 1
	
	(images, lables) = [numpy.array(entity) for entity in [images, lables]] 
	
	
	model = cv2.face.LBPHFaceRecognizer_create() 
	model.train(images, lables) 
	
	
	face_cascade = cv2.CascadeClassifier(cascPath) 
	mycamera = cv2.VideoCapture(0) 
	
	while True:
		
		(_, image) = mycamera.read() 
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
		capture_faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=2, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
		
		for (x, y, w, h) in capture_faces:
			cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2) 
			face = gray[y:y + h, x:x + w] 
			face_resize = cv2.resize(face, (150, 120)) 
	
			face_prediction = model.predict(face_resize) 
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3) 
	
			if face_prediction[1]<500:
				cv2.putText(image, '% s - %.0f' % (names[face_prediction[0]], face_prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0)) 
			else:
				cv2.putText(image, 'unable to recognize', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
			
			cv2.imshow('Faces Found', image) 
		
		input_key = cv2.waitKey(5) 
		if input_key == 25: 
			break
	
	return "Success"