from openai import OpenAI
import os
import base64

def get_audio(format):
    # format = "m4a"
    # os.system("base64 -D -i audio.txt -o audio."+format)
    client = OpenAI(
        api_key='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'
    )

    input_file = open("audio.txt", "r")
    audio_file_encoded = input_file.read()
    audio_file_decoded = base64.b64decode(audio_file_encoded)
    input_file.close()

    # print(audio_file_decoded)

    output_file = open("audio."+format, "wb")
    output_file.write(audio_file_decoded)
    output_file.close()

    audio_file = open("audio."+format, "rb")

    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        response_format="text",
        # language="it"
    )

    audio_file.close()

    return transcript

# get_audio()
