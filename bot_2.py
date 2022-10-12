from flask import Flask, request 
from twilio.twiml.messaging_response import MessagingResponse 

app=Flask(__name__)

@app.route("/")
def hello():
	return "hello , Balufu!"

	@app.route("/sms", methods=['POST'])
	def sms_reply():
		"""Respond to incoming calls with a simple text message"""
		#Fetch the message 
		msg = request.form.get('Body')

		#create rply 
		resp = MessagingResponse()
		resp.message("You said: {}" . format(mesg))

		return str(resp)

if __name__ == "__main__":
  app.run()
