# author Oleslav Boychuk
# ver. 1.2
from tkinter import *
tk = Tk()


def welcome():
    print('hello world # author Oleslav Boychuk # ver. 1.2')


btn = Button(tk, text='touch me', command=welcome)
btn.pack()
tk.mainloop()
