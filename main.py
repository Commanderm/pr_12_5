# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import IntVar

import nump as nump
import numpy as np
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from numpy import ndarray

#buttons = []

def print_string(name):
    print(f'{name}')

def convertStr(s):  # Rjydthnbhetv Str в Int
    try:
        ret = int(s)
    except ValueError:
        messagebox.showerror('Ошибка!', 'Вводить можно только цифры!')  # показывает сообщение об ошибке
        ret = "error"
    return ret

def autoCreate(sz):
    items: int | ndarray[int] = np.random.randint(1, high=101, size=sz*sz)
    #print(len(items), items[:sz*sz])  # 100000 [73846 49707 18846 73887 43349]
    return items

def clicked():
    m = combo.get()
    x = convertStr(m)

    if x != "error" :
        if x < 2 or x > 8 :
            messagebox.showwarning('Предупреждение!',
                                   'Размерность матрицы может быть от 2 до 8')  # показывает предупреждающее сообщение
        elif x % 2 != 0:
            messagebox.showwarning('Предупреждение!',
                                   'Размерность матрицы может быть только чётным числом. Вы ввели не чётное число!')  # показывает предупреждающее сообщение
        else:
            res = "Выбрано создание матрицы {} ".format(m)
            res = res+"x {}".format(m)
            if selected.get() == 1 :
                lbl2.configure(text="С автоматическим заполнением", font=("Arial Bold", 12))
                items = autoCreate(x)
            else:
                lbl2.configure(text="С ручным заполнением", font=("Arial Bold", 12))
                frame.matrix.clear()
                for r in range(x):
                    line = []
                    for c in range (x):
                        spin = Spinbox(frame, from_=1, to=100, width=3)
                        spin.grid(column=c, row=r+2)
                        #                       ____b = Spinbox(window, from_=1, to=100, width=2)
 #                       ____b.grid(column=c, row=r+3)
 #                       ____b.pack()
 #                       ____buttons.append(b)

            lbl1.configure(text=res)
            lbl4.configure(text=" ")
            combo.destroy()
            rad1.destroy()
            rad2.destroy()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.title("Практическая работа 12, вариант 5")

    frame = Frame(window)
    frame.matrix = []
    frame.grid(row=0, column=0, columnspan=2)

    lbl1 = Label(frame, text="Для создания квадратной матрицы MxM укажите её размерность M.\n"
                             "M может быть только чётным числом из диапазона [2, 8]", font=("Arial Bold", 12))
    lbl1.grid(column=0, row=0)
    lbl2 = Label(frame, text=" ")
    lbl2.grid(column=0, row=1)

    combo = Combobox(window, width=2)
    combo['values'] = (2, 4, 6, 8)
    combo.current(0)  # установите вариант по умолчанию
    combo.grid(column=0, row=2)
    combo.focus()

    lbl3 = Label(window, text=" ")
    lbl3.grid(column=0, row=3)

    lbl4 = Label(window, text="Как вы хотите заполнить полученную матицу?")
    lbl4.grid(column=0, row=4)

    selected: IntVar = IntVar()
    rad1 = Radiobutton(window, text='Автоматически', value=1, variable=selected, command=clicked)
    rad2 = Radiobutton(window, text='Вручную', value=2, variable=selected, command=clicked)
    rad1.grid(column=0, row=5)
    rad2.grid(column=0, row=6)

    #txt = Entry(window, width=10)
    #txt.grid(column=0, row=2)
    #txt.focus()
    #lbl5 = Label(window, text=" ")
    #lbl5.grid(column=0, row=7)
    #btn = Button(window, text="Клик!", command=clicked)
    #btn.grid(column=0, row=8)
    window.mainloop()

    np.random.rand(2,3)

