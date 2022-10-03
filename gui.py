import tkinter as tk
from tkinter import Menu

class GUI:
    def __init__(self):
        pass

    def window(self, t='', b='', sz=''):
        window = tk.Tk()
        window.title(t)
        window.config(bg=b)
        window.geometry(sz)
        window.eval('tk::PlaceWindow . center')
        return window

    def label(self, win=window, t='', fts=0, b='white', fg='black', r=0, c=0, px=0, py=0, ipx=0, ipy=0, s='', cos=1, ros=1):
        label = tk.Label(win, text=t, font=("Arial", fts), bg=b)
        label.grid(row=r, column=c, sticky=s, padx=px, pady=py, columnspan=cos, rowspan=ros)
        return label

    def button(self, win=window, t='', cm=None, h=0, w=0, b='white', fg='black', r=0, c=0, px=0, py=0, ipx=0, ipy=0, s='', cos=1, ros=1):
        button = tk.Button(win, text=t, command=cm, bg=b, height=h, width=w)
        button.grid(row=r, column=c, sticky=s, padx=px, pady=py, columnspan=cos, rowspan=ros)
        return button

    def frame(self, win=window, b="", r=0, c=0, s='', px=0, py=0):
        frame = tk.Frame(win, bg=b, borderwidth="2")
        frame.grid(row=r, column=c, sticky=s, padx=px, pady=py)
        return frame
        
    def mainloop(self, win):
        win.mainloop()




