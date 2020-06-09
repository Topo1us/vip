import tkinter
from tkinter import *
import os
def lolkek():
    xol='                                                   \n                                 \n                                        '
#МЕНЮ
    def whoami():
        whoami_q=os.system('whoami')
    def help_me():
        l=Label(top,text='Привет, вот список кнопок и их команд:\nwh - whoami (указывает ваш логин в Termux.)',bg='black',fg='white')
        l.place(x=1,y=1)
    def help_m():
        l_2=Label(top,text='кек чебурек'+xol,bg='black',fg='white')
        l_2.place(x=1,y=1)

#ОКНО
    top=Tk()
    top.title('Termux Cod')
    top.configure(bg='black')
#КНОПКИ
    but_1=Button(top,text='help',relief=GROOVE,command=help_me,bg='black',fg='red')
    but_1.place(x=35,y=110)

    but_2=Button(top,text='wh',relief=GROOVE,command=help_m,bg='black',fg='red')
    but_2.place(x=5,y=110)
    top.mainloop()
def passw():
    x=input('код доступа: ')
    if x=='1234':
        lolkek()
    else:
        print('если у вас нет кода доступа обратитесь в тех. поддержку Termux Cod')
passw()
