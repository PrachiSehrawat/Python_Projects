############## DICTIONARY ################

from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
window = Tk()
window.title("My Dictionary")
window.geometry("1000x500")

def dict():
    meaning.config(text=dictionary.meaning(word.get()))
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))


Label(window, text="Dictionary", font=("Georgia 40"), fg="white",bg="black").place(x=380,y=30)
Label(window, text="Type Any Word", font=("Georgia 20"), fg="white",bg="brown").place(x=150,y=150)
word = Entry(width = "50", font="Large_font")
word.place(x=400,y=150)
Label(window, text="Meaning: ", font=("Georgia 20"), fg="black",bg="red").place(x=150,y=200)
meaning = Label(window, text="", font=("Large_font"))
meaning.place(x=400,y=200)
Label(window, text="Synonym: ", font=("Georgia 20"), fg="black",bg="green").place(x=150,y=250)
synonym = Label(window, text="", font=("Large_font"))
synonym.place(x=400,y=250)
Label(window, text="Antonym: ", font=("Georgia 20"), fg="black",bg="cyan").place(x=150,y=300)
antonym = Label(window, text="", font=("Large_font"))
antonym.place(x=400,y=300)

Button(window, text="Find", font=("Georgia 20"), command=dict).place(x=450,y=350)

window.mainloop()

