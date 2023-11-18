import openai

def recipe_gen(list):
    client = openai.OpenAI(
        api_key='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',
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