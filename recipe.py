import openai

def recipe_gen(list):
    client = openai.OpenAI(
        api_key='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'
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