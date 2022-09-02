#import time --> strfrtime
#import tkinter --> Label, Tk
from time import strftime
from tkinter import Label, Tk

#window config
window = Tk()
window.title("Digital Clock")
window.geometry("300x300")
window.configure(bg="green")
window.resizable(False, False)

clock_label = Label(window, bg="green", fg="white", font = ("Times", 30, 'bold'), relief='flat')
clock_label.place(x = 20, y = 20)

def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

#run program loops

update_label()
window.mainloop()