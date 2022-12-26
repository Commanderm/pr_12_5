from tkinter import IntVar
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


buttons = []
labels = []

def print_string(name):
    print(f'{name}')

def close_window():
    window.destroy()

def showMatrix(matrix):
    count = 0
    coolrow = 2
    print(matrix)
    for widget in window.winfo_children():
        if widget.widgetName != "label":
            widget.destroy()

    lbl = ttk.Label(window, text=" ")
    lbl.grid(column=0, row=coolrow)
    labels.append(lbl)
    coolrow = coolrow + 1

    for r in range(x):
        coolrow = coolrow + 1
        for c in range(x):
            print(matrix[count])
            lbl = ttk.Label(window, text=matrix[count])
            lbl.grid(column=c, row=coolrow)
            labels.append(lbl)
            count = count + 1

    coolrow = coolrow + 1
    lbl = ttk.Label(window, text=" ")
    lbl.grid(column=0, row=coolrow)
    labels.append(lbl)
    coolrow = coolrow + 1
    count = 0
    matrix.sort()
    print(matrix)

    half = int(len(matrix) / 2)
    matrix[:half], matrix[half:] = matrix[half:], matrix[:half]

    for r in range(x):
        coolrow = coolrow + 1
        for c in range(x):
            print(matrix[count])
            lbl = ttk.Label(window, text=matrix[count])
            lbl.grid(column=c, row=coolrow)
            labels.append(lbl)
            count = count + 1

    coolrow = coolrow + 1
    lbl = ttk.Label(window, text=" ")
    lbl.grid(column=0, row=coolrow)
    labels.append(lbl)
    coolrow = coolrow + 1
    clickButton2 = ttk.Button(window, command=close_window, text="Выход", width=10)
    clickButton2.grid(column=(c % 2), row=coolrow) # поменять
    labels.append(clickButton2)

def convertStr(s):  # Конвертируем Str в Int
    try:
        ret = int(s)
    except ValueError:
        messagebox.showerror('Ошибка!', 'Вводить можно только цифры!')  # показывает сообщение об ошибке
        ret = "error"
    return ret

def autoCreate(sz):
    siz = sz*sz
    items = np.random.randint(1, high=101, size=siz)

    return items.tolist()

def addMass():
    global z
    global errs
    errs = 0
    items = [[0 for i in range(x)] for j in range(x)]
    arr_t = []

    for i in range(x):
        for j in range(x):
            z = convertStr(var[i][j].get())
            if z != "error":
                if z < 1 or z > 100 :
                    messagebox.showwarning('Предупреждение!',
                                           'значения в матрице могут быть от 1 до 100 включительно.')
                else:
                    items[i][j] = z
            else:
                errs = errs + 1

    if errs == 0 :
        for a in items:
            arr_t += a
        showMatrix(arr_t)

#        s =list(chain.from_iterable(map(str, items)))
#        print(list(filter(str.isdigit, s)))

#def clicked2():

def clicked():
    m = combo.get()
    global x
    global var
    x = convertStr(m)
    var = []
    for j in range(x):
        var.append([StringVar() for i in range(x)])

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
            if selected.get() == 1:
                lbl2.configure(text="С автоматическим заполнением", font=("Arial Bold", 12))
                showMatrix(autoCreate(x))
            else:
                lbl2.configure(text="С ручным заполнением", font=("Arial Bold", 12))
                for r in range(x):
                    for c in range(x):
                        spinb = ttk.Spinbox(window, textvariable=var[r][c], from_=1, to=100, width=2)
                        #spinb = ttk.Spinbox(window, textvariable=var, from_=1, to=100, width=2, command=clicked2)
                        spinb.grid(column=c, row=r+3)
                        buttons.append(spinb)

                clickButton = ttk.Button(window, command=addMass, text="Заполнить", width=10)
                clickButton.grid(column= (c%2), row=r+5)
                buttons.append(clickButton)

            lbl1.configure(text=res)
            lbl4.configure(text=" ")
            combo.destroy()
            rad1.destroy()
            rad2.destroy()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.title("Практическая работа 12, вариант 5")
    window.geometry('1024x720')
    lbl1 = Label(window, text="Для создания квадратной матрицы MxM укажите её размерность M.\n"
                             "M может быть только чётным числом из диапазона [2, 8]", font=("Arial Bold", 12))
    lbl1.grid(column=0, row=0)
    lbl2 = Label(window, text=" ")
    lbl2.grid(column=0, row=1)

    combo = ttk.Combobox(window, width=2)
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