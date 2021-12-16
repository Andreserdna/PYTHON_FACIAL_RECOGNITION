from datetime import datetime
import os
from face_trainer_multiple import returnTimeStamp, returnLogTime
import time
#TODO create a function that creates a new file once current file has reached its limit

class WriteLogsToText:
#Script used to write logs for who is detected
	def __init__(self):
		self.video_log_dir = os.path.join(os.getcwd() + str("\\video_logs_text\\"))
		self.log_file = self.video_log_dir + str("capture_logs_") + returnTimeStamp() + ".txt"
		self.log_data_list = list()
		self.new_log_file = ''

	def createLoggingTextFile(self):
		#Created the logging text file user for capture logs
		#purposely supressed print statements until I figure out how to print onle 1
		try:
			open(self.log_file,"w").close
			return
		except OSError as e:
			print(e)

		if os.path.exists(self.log_file):
			#print("Found a file with the same name. Creating new one with timestamp ")
			self.new_log_file = self.video_log_dir + str("capture_logs_") + returnTimeStamp() + ".txt"
			open(self.new_log_file,"w").close
			#print("Created log file in {} ".format(self.new_log_file))
			return self.new_log_file, True
		else:
			print("Did not find a log file, creating new one")
			open(self.log_file,"w").close
			print("Created log file in {} ".format(self.log_file))


	def writeToText(self, data, file_path):
	#This function takes 2 arguments data and file_path
	#we retrieve the file path from the function createLoggingTextFile
	#We then pass the data captured from the captureLogs method
		try:
			with open(file_path,"a") as text_file:
				for line in data:
					text_file.write(line + "\n")
				#text_file.close()

		except IOError as e:
			print(e)
		

	def captureLogs(self,user_name,conf):
		#Takes 2 arguments user_name and conf the
		#I initialize createLogging in this method in order to create the new text file
		#user_name and conf are initialized in initlaize_house_camera.py. Captures detected person
		#and appends them to the list self.log_data_list once list hits the limit, logs are written to text file
		self.createLoggingTextFile()
		try:
			detected_person_logs = ("{} was detected at {}-{} Confidence percenatage {}".format(user_name,returnTimeStamp(),returnLogTime(),conf))
			print(detected_person_logs)
			self.log_data_list.append(detected_person_logs)
			print()
			if len(self.log_data_list) > 100:
				self.writeToText(self.log_data_list,self.log_file)
		except IOError as e:
			print(e)
	def checkLogFileSize(self):
		#Checking the size of the logfile, once the size limit is reached function exits and writes data
		MAX_SIZE = 60000 # equals to 60KB
		file_size = os.path.getsize(self.log_file)
		if file_size >= MAX_SIZE:
			print("File has reaCHED its size limit")
			print("Wrote data to: \n{}".format(self.log_file))
			return True
		else:
			print("Current file size is {}".format(file_size))

