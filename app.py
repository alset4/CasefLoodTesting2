from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
import os

# Initialize Flask app
app = Flask(__name__)

# Twilio voice response endpoint
@app.route("/voice", methods=["POST"])
def voice():
    # Create a TwiML response object
    response = VoiceResponse()
    # Respond with a greeting message
    response.say("Hello, thank you for calling Caseflood. I'm Luna, their AI assistant. How can I help?")
    return Response(str(response), mimetype="application/xml")

# Run the server
if __name__ == "__main__":
    app.run(port=5000)
