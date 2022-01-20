from tkinter import *
from tkinter import ttk

characteristics = [["марка", "vaz"],
                    ["год производства", 0],
                    ["пробег", 0],
                    ["цвет", "чёрный"],
                    ["двигатель", 0],
                    ["коробка передач", "механическая"],
                    ["привод", "полный"],
                    ["состояние", "не требует ремонта"],
                    ["владельцы", 2]]


def get_users_ask():
    # создание диалогового окна
    root = Tk()
    root.title("Диалоговое окно")
    root.geometry("700x500")

    # размещаем текстовые указания
    text = Label(root, text="Введите характеристики вашей машины", font=("Arial Bold", 25))
    text.grid(column=0, row=0, columnspan=3)

    lables = []
    forms = []

    for i in range(2, len(characteristics)+2):
        lables.append(Label(root, text = characteristics[i-2][0], font=("Arial Bold", 15)))
        lables[-1].grid(column=0, row=i)
        if characteristics[i-2][0] != 'марка':
            forms.append(Entry(root, width = 30))
        else:
            forms.append(ttk.Combobox(root, textvariable=StringVar(), values=("vaz", 'audi', 'bmw', 'chery', 'chevrolet', 'citroen', 'daewoo')))
            forms[-1].current(0)
        forms[-1].grid(column=1, row=i, sticky='w')

    def clicked():
        table = []
        for i in range(len(characteristics)):
            table.append(forms[i].get())
        for i in range(len(characteristics)):
            characteristics[i][1] = table[i]
        root.destroy()

    enter_b = Button(root, width=10, bg='lightgreen', text="Готово!", command=clicked, font=("Arial Bold", 15))
    enter_b.grid(column=1, row=2*len(characteristics)+4, sticky='s')

    root.mainloop()

    #print(characteristics)

    return {i[0]: i[1] for i in characteristics}