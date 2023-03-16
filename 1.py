import datetime
import threading
from time import *
from datetime import *
from tkinter import *
from multiprocessing import Process
import threading
from tkinter import messagebox
import tkinter as tk

g = 0


def monahdef3():
    qq3.config(text='00')
    qq.config(text='00')
    while True:
        global g  # для кнопки стоп

        g = 0
        x = threading.enumerate()  # для того чтобы небыло второго потока
        try:
            if x[2] == x[2]:
                print('xd')
                return
        except IndexError:
            print('ok')
        x4 = qq1.get()  # получает строку из поля
        qq1.config(show='')  # не работает
        smin = 0  # задать переменные вне цикла(кол во минут)
        ssec = 0  # кол во секунд
        g = 0  # чтоб точно работала
        h2 = int(x4) * 60  # кол во секунд через которые закончить таймер
        h3 = 0
        for i in range(h2 + 1):  # начало цикла таймера
            if g == 1:  # кнопка стоп
                return
            print(h3)
            if h3 == h2:
                ssec = 0
                x = '0'
                qq3.config(text=x + str(smin + 1))
                qq.config(text=x + '0')
                sleep(0.2)
                qq3.config(text='00')
            x = '0'  # для заполнения левого поля когда число меньше 10
            x1 = '0'
            if ssec == 60:  # что делать если секунды дошли до 60
                if g == 1:  # проверка на стоп
                    return
                ssec = 0
                if smin < 10:  # для заполнения левого поля
                    if g == 1:  # проверка на стоп
                        return
                    smin += 1
                    print(smin)
                    qq3.config(text=x + str(smin))
                else:  # добавление минут в таймер
                    if g == 1:
                        return
                    smin += 1
                    qq3.config(text=str(smin))
            while ssec < 10:  # заполнение левого поля
                x = datetime.today()

                if g == 1:
                    return
                qq.config(text=x1 + str(ssec))

                ssec += 1
                if ssec == 9:
                    h3 += 10
                sleep(1)
                # if h3 == h2:
                # x = '0'
                # qq3.config(text=x + str(smin + 1))
                # qq.config(text=x + '0')
                # return
            qq.config(text=str(ssec))  # вывод строки
            ssec += 1
            h3 += 1

            sleep(1)
            if h3 == h2:
                x = '0'
                qq3.config(text=x + str(smin + 1))
                qq.config(text=x + '0')
                tk.messagebox.showinfo(title="#ALARM", message="LEEEETS GO")
        qq3.config(text='00')



def monahg():
    qq3.config(text='00')
    qq.config(text='00')
    global g  # кнопка стоп
    g = 1


def monahdef2():
    qq3.config(text='00')
    qq.config(text='00')
    global g  # для кнопки стоп
    g = 0
    x = threading.enumerate()  # для того чтобы небыло второго потока
    try:
        if x[2] == x[2]:
            print('xd')
            return
    except IndexError:
        print('ok')
    x4 = qq1.get()  # получает строку из поля
    qq1.config(show='')  # не работает
    smin = 0  # задать переменные вне цикла(кол во минут)
    ssec = 0  # кол во секунд
    g = 0  # чтоб точно работала
    h2 = int(x4) * 60  # кол во секунд через которые закончить таймер
    h3 = 0
    for i in range(h2 + 1):  # начало цикла таймера
        if g == 1:  # кнопка стоп
            return
        print(h3, )
        if h3 == h2:
            x = '0'
            qq3.config(text=x + str(smin + 1))
            qq.config(text=x + '0')
            return tk.messagebox.showinfo(title="#ALARM", message="LEEEETS GO")
        x = '0'  # для заполнения левого поля когда число меньше 10
        x1 = '0'
        if ssec == 60:  # что делать если секунды дошли до 60
            if g == 1:  # проверка на стоп
                return
            ssec = 0
            if smin < 10:  # для заполнения левого поля
                if g == 1:  # проверка на стоп
                    return
                smin += 1
                print(smin)
                qq3.config(text=x + str(smin))
            else:  # добавление минут в таймер
                if g == 1:
                    return
                smin += 1
                qq3.config(text=str(smin))
        while ssec < 10:  # заполнение левого поля
            x = datetime.today()

            if g == 1:
                return
            qq.config(text=x1 + str(ssec))

            ssec += 1
            if ssec == 9:
                h3 += 10
            sleep(1)
            if h3 == h2:
                x = '0'
                qq3.config(text=x + str(smin + 1))
                qq.config(text=x + '0')
                return tk.messagebox.showinfo(title="#ALARM", message="LEEEETS GO")
        qq.config(text=str(ssec))  # вывод строки
        ssec += 1
        h3 += 1

        sleep(1)


def monahdef():
    h = threading.Thread(target=monahdef2)  # создание потока
    h.start()


def monahdef1():
    h = threading.Thread(target=monahdef3)  # создание потока
    h.start()


root = Tk()
root.title('ALARM')
root.geometry('500x300')
qq1 = Entry(root)
qqq = Label(root, text="minutes: ", font='monahSL 10')
qq = Label(root, text='00', font="monahSL 15")
qq3 = Label(root, text='00', font="monahSL 15")
qq5 = Button(root, text='ENDLESS', font='monahSL 12', command=monahdef1)
qq2 = Button(root, text='START', font='monahSL 12', command=monahdef)
qq4 = Button(root, text='STOP', font='monahSL 12', command=monahg)
qqq.place(relx=0.3, rely=0.4, anchor='center')
qq4.place(relx=0.5, rely=0.5, anchor='center')
qq2.place(relx=0.5, rely=0.6, anchor='center')
qq5.place(relx=0.5, rely=0.7, anchor='center')
qq.place(relx=0.535, rely=0.3, anchor='center')
qq3.place(relx=0.465, rely=0.3, anchor='center')
qq1.place(relx=0.5, rely=0.4, anchor='center')

root.mainloop()
