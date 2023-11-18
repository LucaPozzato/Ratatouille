from openai import OpenAI
import os

def audio_product():
    os.system("base64 -D -i audio.txt -o audio.mp3")
    return 0

def get_text(file):
    client = OpenAI(
        api_key='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'
    )

    audio_file = open("audio.mp3", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )

    print(transcript)
    return transcript