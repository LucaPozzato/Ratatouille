from openai import OpenAI
import os

def get_audio(format):
    os.system("base64 -D -i audio.txt -o audio."+format)

    client = OpenAI(
        api_key='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'
    )

    audio_file = open("audio."+format, "rb")

    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        response_format="text",
        # language="it"
    )

    return transcript

# audio_product()
