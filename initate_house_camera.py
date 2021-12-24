import cv2
import numpy as np
import os
from write_video_logs import *
from twilio_client.send_alert_sms import SendSmsAlert


#TODO add descriptions for your functions 
#TODO Create an infinite loop to grab all the logs
#TODO create another script that checks the size of the log file
#TODO Create a script that sends an SMS if a stranger is detected

class InitiateHouseCamera:
	def __init__(self):
		self.yml_path = os.path.join(os.getcwd() + "\\YML\\training_data.yml")
		self.unknown_person_images = os.path.join(os.getcwd() + "\\unknown_person_images\\")
		self.font = (cv2.FONT_HERSHEY_SIMPLEX)
		self.fontColor = (255,255,255)
		self.fontScale = 1
		self.lineType = 2
		self.bottomLeftCornerText = (10,255)


	def InitateCameraAndIdentify(self):
		user_id = 0
		unknow_person_count = 0
		name = ["None","Unknown","Lola","Keira"]
		write_log_file = WriteLogsToText()
		notify_owner = SendSmsAlert()
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
				user_id,conf = recognizer.predict(gray[y:y+h,x:x+w])
				#conf = 100 - float(conf)
				formated_confidence = "{:.2f}".format(conf)
				str_conf = "Confidence "+ str(formated_confidence) + "%"
				if conf<=100:
					user_id = name[user_id]
					conf = " {0}%".format(round(100 - conf))
					write_log_file.captureLogs(user_id, str_conf)
				elif conf > 100:
					user_id = "Unknown"
					write_log_file.captureLogs(user_id, str_conf)
					unknow_person_count = unknow_person_count + 1
					conf = " {0}%".format(round(100 - conf))
					print("Number of times Unknown person was detected {}".format(unknow_person_count))
					if unknow_person_count >=100:
						#notify_owner.SendSMS()
						print("Cpaturing Image of unknown person")
						cv2.imwrite(self.unknown_person_images + "Unknown_person_detected"+'.jpg',img)
						print("Stored unknown person image under {}".format(self.unknown_person_images))
						camera.release()
						cv2.destroyAllWindows()
						return

				#write_log_file.captureLogs(user_id, str_conf)
				if write_log_file.checkLogFileSize() == True:
					camera.release()
					cv2.destroyAllWindows()
					return
				cv2.putText(img,str(str(user_id) + str_conf),self.bottomLeftCornerText,self.font,self.fontScale,self.fontColor,self.lineType)
				cv2.imshow("FACE", img)
			if(cv2.waitKey(1) == ord('q')):
				break
x = InitiateHouseCamera()
x.InitateCameraAndIdentify()