from IPython.display import Image, display
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from nltk.corpus import wordnet
from googletrans import Translator

root = tk.Tk()
root.title('Dictionary')
root.geometry('600x300')
root['bg'] = 'white'
frame = Frame(root,width=200,height=300,borderwidth=1,relief=RIDGE) 
frame.grid(sticky="W") 

def get_meaning():
    get_word = entry.get()
    language = language_combo.get()

    if get_word == "":
        messagebox.showerror('Dictionary','Please write the word')
        return

    if language == 'English-to-English':
        meanings = wordnet.synsets(get_word)
        if meanings:
            meaning_text = ', '.join([meaning.definition() for meaning in meanings])
            output.insert('end', meaning_text)
        else:
            messagebox.showinfo('Dictionary', 'No meaning found for the word.')
    elif language == 'English-to-Hindi':
        translator = Translator()
        translation = translator.translate(get_word, dest='hi')
        output.insert('end', translation.text)

def quit_app():
    root.destroy()

image_path = 'image.png'
image = PILImage.open(image_path)
image.thumbnail((100, 100))  # Adjust size if needed
tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=tk_image)
image_label.place(x=40, y=70)

word_label = Label(root, text="Enter Word", bg="white", font=('verdana', 10, 'bold'))
word_label.place(x=250, y=23)

language_var = tk.StringVar() 
language_combo = ttk.Combobox(root, width=20, textvariable=language_var, state='readonly', font=('verdana', 10, 'bold'))
language_combo['values'] = ('English-to-English', 'English-to-Hindi')
language_combo.place(x=380, y=10)
language_combo.current(0)

entry = Entry(root, width=50, borderwidth=2, relief=RIDGE)
entry.place(x=250, y=50)

search_button = Button(root, text="Search", font=('verdana', 10, 'bold'), cursor="hand2", relief=RIDGE, command=get_meaning)
search_button.place(x=430, y=80)

quit_button = Button(root, text="Quit", font=('verdana', 10, 'bold'), cursor="hand2", relief=RIDGE, command=quit_app)
quit_button.place(x=510, y=80)

meaning_label = Label(root, text="Meaning", bg="white", font=('verdana', 15, 'bold'))
meaning_label.place(x=230, y=120)

output = Text(root, height=8, width=40, borderwidth=2, relief=RIDGE)
output.place(x=230, y=160)

root.mainloop()
