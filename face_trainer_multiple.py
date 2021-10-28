import os
import cv2
import numpy as np
from PIL import Image
from datetime import datetime

#A simple python script which creates the training model using CV2. This script accepts up to 3
#datasets. Once the program is finished it creates a YML file containg the trained data

recognizer = cv2.face.LBPHFaceRecognizer_create()

data_path_andres = "C:\\Users\\avale\\Desktop\\PYTHON_SCRIPTS\\OPENCV\\dataset\\Andres"
data_path_lola = "C:\\Users\\avale\\Desktop\\PYTHON_SCRIPTS\\OPENCV\\dataset\\lola"
data_path_keira = "C:\\Users\\avale\\Desktop\\PYTHON_SCRIPTS\\OPENCV\\dataset\\KeiraBak"
andres_image_path = list()
lola_image_path = list()
keira_image_path = list()
YML_EXT = (".yml")
PATH_TO_YML_FILE = ("C:\\Users\\avale\\Desktop\\PYTHON_SCRIPTS\\OPENCV\\YML\\")
FILE_NAME = ("training_data_multiple_complete.yml")

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
	now = datetime.today().strftime("%Y-%m-%d")
	return str(now).replace(" ","")

def check_if_yml_exists(path,filename):
	#Checking if existing YML file is found,if file is found will
	#add datetime to end of file
	yml_file = os.path.join(path,filename)
	print(yml_file)
	try:
		if os.path.isfile(yml_file):
			print("\nFound existing yml. Creating a new one!")
			filename = filename[:-4] + "_" + returnTimeStamp() + YML_EXT
			filename = os.path.join(path,filename)
			print("Created new file, {}".format(filename))
			return filename
		else:
			print("Did not find an existing YML file. Creating a new one")
			filename = os.path.join(path,filename)
			print("Created new file " ,filename)
			return filename
	except OSError as e:
		print(e)


#getImageID(data_path_andres,data_path_lola)
def main():
	#check_if_yml_exists(PATH_TO_YML_FILE,FILE_NAME)
	Ids,faces = getImageID(data_path_andres,data_path_lola,data_path_keira)
	print("Training the model")
	recognizer.train(faces,np.array(Ids))
	check_if_yml_exists(PATH_TO_YML_FILE,FILE_NAME)
	recognizer.save(FILE_NAME)
	print("Success! .YML was saved under YML folder")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()