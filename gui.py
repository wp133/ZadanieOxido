import tkinter as tk
from tkinter import filedialog
from formatting import article_formatting
from tkhtmlview import HTMLLabel

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("text files", "Zadanie dla JJunior AI Developera - tresc artykulu.txt")])
    if file_path:
        print(file_path)
        desc = article_formatting(file_path)
        file1 = open("artykul.html", "w")
        file1.write(desc)
        #file1.close()

        file2 = open("showcase.html", "a")
        file2.write(("<body>\n"))
        file2.write(desc)
        file2.write(("\n</body>"))
        #file2.close()

def load_html_file(showfile_path):
    with open(showfile_path, 'r') as file:
        return file.read()

def reset():
    file1 = open("showcase.html", "w")
    file1.write("")

root = tk.Tk()
root.title("Article Generator")
root.geometry("800x600")


open_button = tk.Button(root, text="Open Text File", command=open_file)
open_button.pack(pady=20)

open_button = tk.Button(root, text="Reset", command=reset)
open_button.pack(pady=20)

html_content = load_html_file("showcase.html")
html_label = HTMLLabel(root, html=html_content)
html_label.pack(fill="both", expand=True)

root.mainloop()
