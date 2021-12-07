from datetime import datetime
import os
from face_trainer_multiple import returnTimeStamp


class WriteLogsToText:
#Script used to write logs for who is detected
	def __init__(self):
		self.video_log_dir = os.path.join(os.getcwd() + str("\\video_logs_text\\"))
		self.text_extension = ".txt"
		self.log_file = self.video_log_dir + str("capture_logs_") + returnTimeStamp() + self.text_extension
		self.log_data_list = list()
		#self.detected_person_logs = detected_person_logs
		self.user_names =  {1:{"name":"Andres "},
	 	 				    2:{"name":"Lola "},
	 	  					3:{"name":"Keira "}}
		#self.log_list = log_list

	def createLoggingTextFile(self):
		try:
			video_log_text_file = self.log_file
			open(video_log_text_file,"w").close
			
			if os.path.exists(video_log_text_file):
				print("Did not find a log text file,creating new one")
				open(video_log_text_file,"w").close
				print("Created video log file!")
				return video_log_text_file
			else:
				print("Found old log file, deleting")
				open(video_log_text_file,"w").close
				return video_log_text_file
		except OSError as e:
			print(e)
	def writeToText(self, data, file_path):
		self.createLoggingTextFile()
		try:
			print("opening text file")
			with open(file_path,"w") as text_file:
				for line in data:
					text_file.write(line + "\n")
				text_file.close()
		except IOError as e:
			print(e)
	def captureLogs(self):
		try:
			current_samples = 0
			detected_person_logs = ("{} was detected at {}".format(self.user_names,returnTimeStamp()))
			print(detected_person_logs)
			self.log_data_list.append(detected_person_logs)
			print()
			if len(self.log_file) > 500:
				print("Data has reached its limit, writing logs to text file")
				self.writeToText(self.log_data_list,self.log_file)
				return True
		except IOError as e:
			print(e)




	def test(self):

		if os.path.isdir(self.video_log_dir):
			print("Path exists!!")
		print(self.log_file)

a = WriteLogsToText()
a.captureLogs()