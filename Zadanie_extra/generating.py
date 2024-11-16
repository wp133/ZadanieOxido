from openai import OpenAI


def article_generating():
    API_KEY = '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'
    try:
        client = OpenAI(api_key=API_KEY)

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Wygeneruj szablon HTML z pustą sekcją <body> do której można wkleić dowolny tekst. Użyj elementów CSS żeby poprawnie ustrukturyzować kod.",
                }
            ],
            model="gpt-3.5-turbo",
        )

        return response.choices[0].message.content
    except Exception as e:
        return str(e)