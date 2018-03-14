#
# ver. 1.0
from tkinter import *
tk = Tk()


def welcome():
    print('hello world')


btn = Button(tk, text='touch me', command=welcome)
btn.pack()
tk.mainloop()
