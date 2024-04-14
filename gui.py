import tkinter

import pyautogui as pg
from tkinter import *
import os


def change_text(text, data="There is no data to check at this time"):
    text.set(str(data))
def open_window():
    data = None
    window = Tk()
    window.attributes("-alpha", 0.4)
    window.title("Falsified")
    s_width = window.winfo_screenwidth()
    s_height = window.winfo_screenheight()
    window.geometry('%dx%d+%d+%d' % (s_width / 5, s_height / 6, 1520, 150))
    # window.resizable(False, False)s

    frame = Frame(window)
    frame.pack()

    var = StringVar()
    var.set("Hello World")
    response = Label(window, textvariable=var)
    check = Button(frame, text="Check Article", command=lambda : change_text(var))
    close = Button(frame, text="Close", command=window.destroy)

    response.pack()
    check.pack()
    close.pack()

    window.protocol("WM_DELETE_WINDOW", 'disable_event')
    window.mainloop()


open_window()
