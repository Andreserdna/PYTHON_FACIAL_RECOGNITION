from datetime import datetime
import os
from face_trainer_multiple import returnTimeStamp, returnLogTime

#TODO add descriptions for your functions 
class WriteLogsToText:
#Script used to write logs for who is detected
	def __init__(self):
		self.video_log_dir = os.path.join(os.getcwd() + str("\\video_logs_text\\"))
		self.text_extension = ".txt"
		self.log_file = self.video_log_dir + str("capture_logs_") + returnTimeStamp() + self.text_extension
		self.log_data_list = list()

	def createLoggingTextFile(self):
		try:
			video_log_text_file = self.log_file
			open(video_log_text_file,"w").close
			
			if os.path.exists(video_log_text_file):
				open(video_log_text_file,"w").close
				return video_log_text_file
			else:
				print("Found old log file, deleting")
				open(video_log_text_file,"w").close
				return video_log_text_file
		except OSError as e:
			print(e)

	def writeToText(self, data, file_path):
		try:
			with open(file_path,"w") as text_file:
				for line in data:
					text_file.write(line + "\n")
				text_file.close()
				print("Wrote data to: \n{}".format(self.log_file))
		except IOError as e:
			print(e)

	def captureLogs(self,user_name,conf):
		self.createLoggingTextFile()
		try:
			detected_person_logs = ("{} was detected at {}-{} Confidence percenatage {}".format(user_name,returnTimeStamp(),returnLogTime(),conf))
			print(detected_person_logs)
			self.log_data_list.append(detected_person_logs)
			print()
			if len(self.log_data_list) > 100:
				print("Data has reached its limit, writing logs to text file")
				self.writeToText(self.log_data_list,self.log_file)
				return True
		except IOError as e:
			print(e)