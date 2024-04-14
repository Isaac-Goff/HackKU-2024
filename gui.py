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
    window.geometry('%dx%d+%d+%d' % (s_width / 5, s_height / 3, 1530, 150))
    # window.resizable(False, False)

    frame = Frame(window)
    frame.pack()

    var = StringVar()
    choice = IntVar()
    var.set("This is an application to test the trust of articles")
    response = Label(window, textvariable=var, borderwidth=4, relief="groove", wraplength=500, justify='center')
    response.pack(pady=40, padx=20)

    R1 = Radiobutton(window, text="Sentiment Analysis", variable=choice, value=1)
    R2 = Radiobutton(window, text="AI Sentiment", variable=choice, value=2)
    choice.set(1)
    R1.pack(anchor=W)
    R2.pack(anchor=W)

    check = Button(frame, text="Check Article", command=lambda: change_text(var))
    check.pack(pady=40)
    close = Button(frame, text="Close", command=window.destroy)
    close.pack(side=BOTTOM)

    window.protocol("WM_DELETE_WINDOW", 'disable_event')
    window.mainloop()


open_window()
