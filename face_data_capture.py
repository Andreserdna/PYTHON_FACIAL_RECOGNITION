import os
import shutil
import cv2
import numpy as np

#Replace the path to YOUR haarcascade xml!!
cascPath = os.path.join(os.getcwd() + "\\assets\\haarcascade_frontalface_default.xml")
data_path_folder = os.path.join(os.getcwd() + "\\dataset\\")
faceDetect = cv2.cv2.CascadeClassifier(cascPath)

print("Initiating facial capture")
user_name = input("Enter Name: ")
user_id = input('Enter user ID[0-9]: ')
new_folder_path = os.path.join(data_path_folder,str(user_name))

class InitiateDataCapture:
	def __init__(self,user_name,user_id,new_folder_path,sampleNum=0):
		self.user_name = user_name
		self.user_id = user_id
		self.new_folder_path = new_folder_path
		self.sampleNum = sampleNum

	def create_data_folder(self):
		#Creating a new data_folder
		try:
			if not os.path.exists(self.new_folder_path):
				print("Did not find a folder with that user name\nCreating new one")
				os.makedirs(self.new_folder_path)
			elif os.path.exists(self.new_folder_path):
				print("Found existing folder with same do you wish to delete?")
				answer = input ("y/N: ")
				if answer == "y":
					print("Deleting files")
					shutil.rmtree(self.new_folder_path)
					print("Done, creating new directory")
					os.makedirs(self.new_folder_path)
				if answer == 'N':
					print("adding new images to existing dataset")
					pass
		except OSError as e:
			print(e)

	def capture_facial_samples(self):
		#method used for capturing the data
		print("Initiating the camera, may take up to 45 seconds")
		cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
		while (self.sampleNum<500):
			ret,img = cam.read()
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			faces = faceDetect.detectMultiScale(gray,1.3,5)
			for(x,y,w,h) in faces:
				print("Captured {} images ".format(self.sampleNum))
				self.sampleNum = self.sampleNum+1
				cv2.imwrite(self.new_folder_path +"/"+self.user_name+"."+str(self.user_id)+"."+str(self.sampleNum)+".jpg",gray[y:y+h,x:x+w])
				cv2.rectangle(img,(x,y), (x+w, y+h),(0,0,255),2)
				cv2.waitKey(100)
			cv2.imshow("FACE", img)
			cv2.waitKey(1)
			if(self.sampleNum>500):
				break
		cam.release()
		cv2.destroyAllWindows()
		print("Finished capture dataset was stored under \n{}".format(self.new_folder_path))

def main():
	initiate = InitiateDataCapture(user_name, user_id, new_folder_path)
	initiate.create_data_folder()
	initiate.capture_facial_samples()

if __name__ == '__main__':
	main()