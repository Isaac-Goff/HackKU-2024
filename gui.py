import pyautogui as pg
import wx
import os

class main_window(wx.Frame):
    def __init__(self):

        wx.Frame.__init__(self, None, style=wx.TRANSPARENT_WINDOW,pos=(1080, 30))
        panel = wx.Panel(self)
        self.amount = 75
        self.delta = -5
        self.Show()
        self.SetTransparent(self.amount)


app = wx.App(False)
frame = main_window()
app.MainLoop()