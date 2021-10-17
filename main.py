from tkinter import *

# Переменные
width = 5
x_label = 28
x_txt = 65
x_stop = 220
y_stop = 200
quest = False

val_list = ['lbl_sum_5000', 'lbl_sum_2000', 'lbl_sum_1000',
            'lbl_sum_500', 'lbl_sum_200', 'lbl_sum_100', 'lbl_sum_50',
            'lbl_sum_10', 'lbl_sum_5', 'lbl_sum_2', 'lbl_sum_1']

txt_dict = {'txt5000': 5000, 'txt2000': 2000, 'txt1000': 1000, 'txt500':500,
            'txt200': 200, 'txt100': 100, 'txt50': 50, 'txt10': 10, 'txt5': 5, 'txt2': 2, 'txt1': 1}


def cast():
    global quest
    if quest:
        lbl_sum_5000 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_2000 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_1000 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_500 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_200 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_100 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_50 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_10 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_5 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_2 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_1 = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_sum_cash = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_log = Label(wnd, text="              ", font=("Arial Bold", 10))
        lbl_difference = Label(wnd, text="              ", font=("Arial Bold", 10))
        a = 110
        for i in range(len(val_list)):
            eval(f'{val_list[i]}.place(x=x_label + 105, y={a}, anchor="center")')
            a += 20

        lbl_sum_cash.place(x=x_label + 105, y=a, anchor='center')
        lbl_log.place(x=815, y=70, anchor="center")
        lbl_difference.place(x=915, y=70, anchor="center")

    list_sum = []
    for elem, num in txt_dict.items():
        if eval(f'len({elem}.get())') != 0:
            list_sum.append(eval(f'int({elem}.get())*{num}'))
        else:
            list_sum.append(0)

    print(list_sum)

    lbl_sum_5000 = Label(wnd, text=list_sum[0], font=("Arial Bold", 10), anchor="center")
    lbl_sum_2000 = Label(wnd, text=list_sum[1], font=("Arial Bold", 10), justify=CENTER)
    lbl_sum_1000 = Label(wnd, text=list_sum[2], font=("Arial Bold", 10), justify=CENTER)
    lbl_sum_500 = Label(wnd, text=list_sum[3], font=("Arial Bold", 10))
    lbl_sum_200 = Label(wnd, text=list_sum[4], font=("Arial Bold", 10))
    lbl_sum_100 = Label(wnd, text=list_sum[5], font=("Arial Bold", 10))
    lbl_sum_50 = Label(wnd, text=list_sum[6], font=("Arial Bold", 10))
    lbl_sum_10 = Label(wnd, text=list_sum[7], font=("Arial Bold", 10))
    lbl_sum_5 = Label(wnd, text=list_sum[8], font=("Arial Bold", 10), justify=CENTER)
    lbl_sum_2 = Label(wnd, text=list_sum[9], font=("Arial Bold", 10))
    lbl_sum_1 = Label(wnd, text=list_sum[10], font=("Arial Bold", 10))
    lbl_sum_cash = Label(wnd, text=sum(list_sum), font=("Arial Bold", 10))
    lbl_difference = Label(wnd, text=sum(list_sum), font=("Arial Bold", 10))

    a = 110
    for i in range(len(val_list)):
        eval(f'{val_list[i]}.place(x=x_label + 105, y={a}, anchor="center")')
        a += 20
    lbl_sum_cash.place(x=x_label + 105, y=a, anchor='center')

    # Таблица
    if txt_stop_550.get() == '':
        count_stop_550 = 0
    else:
        count_stop_550 = int(txt_stop_550.get())

    if txt_stop_400.get() == '':
        count_stop_400 = 0
    else:
        count_stop_400 = int(txt_stop_400.get())

    sum_cash = sum(list_sum) - 400 * count_stop_400 - 550 * count_stop_550

    lbl_cash_sheet = Label(wnd, text=sum_cash, font=("Arial Bold", 10))
    lbl_cash_sheet.place(x=285, y=70, anchor="center")

    if txt_non_cash.get() == '':
        non_cash = 0
    else:
        non_cash = int(txt_non_cash.get())

    if txt_dop_plus.get() == '':
        dop_plus = 0
    else:
        dop_plus = int(txt_dop_plus.get())

    if txt_dop_minus.get() == '':
        dop_minus = 0
    else:
        dop_minus = int(txt_dop_minus.get())

    if txt_cashbox.get() == '':
        cashbox = 0
    else:
        cashbox = int(txt_cashbox.get())

    print(type(sum_cash), type(non_cash), type(dop_plus), type(dop_minus))

    sum_log = sum_cash + non_cash + dop_plus - dop_minus - cashbox
    sum_difference = sum_log - 5000

    lbl_log = Label(wnd, text=sum_log, font=("Arial Bold", 10))
    lbl_log.place(x=815, y=70, anchor="center")

    lbl_difference = Label(wnd, text=sum_difference, font=("Arial Bold", 10))
    lbl_difference.place(x=915, y=70, anchor="center")

    quest = True


wnd = Tk()

wnd.title("Подсчёт кассы")

wnd.geometry("1000x350")

# Окно постоянных размеров
wnd.resizable(False, False)

# Создание объекта метки (номинал купюры):
lbl_5000 = Label(wnd, text="5000", font=("Arial Bold", 10))
lbl_2000 = Label(wnd, text="2000", font=("Arial Bold", 10))
lbl_1000 = Label(wnd, text="1000", font=("Arial Bold", 10))
lbl_500 = Label(wnd, text="500", font=("Arial Bold", 10))
lbl_200 = Label(wnd, text="200", font=("Arial Bold", 10))
lbl_100 = Label(wnd, text="100", font=("Arial Bold", 10))
lbl_50 = Label(wnd, text="50", font=("Arial Bold", 10))
lbl_10 = Label(wnd, text="10", font=("Arial Bold", 10))
lbl_5 = Label(wnd, text="5", font=("Arial Bold", 10))
lbl_2 = Label(wnd, text="2", font=("Arial Bold", 10))
lbl_1 = Label(wnd, text="1", font=("Arial Bold", 10))

lbl_sum = Label(wnd, text="Сумма", font=("Arial Bold", 10))

# Размещение метки в окне (номинал купюры):
lbl_5000.place(x=x_label, y=100)
lbl_2000.place(x=x_label, y=120)
lbl_1000.place(x=x_label, y=140)
lbl_500.place(x=x_label+5, y=160)
lbl_200.place(x=x_label+5, y=180)
lbl_100.place(x=x_label+5, y=200)
lbl_50.place(x=x_label+10, y=220)
lbl_10.place(x=x_label+10, y=240)
lbl_5.place(x=x_label+15, y=260)
lbl_2.place(x=x_label+15, y=280)
lbl_1.place(x=x_label+15, y=300)
lbl_sum.place(x=x_label+52, y=330, anchor='center')


# Создание объекта поля вода:
txt5000 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt2000 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt1000 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt500 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt200 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt100 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt50 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt10 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt5 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt2 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt1 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))


# Расположение полей для ввода
txt5000.place(x=x_txt, y=100)
txt2000.place(x=x_txt, y=120)
txt1000.place(x=x_txt, y=140)
txt500.place(x=x_txt, y=160)
txt200.place(x=x_txt, y=180)
txt100.place(x=x_txt, y=200)
txt50.place(x=x_txt, y=220)
txt10.place(x=x_txt, y=240)
txt5.place(x=x_txt, y=260)
txt2.place(x=x_txt, y=280)
txt1.place(x=x_txt, y=300)

# Стопчеки

lbl_stop_400 = Label(wnd, text='Стоп-чеков 400:', font=("Arial Bold", 11))
lbl_stop_550 = Label(wnd, text='Стоп-чеков 550:', font=("Arial Bold", 11))

lbl_stop_400.place(x=x_stop, y=y_stop)
lbl_stop_550.place(x=x_stop, y=y_stop+30)

txt_stop_400 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt_stop_550 = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))

txt_stop_400.place(x=x_stop+120, y=y_stop)
txt_stop_550.place(x=x_stop+120, y=y_stop+30)

# Таблица

lbl_cash = Label(wnd, text="Наличные", font=("Arial Bold", 10))
lbl_cash.place(x=250, y=30)

lbl_non_cash = Label(wnd, text="Безналичные", font=("Arial Bold", 10))
lbl_non_cash.place(x=350, y=30)

lbl_dop_plus = Label(wnd, text="Доп +", font=("Arial Bold", 10))
lbl_dop_plus.place(x=480, y=30)

lbl_dop_minus = Label(wnd, text="Доп -", font=("Arial Bold", 10))
lbl_dop_minus.place(x=580, y=30)

lbl_cashbox = Label(wnd, text="Эл. Касса", font=("Arial Bold", 10))
lbl_cashbox.place(x=680, y=30)

lbl_log = Label(wnd, text="В журнал", font=("Arial Bold", 10))
lbl_log.place(x=780, y=30)

lbl_difference = Label(wnd, text="Разница", font=("Arial Bold", 10))
lbl_difference.place(x=880, y=30)

txt_non_cash = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt_non_cash.place(x=350, y=60, width=90)

txt_dop_plus = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt_dop_plus.place(x=470, y=60, width=70)

txt_dop_minus = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt_dop_minus.place(x=570, y=60, width=70)

txt_cashbox = Entry(master=wnd, width=width, justify=CENTER, font=("Arial Bold", 10))
txt_cashbox.place(x=670, y=60, width=80)





# Объект кнопки:
btn = Button(wnd, text="Подсчёт", font=("Courier New Bold", 13), command=cast)

# Размещение объекта кнопки в окне:
btn.place(x=500, y=300, width=160, height=30)


wnd.mainloop()
