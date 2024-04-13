import tkinter

import pyautogui as pg
from tkinter import *
import os



def open_window():
    window = Tk()
    window.attributes("-alpha", 0.4)
    window.title("Falsified")
    s_width = window.winfo_screenwidth()
    s_height = window.winfo_screenheight()
    window.geometry('%dx%d+%d+%d' % (s_width / 5, s_height / 6, 1520, 150))
    window.resizable(False, False)

    frame = Frame(window)
    frame.pack()

    check = Button(frame, text="Check Article")

    close = Button(frame, text="Close", command=window.destroy)
    close.pack(side=BOTTOM, padx=20, pady=30)
    check.pack(side=BOTTOM, padx=20, pady=30)

    window.protocol("WM_DELETE_WINDOW", 'disable_event')
    window.mainloop()


open_window()
