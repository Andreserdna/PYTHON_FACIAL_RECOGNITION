import os
import cv2
import numpy as np
from PIL import Image
from datetime import datetime
import time as time_

#A simple python script which creates the training model using CV2. This script accepts up to 3
#datasets. Once the program is finished it creates a YML file containg the trained data

#TODO cleanup this script
#TODO assure user only has 1 YML file in directory

recognizer = cv2.face.LBPHFaceRecognizer_create()

data_path_andres = "C:\\Users\\avale\\Desktop\\PYTHON_SCRIPTS\\OPENCV\\dataset\\Andres"
data_path_lola = "C:\\Users\\avale\\Desktop\\PYTHON_SCRIPTS\\OPENCV\\dataset\\lola"
data_path_keira = "C:\\Users\\avale\\Desktop\\PYTHON_SCRIPTS\\OPENCV\\dataset\\KeiraBak"
YML_EXT = (".yml")
PATH_TO_YML_FILE = ("C:\\Users\\avale\\Desktop\\PYTHON_SCRIPTS\\OPENCV_2\\PYTHON_FACIAL_RECOGNITION\\YML\\")
FILE_NAME = ("training_data.yml")

def getImageID(data_path_andres,data_path_lola,data_path_keira):
	#TODO add error handling for user provided paths
	print("Retreiving faces from user provided datasets")
	try:
		imagePathAndres = [os.path.join(data_path_andres,f) for f in os.listdir(data_path_andres)]
		imagePathLola = [os.path.join(data_path_lola,f) for f in os.listdir(data_path_lola)]
		imagePathKeira = [os.path.join(data_path_keira,f) for f in os.listdir(data_path_keira)]
		faces = list()
		IDs = list()
		complete_list = imagePathAndres + imagePathLola + imagePathKeira
		for image in complete_list:
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

def returnTimeStamp():
	#Quick function to return time, user to add to end of new yml file
	now = datetime.today().strftime("%Y-%m-%d%H%M%S")
	return str(now).replace(" ","")

def returnLogTime():
	return int(round(time_.time() * 1000))

def check_if_yml_exists_and_create(path,filename):
	#Checking if existing YML file is found,if file is found will
	#add datetime to end of file
	yml_file = os.path.join(path,filename)
	try:
		if os.path.isfile(yml_file):
			print("\nFound existing yml. Creating a new one!")
			filename = filename[:-4] + "_" + returnTimeStamp() + YML_EXT
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


#getImageID(data_path_andres,data_path_lola)
def main():
	Ids,faces = getImageID(data_path_andres,data_path_lola,data_path_keira)
	print("Training the model")
	recognizer.train(faces,np.array(Ids))
	check_if_yml_exists_and_create(PATH_TO_YML_FILE,FILE_NAME)
	print("Success! .YML was saved under YML folder")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()