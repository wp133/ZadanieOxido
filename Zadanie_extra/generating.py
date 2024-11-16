from openai import OpenAI


def article_generating():
    API_KEY = 'tu umiesc klucz'
    try:
        client = OpenAI(api_key=API_KEY)

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Wygeneruj szablon HTML z pustą sekcją <body> do której można wkleić dowolny tekst. Użyj elementów CSS żeby poprawić czytelność strony po umieszczeniu w niej tekstu.",
                }
            ],
            model="gpt-3.5-turbo",
        )

        return response.choices[0].message.content
    except Exception as e:
        return str(e)
