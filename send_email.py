import os
from email.message import EmailMessage
import ssl
import smtplib

class Email_Class:
	def __init__(self):
		self.send_mail()

	def send_mail(self):
		self.email_sender = "Type your E-Mail here..."
		self.email_password = "Type your Password here..."
		self.email_receiver = input("Enter Receiver Email : ")

		self.email_subject = input("\nEnter Subject for your Mail : ")
		self.email_body = input("Enter Body for your Mail : ")

		self.em = EmailMessage()

		self.em["From"] = self.email_sender
		self.em["To"] = self.email_receiver
		self.em["Subject"] = self.email_subject
		self.em.set_content(self.email_body)

		self.email_context = ssl.create_default_context()

		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = self.email_context) as smtp:
			smtp.login(self.email_sender, self.email_password)
			smtp.sendmail(self.email_sender, self.email_receiver, self.em.as_string())

			print(f"\nMail has been sent to *{self.email_receiver}*\nThank you...")


if __name__ == '__main__':
	obj = Email_Class()
