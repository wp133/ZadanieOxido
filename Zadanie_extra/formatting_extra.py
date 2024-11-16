from openai import OpenAI


def article_formatting(filetxt):
    API_KEY = 'tu umiesc klucz'
    try:
        with open(filetxt, 'r') as file:
            lines = file.readlines()

        article = ''
        for line in lines[:-1]:
            if line.strip():
                article += line

        client = OpenAI(api_key=API_KEY)

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": article+ "\nGiven the following HTML file, make sure it is properly structured within its template. Do not alter any part of the HTML code but manipulate only the text which you find within the <body> section",
                }
            ],
            model="gpt-3.5-turbo",
        )

        return response.choices[0].message.content
    except Exception as e:
        return str(e)
