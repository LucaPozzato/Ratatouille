import openai
import os

OPENAI_KEY = os.environ['OPENAI_KEY']

def recipe_gen(list):
    client = openai.OpenAI(
        api_key=OPENAI_KEY,
        # organization='org-oXnNlV1Z1fhmOWvYF8N6mjj2'
    )

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "I need a recipe given the ingredients"},
            {"role": "user", "content": "these are the ingredients" + str(list)}
        ],
        max_tokens=500
    )
    return completion.choices[0].message.content