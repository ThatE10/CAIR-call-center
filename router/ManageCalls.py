from flask import Flask, app
from twilio.twiml.voice_response import VoiceResponse

#
app = Flask(__name__)
LongWaitTimes = False

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    #Todo Create Audio Stream, call AudioProcessing.getAudioWebhook()

    """
    
    response = VoiceResponse()
    start = Start()
    start.stream(
        name='Example Audio Stream', url='wss://mystream.ngrok.io/audiostream'
    )
    response.append(start)

    """
    return str(resp)



app.run(debug=True)
