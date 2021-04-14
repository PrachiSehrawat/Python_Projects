from tkinter import *
import webbrowser as w

window = Tk()
window.title('Web Browser')
window.geometry('700x400')
window.configure(bg="black")
window.resizable(0,0)

Label(window,text='Where You Wanna Go ?',font=('georgia',30),bg='white',fg='purple').place(x=130,y=20)

def fac():
    w.open('facebook.com')

def insta():
    w.open('instagram.com')

def gmail():
    w.open('gmail.com')

def ggl():
    w.open('google.com')

def yt():
    w.open("youtube.com")

Button(window,text='Facebook',width=20,font="Large_font",bg='blue',fg='white',command=fac).place(relx=1,x=-650,y=110)
Button(window,text='Instagram',width=20,font="Large_font",bg='pink',fg='black',command=insta).place(relx=1,x=-280,y=110)
Button(window,text='Gmail',width=20,font="Large_font",bg='brown',fg='white',command=gmail).place(relx=1,x=-650,y=200)
Button(window,text='Google Search',font="Large_font",width=20,bg='green',fg='black',command=ggl).place(relx=1,x=-280,y=200)
Button(window,text='Youtube',font="Large_font",width=20,bg='red',fg='white',command=yt).place(relx=1,x=-460,y=285)


window.mainloop()


