from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
from .utils import call_chat_gpt, generate_speech

app = Flask(__name__)

@app.route('/twiml', methods=['GET'])
def serve_twiml():
    contact_name = request.args.get('contact_name', 'there')

    message = call_chat_gpt(f"Create a persuasive message for {contact_name} to sell their property.")
    
    voice_id = "<voice_id>"
    stability = 0.5
    similarity_boost = 0.5
    audio_data = generate_speech(message, voice_id, stability, similarity_boost)

    response = VoiceResponse()
    response.play('', {'content-type': 'audio/mpeg'})
    response.append(audio_data)

    return Response(str(response), content_type='text/xml')

if __name__ == '__main__':
    app.run(debug=True)
