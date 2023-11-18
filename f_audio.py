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

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "I need an array of dict for each product, its product catgeory and it's shelf life in days. The dictionary should only have as keys: product, category in english, shelf_life represents the number of days of the shelf life"},
            {"role": "user", "content": "I need to generate the array of dict for:"+transcript+"don't generate text, don't talk"}
        ]
    )
    return completion.choices[0].message.content

# get_audio()
