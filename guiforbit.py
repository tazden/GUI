import tkinter as tk
from tkinter import *
import numexpr as ne
import numpy as np
import PIL
from sympy import *
import scipy.integrate as integrate
import scipy.special as special
import torch
import math
import matplotlib as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
win=tk.Tk()
win.title('GUI1')
win.geometry('1600x1600')
frame1=tk.Frame(win)
frame1.place(relx=0.05,rely=0)
tk.Label(frame1,text='Студент: Тазтдинов Денис\nФакультет:АиВТ\nГруппа:АЭ-21-03',bg='#00ccfa',font='Times 20').pack()
frame2=tk.Frame(win)
frame2.place(relx=0.05,rely=0.12)
tk.Label(frame2,text='Введите согласно варианту:',font='Times 20',fg='red').pack()
frame4=tk.Frame(win)
frame4.place(relx=0.05,rely=0.16)
tk.Label(frame4,text='Функцию',font='Times 15',bg='gray').pack(fill=X)
funck=StringVar()
tk.Entry(frame4,textvariable=funck).pack()
frame5=tk.Frame(win)
frame5.place(relx=0.15,rely=0.16)
tk.Label(frame5,text='Интервал',font='Times 15',bg='gray').pack(fill=X)
levinterv=IntVar()
pravinterv=IntVar()
frtable=Frame(win)
tk.Entry(frame5,textvariable=levinterv).pack(side='left')
tk.Entry(frame5,textvariable=pravinterv).pack(side='left')
sos=Frame(win)
frame15=tk.Frame(win)
N=StringVar()
tk.Entry(frame15,textvariable=N).pack()
frame15.place(relx=0.05,rely=0.75)
def f():
    frame100=tk.Frame(win)
    frame101 = tk.Frame(win)
    Y=[]
    X=[]
    n=levinterv.get()
    p=pravinterv.get()
    fofo=funck.get()
    tk.Label(frame100, text='X').grid(column=0)
    tk.Label(frame101, text='Y').grid(column=0)
    for x in range (n,p+1):
        X.append(x)
        Y.append(eval(fofo))
        tk.Label(frame100,text=x).grid(column=0)
        tk.Label(frame101, text=eval(fofo)).grid(column=0)
    frame100.place(relx=0.85,rely=0)
    frame101.place(relx=0.88, rely=0)
    graph = Frame(win, bg='red')  # создание графика
    f = Figure()
    pt = f.add_subplot(111)
    pt.plot(X, Y)
    pt.set_xlabel('Ось X', fontsize=15)
    pt.set_ylabel('Ось Y', fontsize=15)
    canvas = FigureCanvasTkAgg(f, master=graph)
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
    graph.place(relx=0.27, rely=0.15)
    print(X)
    print(Y)
def ochistrka():
    graph1 = Frame(win, bg='red')  # создание графика
    f1 = Figure()
    pt1 = f1.add_subplot(111)
    pt1.set_xlabel('Ось X', fontsize=20)
    pt1.set_ylabel('Ось Y', fontsize=20)
    canvas1 = FigureCanvasTkAgg(f1, master=graph1)
    canvas1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    graph1.place(relx=0.27, rely=0.15)
def pv1():
    Y1=[]
    X = []
    n = levinterv.get()
    p = pravinterv.get()
    fofo = funck.get()
    for x in range(n, p + 1):
        rw = 1
        col = 1
        tk.Label(frtable, text=x).grid(row=rw, column=col)
        tk.Label(frtable, text=eval(fofo)).grid(row=rw, column=col)
        X.append(x)
        rw += 1
        col += 1
    for x in range(n, p + 1):
        x=Symbol('x')
        y=fofo.diff(x)
        Y1.append(y)
    graph = Frame(win, bg='red')  # создание графика
    f = Figure()
    pt = f.add_subplot(111)
    pt.plot(X, Y1)
    pt.set_xlabel('Ось X', fontsize=20)
    pt.set_ylabel('Ось Y', fontsize=20)
    canvas = FigureCanvasTkAgg(f, master=graph)
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)
    graph.place(relx=0.33, rely=0.15)
    print(X)
    print(Y1)
def miin():
    frame9=tk.Frame(win,)
    Y = []
    X = []
    n = levinterv.get()
    p = pravinterv.get()
    fofo = funck.get()
    for x in range(n, p + 1):
        rw = 1
        col = 1
        tk.Label(frtable, text=x).grid(row=rw, column=col)
        tk.Label(frtable, text=eval(fofo)).grid(row=rw, column=col)
        X.append(x)
        Y.append(eval(fofo))
    tk.Label(frame9, text='x',bg='lightgreen').grid()
    tk.Label(frame9,text=min(X),bg='lightgreen').grid()
    tk.Label(frame9, text='y',bg='blue').grid(row=0,column=1)
    tk.Label(frame9, text=min(Y),bg='blue').grid(row=1,column=1)
    frame9.place(relx=0.16,rely=0.46)
def nuli():
    frame10=tk.Frame(win,)
    tk.Label(frame10, text='x0', bg='lightgreen').grid()
    tk.Label(frame10, text='Отсутствует', bg='lightgreen').grid()
    tk.Label(frame10, text='y0', bg='blue').grid(row=0, column=1)
    tk.Label(frame10, text='Отсутствует', bg='blue').grid(row=1, column=1)
    frame10.place(relx=0.16,rely=0.52)
def igr():
    frame99=tk.Frame(win)
    import numpy as np
    import matplotlib.pyplot as plt
    f = lambda x: 1 / (1 + x ** 2)
    a = 0
    b = 5
    N = 10
    n = 10  # Use n*N+1 points to plot the function smoothly
    x = np.linspace(a, b, N + 1)
    y = f(x)
    X = np.linspace(a, b, n * N + 1)
    Y = f(X)
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.plot(X, Y, 'b')
    x_left = x[:-1]  # Left endpoints
    y_left = y[:-1]
    plt.plot(x_left, y_left, 'b.', markersize=10)
    plt.bar(x_left, y_left, width=(b - a) / N, alpha=0.2, align='edge', edgecolor='b')
    plt.title('Left Riemann Sum, N = {}'.format(N))
    dx = (b - a) / N
    x_left = np.linspace(a, b - dx, N)
    print("Partition with", N, "subintervals.")
    left_riemann_sum = np.sum(f(x_left) * dx)
    tk.Label(frame99,text=left_riemann_sum,bg='blue').pack()
    frame99.place(relx=0.1,rely=0.75)
b1=tk.Button(win,text='Вывод графика',font='Times 13',fg='white',bg='red',command=f)
b1.place(relx=0.05,rely=0.23)
b2=tk.Button(win,text='Очистка координатной плоскости',font='Times 13',fg='white',bg='red',command=ochistrka)
b2.place(relx=0.05,rely=0.28)
b3=tk.Button(win,text='График первой производной',font='Times 13',fg='white',bg='red',command=pv1)
b3.place(relx=0.05,rely=0.34)
b4=tk.Button(win,text='График второй производной',font='Times 13',fg='white',bg='red')
b4.place(relx=0.05,rely=0.4)
b5=tk.Button(win,text='MIN',font='Times 13',fg='white',bg='red',command=miin)
b5.place(relx=0.05,rely=0.46)
b5=tk.Button(win,text='Нули функции',font='Times 13',fg='white',bg='red',command=nuli)
b5.place(relx=0.05,rely=0.52)
b6=tk.Button(win,text='Интеграл',font='Times 13',fg='white',bg='red',command=igr)
b6.place(relx=0.05,rely=0.65)
frame6=Frame(win)
frame6.place(relx=0.33,rely=0)
tk.Label(frame6,text='Домашнее задание',font='Times 40',bg='yellow').pack()
frame7=Frame(win)
win.mainloop()
