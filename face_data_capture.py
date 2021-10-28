import os
import cv2
import numpy as np

#Replace the path to YOUR haarcascade xml!!
cascPath = "C:\\Users\\avale\\Desktop\\PYTHON_SCRIPTS\\OPENCV\\assets\\haarcascade_frontalface_default.xml"
data_path_folder = "C:\\Users\\avale\\Desktop\\PYTHON_SCRIPTS\\OPENCV\\dataset\\"
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
		except OSError as e:
			print(e)
		self.new_folder_path = str(self.new_folder_path + "{}".format("\\"))
	def capture_facial_samples(self):
		#method used for capturing the data
		print("Initiating the camera, may take up to 45 seconds")
		cam = cv2.VideoCapture(0)
		while (self.sampleNum<40):
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
			if(self.sampleNum>40):
				break
		cam.release()
		cv2.destroyAllWindows()
		print("Finished capture dataset was stored under \n{}".format(self.new_folder_path))
def main():
	initiate = InitiateDataCapture(user_name, user_id, new_folder_path)
	initiate.create_data_folder()
	initiate.capture_facial_samples()
	# cam.release()
	# cv2.destroyAllWindows()
	# print("Finished dataset was stored under \n{}".format(new_path))


if __name__ == '__main__':
	main()