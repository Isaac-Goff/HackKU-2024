import tkinter

import pyautogui as pg
from tkinter import *
import os


def open_window():
    window = Tk()
    window.title("Falsified")
    s_width = window.winfo_screenwidth()
    s_height = window.winfo_screenheight()

    frame = Frame(window)
    frame.pack()

    check = Button(frame, text="Check Article")
    check.pack(side=BOTTOM, padx=20, pady=30)

    window.geometry('%dx%d+%d+%d' % (s_width / 5, s_height / 6, 1520, 150))
    window.mainloop()


open_window()
