import speech_recognition as sr

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import os

load_dotenv()


# Load API key from environment variable

client = ElevenLabs(api_key='sk_b756b91b40a211138e50c015a7de6c92e29ce0342361bdd9')

try:
    # Convert text to speech
    audio = client.text_to_speech.convert(
        text="The first move is what sets everything in motion.",
        voice_id="JBFqnCBsd6RMkjVDRZzb",  
        model_id="eleven_multilingual_v2", 
        output_format="mp3_44100_128",  
    )

    # Play the audio
    play(audio)

except Exception as e:
    print(f"An error occurred: {e}")
