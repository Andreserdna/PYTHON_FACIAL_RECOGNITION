import os
import cv2
import numpy as np
from PIL import Image
from datetime import datetime
import time as time_

#A simple python script which creates the training model using CV2. This script accepts up to 3
#datasets. Once the program is finished it creates a YML file containg the trained using image dataset provided


def retrieve_datasets_paths(dpath,image_list):
	#Retrieves all of the images from a directory
	for r,d,f in os.walk(dpath):
		if len(r) == 81:
			pass
		elif len(r)>81:
			print("Appended the following directory to  datasets \n {}".format(r))
			dataset_directories.append(r)
	for images in dataset_directories:
		image_path = [os.path.join(images,f) for f in os.listdir(images)]
		for items in image_path:
			image_list.append(items)

def getImageID(data_set):

	print("Retreiving faces from user provided datasets")
	try:
		faces = list()
		IDs = list()
		for image in data_set:
			faceImg = Image.open(image).convert("L")
			faceNP = np.array(faceImg,'uint8')
			ID = int(os.path.split(image)[-1].split('.')[1])
			faces.append(faceNP)
			IDs.append(ID)
			cv2.imshow("training",faceNP)
			cv2.waitKey(10)
		return IDs,faces
	except ValueError as e:
		print("Did you pass the correct path?", e)
def getImageIDAndLabels(data_set,detector):

	print("Retreiving faces from user provided datasets")
	try:
		FaceSamples = list()
		IDs = list()
		for image in data_set:
			faceImg = Image.open(image).convert("L")
			faceNP = np.array(faceImg,'uint8')
			ID = int(os.path.split(image)[-1].split('.')[1])
			faces = detector.detectMultiScale(faceNP)
			for (x,y,w,h) in faces:
				FaceSamples.append(faceNP[y:y+h,x:x+w])
				IDs.append(ID)
			cv2.imshow("training",faceNP)
			cv2.waitKey(10)
		return FaceSamples,IDs
	except ValueError as e:
		print("Did you pass the correct path?", e)

def returnTimeStamp():
	#Quick function to return time, user to add to end of new yml file
	now = datetime.today().strftime("%Y-%m-%d%H%M%S")
	return str(now).replace(" ","")

def returnLogTime():
	return int(round(time_.time() * 1000))

def check_if_yml_exists_and_create(path,filename):
	#Checking if existing YML file is found,if file is found will
	#delete old one and create new one
	yml_file = os.path.join(path,filename)
	try:
		if os.path.isfile(yml_file):
			print("\nFound existing yml. Deleting and creating a new one!")

			filename = os.path.join(path,filename)
			print("Starting recognizer")
			recognizer.save(filename)
			print("Created new file, {}".format(filename))
			return 
		else:
			print("Did not find an existing YML file. Creating a new one")
			filename = os.path.join(path,filename)
			print("Created new file " ,filename)
			recognizer.save(yml_file)
			return 
	except OSError as e:
		print(e)

def main():
	image_count = 0
	retrieve_datasets_paths(data_path,image_list)
	faces,Ids = getImageIDAndLabels(image_list,detector)
	print("Training the model")
	recognizer.train(faces,np.array(Ids))
	check_if_yml_exists_and_create(PATH_TO_YML_FILE,FILE_NAME)
	print("Success! .YML was created with {} images".format(len(image_list)))
	cv2.destroyAllWindows()

if __name__ == '__main__':
	#os.chdir("..")
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	haar_file = os.path.join(os.getcwd() + "\\assets\\haarcascade_frontalface_default.xml")
	detector = cv2.CascadeClassifier(haar_file)
	data_path = os.path.join(os.getcwd() + "\\dataset\\")
	dataset_directories = list()
	image_list = list()
	PATH_TO_YML_FILE = (os.path.join(os.getcwd() + "\\YML\\"))
	FILE_NAME = ("training_data.yml")
	main()