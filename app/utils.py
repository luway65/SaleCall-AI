import openai
import requests

OPENAI_API_KEY = "<your_openai_api_key>"
openai.api_key = OPENAI_API_KEY
XI_API_KEY = "<xi-api-key>"

def call_chat_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

def generate_speech(text, voice_id, stability, similarity_boost):
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "xi-api-key": XI_API_KEY
    }

    data = {
        "text": text,
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity_boost
        }
    }

    response = requests.post(tts_url, json=data, headers=headers, stream=True)

    audio_data = b""
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            audio_data += chunk

    return audio_data
