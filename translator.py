from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry("1080x400")
root.resizable(0,0)
root.title("language translator")
root.config(bg="ghost white")
Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg="white smoke").pack()
Label(root, text="Created By BIT", font="arial 20 bold", bg="red", width="20").pack(side="bottom")

Label(root, text="Enter Text", font="arial 13 bold", bg="white smoke").place(x = 200, y = 60)
input_text = Text(root, font="arial 10", height=11, wrap=WORD, padx=5, pady=5, width=60)
input_text.place(x = 50, y = 100)

Label(root, text="Translation", font="arial 13 bold", bg="white smoke").place(x = 750, y = 60)
output_text = Text(root, font="arial 10", height=11, wrap=WORD, padx=5, width=60)
output_text.place(x = 600, y = 100)

Languages = list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values=Languages, width=22)
dest_lang.place(x = 890, y = 60)
dest_lang.set("choose Output Language")

def Translate():
    translator = Translator()
    translated = translator.translate(text=input_text.get(1.0, END), dest= dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)

trans_btn = Button(root, text="Translate", font="arial 12 bold", pady=5, command=Translate, bg="royal blue1", activebackground="sky blue", activeforeground="red")
trans_btn.place(x = 500, y = 180)

root.mainloop()