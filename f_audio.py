from openai import OpenAI
import os
import base64
from datetime import date

def get_audio(format):
    # format = "m4a"
    # os.system("base64 -D -i audio.txt -o audio."+format)

    today = date.today()

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

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            # {"role": "system", "content": "I need an array of dict for each product, its product catgeory and the shelf_life which is an estimate of the expiration date given that I purchased the product today. The dictionary should only have as keys: product, category in english, shelf_life is the string formatted like DD-MM-YYYY"},
            {"role": "user", "content": "I need an array of dict for each product, its product catgeory and the shelf_life the day:" + str(today) + ". The dictionary should only have as keys: product, category in english, shelf_life is in days. I need to generate the array of dict for:"+transcript+". I only need the array, please don't generate other text. Don't say anything else."}
        ]
    )
    return completion.choices[0].message.content

# get_audio()
