
from googletrans import Translator

from tkinter import *
window=Tk()

txtfld = Entry(window, width = 50, text = "Enter text here...")
txtfld.place(x=90,y=150)

def Translate(x):
    translator = Translator()
    y = translator.translate(x)
    return y.text

def myClick():
    newLabel = Label(window,text = "Translated into English: ", fg = 'white',bg = 'black')
    newLabel.place(x=160,y=240)
    myLabel = Label(window, text = Translate(txtfld.get()))
    myLabel.place(x=140,y=260)
    # myLabel.pack()



btn = Button(window, text = "Translate", fg = 'blue', command = myClick)
btn.place(x=200, y=200)
lbl = Label(window, text = "Please Enter The Text To Be Translated",fg='red', font=("Cambria", 16))
lbl.place(x=80,y=80)


window.title('Translator App')
window.geometry("500x320+10+20")
window.mainloop()