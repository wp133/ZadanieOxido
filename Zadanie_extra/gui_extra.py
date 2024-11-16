import tkinter as tk
from tkinter import filedialog
from formatting_extra import article_formatting
from generating import article_generating
from tkhtmlview import HTMLLabel

def generate():
    rez = article_generating()
    file3 = open("szablon.html", "w")
    file3.write(rez)

def load_html_file(showfile_path):
    with open(showfile_path, 'r') as file:
        return file.read()

def reset():
    file1 = open("showcase.html", "w")
    file1.write("")

def insert_text_into_html():

    text_file_path = filedialog.askopenfilename(filetypes=[("text files", "*.txt")])
    with open(text_file_path, 'r') as text_file:
        text_content = text_file.read()

    html_template_path = filedialog.askopenfilename(filetypes=[("html files", "*.html")])
    with open(html_template_path, 'r') as html_file:
        html_content = html_file.read()

    html_with_text = html_content.replace('<body>', f'<body>\n{text_content}\n', 1)

    with open("showcase.html", 'w') as output_file:
        output_file.write(html_with_text)
    article_formatting("showcase.html")

    html_content = load_html_file("showcase.html")
    html_label = HTMLLabel(root, html=html_content)
    html_label.pack(fill="both", expand=True)


root = tk.Tk()
root.title("Article Generator")
root.geometry("800x600")


open_button = tk.Button(root, text="Wygeneruj szablon", command=generate)
open_button.pack(pady=20)

open_button = tk.Button(root, text="Umieść tekst w szablonie", command=insert_text_into_html)
open_button.pack(pady=20)

open_button = tk.Button(root, text="Reset", command=reset)
open_button.pack(pady=20)


root.mainloop()


