from openai import OpenAI


def article_formatting(filetxt):
    API_KEY = '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'
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
                    "content": "Properly structurize the following text, with headlines and paragraphs, as a HTML file, omitting the <html> and <head> tags: " + article
                               + "\nThen insert images in-between paragraphs with <img src =\"image_placeholder.jpg\"> and place a short description in Polish, fitting to the paragraph above, under each image using the alt atribute and <figcaption> tag. Then remove \"<body>\" in the beginning and \"</body>\" in the end. Reply only with HTML code and nothing else. \n",
                }
            ],
            model="gpt-3.5-turbo",
        )

        return response.choices[0].message.content
    except Exception as e:
        return str(e)