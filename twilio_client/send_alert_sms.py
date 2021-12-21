import os
import logging
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


class SendSmsAlert:
	#Class that sends an SMS alert if an unknow person was detected
	def __init__(self):
		self.account_sid = "YOUR TWILIO ACCOUNT"
		self.auth_token = "YOUR TWILIO AUTH TOKEN"
		self.log_file = os.path.join(os.getcwd() + "\\twilio_client\\sms_logs\\twilio_logs.txt")

	def SendSMS(self):
		#print(self.log_file)
		try:
			client = Client(self.account_sid,self.auth_token)
			logging.basicConfig(filename=self.log_file)			
			client.http_client.logger.setLevel(logging.INFO)
			message = client.messages.create(
								from_="+12344075238",
								body="Unknown person was detected",
								to="+14083899258"
								)
			m_id = message.error_code
			if m_id == None:
				print("Message was sent successfully alerting home owner")
			print("Wrote twilio logs to \n{}".format(self.log_file))
		except TwilioRestException as e:
			print(e)