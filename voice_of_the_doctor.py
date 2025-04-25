# If you don’t use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

import os
import subprocess
import platform

from gtts import gTTS
from langchain.chat_models import init_chat_model


# Initialize Groq chat model
groq_chat_model = init_chat_model("playai-tts", model_provider="groq")

# Function: Text to Speech with gTTS (Google TTS)
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Function: Text to Speech with ElevenLabs
def text_to_speech_with_elevenlabs(input_text: str, output_filepath: str):
    audio = client.audio.speech.create(
        text=input_text,
        voice="Fritz-PlayAI",  # or any voice you prefer
        model="playai-tts"
       
    )
    save(audio, output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


