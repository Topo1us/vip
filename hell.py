#!/usr/bin/python
import tkinter
from tkinter import *
ok=tkinter.Tk()
ok.configure(bg='black')
ok.title('Termux Cod')
lat=Label(ok,text='если у вас нет кода доступа\nобратитесь в тех.поддержку группы Termux Cod.',bg='black',fg='yellow')
en=Entry(ok,show='*')
but=Button(ok,text='войти',bg='black',fg='green')
but_2=Button(ok,text='выйти',command=ok.quit,bg='black',fg='red')
lat.pack()
en.pack()
but.pack()
but_2.pack()
ok.mainloop()
