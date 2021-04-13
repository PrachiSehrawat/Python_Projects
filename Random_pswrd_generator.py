from tkinter import *
import pyperclip
import random
import string

window = Tk()
window.title("Password Generator")
window.geometry("700x400")
window.resizable(0,0)

pswrdstr = StringVar()
pswrdlen = IntVar()
pswrdlen.set(0)

def generate():

    pass1 = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ""

    for x in range(pswrdlen.get()):
        password = password + random.choice(pass1)

    pswrdstr.set(password)

def copytoclipboard():
    random_password = pswrdstr.get()
    pyperclip.copy(random_password)

Label(window, text="Random Password Generator",bg="black",fg = "white", font="georgia 30 bold").pack()
Label(window, text="Enter Password Length :",fg="red", font="georgia 20 italic").pack(pady=20)
Entry(window, text=pswrdlen, width = 30,font="Large_font").pack(pady=10)
Button(window, text="Generate Password",bg="green",fg = "white",font="georgia 15 bold", command=generate).pack(pady=10)
Entry(window, text=pswrdstr,width = 30,font="Large_font").pack(pady=10)
Button(window, text="Copy to Clipboard",bg="blue",fg = "white",font="georgia 15 bold", command=copytoclipboard).pack(pady=10)

window.mainloop()


