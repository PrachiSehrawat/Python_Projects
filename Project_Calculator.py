import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("My Calculator")
window.geometry("350x400")
window.resizable(0,0)

val = ""
A = 0
operator = ""

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_plus_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_sub_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mul_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def C_clicked():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        data.set(C)
        val = str(C)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        data.set(C)
        val = str(C)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        data.set(C)
        val = str(C)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showinfo("Error","Division By 0 Not supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A/x)
            data.set(C)
            cal = str(C)

data = StringVar()
lbl = Label(text = "Label",anchor = SE, font = ("verdana", 20), textvariable = data, bg = "#ffffff", fg = "#000000")
lbl.pack(expand = True, fill = "both")


btnrow1 = Frame(window, bg = "#000000")
btnrow1.pack(expand = True, fill = "both",)

btnrow2 = Frame(window)
btnrow2.pack(expand = True, fill = "both",)

btnrow3 = Frame(window)
btnrow3.pack(expand = True, fill = "both",)

btnrow4 = Frame(window)
btnrow4.pack(expand = True, fill = "both",)

btn1= Button(btnrow1,text = "1",font = ("verdana", 22),relief = GROOVE, border=0,command = btn_1_isclicked)
btn1.pack(side= LEFT, expand = True, fill = "both")

btn2= Button(btnrow1,text = "2",font = ("verdana", 22),relief = GROOVE, border=0,command = btn_2_isclicked)
btn2.pack(side= LEFT, expand = True, fill = "both")

btn3= Button(btnrow1,text = "3",font = ("verdana", 22),relief = GROOVE, border=0, command = btn_3_isclicked)
btn3.pack(side= LEFT, expand = True, fill = "both")

btn4= Button(btnrow1,text = "+",font = ("verdana", 22),fg = "green", relief = GROOVE, border=0,command = btn_plus_isclicked)
btn4.pack(side= LEFT, expand = True, fill = "both")



btn1= Button(btnrow2,text = "4",font = ("verdana", 22),relief = GROOVE, border=0,command = btn_4_isclicked)
btn1.pack(side= LEFT, expand = True, fill = "both")

btn2= Button(btnrow2,text = "5",font = ("verdana", 22),relief = GROOVE, border=0,command = btn_5_isclicked)
btn2.pack(side= LEFT, expand = True, fill = "both")

btn3= Button(btnrow2,text = "6",font = ("verdana", 22),relief = GROOVE, border=0,command = btn_6_isclicked)
btn3.pack(side= LEFT, expand = True, fill = "both")

btn4= Button(btnrow2,text = "-",font = ("verdana", 22),fg = "green",relief = GROOVE, border=0,command = btn_sub_isclicked)
btn4.pack(side= LEFT, expand = True, fill = "both")



btn1= Button(btnrow3,text = "7",font = ("verdana", 22),relief = GROOVE, border=0,command = btn_7_isclicked)
btn1.pack(side= LEFT, expand = True, fill = "both")

btn2= Button(btnrow3,text = "8",font = ("verdana", 22),relief = GROOVE, border=0,command = btn_8_isclicked)
btn2.pack(side= LEFT, expand = True, fill = "both")

btn3= Button(btnrow3,text = "9",font = ("verdana", 22),relief = GROOVE, border=0,command = btn_9_isclicked)
btn3.pack(side= LEFT, expand = True, fill = "both")

btn4= Button(btnrow3,text = "*",font = ("verdana", 22),fg = "green",relief = GROOVE, border=0,command = btn_mul_isclicked)
btn4.pack(side= LEFT, expand = True, fill = "both")



btn1= Button(btnrow4,text = "C",font = ("verdana", 22),fg = "red",relief = GROOVE, border=0,command = C_clicked)
btn1.pack(side= LEFT, expand = True, fill = "both")

btn2= Button(btnrow4,text = "0",font = ("verdana", 22),relief = GROOVE, border=0,command = btn_0_isclicked)
btn2.pack(side= LEFT, expand = True, fill = "both")

btn3= Button(btnrow4,text = "=",font = ("verdana", 22),fg = "red",relief = GROOVE, border=0,command = result)
btn3.pack(side= LEFT, expand = True, fill = "both")

btn4= Button(btnrow4,text = "/",font = ("verdana", 22),fg = "green",relief = GROOVE, border=0,command = btn_div_isclicked)
btn4.pack(side= LEFT, expand = True, fill = "both")

window.mainloop()






