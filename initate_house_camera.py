import cv2
import numpy as np
import os
from write_video_logs import *


#TODO add descriptions for your functions 
#TODO Create an infinite loop to grab all the logs
#TODO create another script that checks the size of the log file
#TODO Create a script that sends an SMS if a stranger is detected
#TODO Create a function to classify different memebers of your hoome. Write the detections to log file
class InitiateHouseCamera:
	def __init__(self):
		self.user_id = 0
		self.yml_path = os.path.join(os.getcwd() + "\\YML\\training_data_multiple_complete.yml")
		self.font = (cv2.FONT_HERSHEY_SIMPLEX)
		self.fontColor = (255,255,255)
		self.fontScale = 1
		self.lineType = 2
		self.bottomLeftCornerText = (10,255)
		self.user_id = 0
		self.our_home_data = {1:{"name":"Andres"},
	 	  		  			  2:{"name":"Lola"},
	 	  		  			  3:{"name":"Keira"}}

	def InitateCameraAndIdentify(self):
		write_log_file = WriteLogsToText()
		cascade_path = os.path.join(os.getcwd() + "\\assets\\haarcascade_frontalface_default.xml")
		faceDetect = cv2.cv2.CascadeClassifier(cascade_path)
		print("Initating Camera, may take up to 30 seconds")
		camera =  cv2.VideoCapture(0)
		recognizer = cv2.face.LBPHFaceRecognizer_create()
		recognizer.read(self.yml_path)
		while True:
			ret,img = camera.read()
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			faces = faceDetect.detectMultiScale(gray,1.3,5)
			for(x,y,w,h) in faces:
				cv2.rectangle(img,(x,y), (x+w, y+h),(0,0,255),2)
				self.user_id,conf = recognizer.predict(gray[y:y+h,x:x+w])
				conf = 100 - float(conf)
				formated_confidence = "{:.2f}".format(conf)
				conf = "Confidence "+ str(formated_confidence) + "%"
				for house_id,house_names in self.our_home_data.items():
					self.user_id =(house_names['name'])
					break
				for house_id,house_names in self.our_home_data.items():
					if house_id == 1:
						if write_log_file.captureLogs(self.user_id,str(formated_confidence)) == True:
							camera.release()
							cv2.destroyAllWindows()
							return
					cv2.putText(img,str(self.user_id + conf),self.bottomLeftCornerText,self.font,self.fontScale,self.fontColor,self.lineType)
			cv2.imshow("FACE", img)
			if(cv2.waitKey(1) == ord('q')):
				break
x = InitiateHouseCamera()
x.InitateCameraAndIdentify()