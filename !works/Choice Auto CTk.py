from customtkinter import *
from tkinter import *
import tkinter.filedialog, tkinter.messagebox, tkinter.colorchooser
from datetime import date

root = Tk()
w = root.winfo_screenwidth() / 2 - 750
h = root.winfo_screenheight() / 2 - 225
root.geometry(f'1500x450+{int(w)}+{int(h)}')
root['bg'] = 'grey40'
root.title('Вибір Авто')
root.resizable(width=False, height=False)

def selectColor():
    global color
    color = tkinter.colorchooser.askcolor(parent=root, initialcolor='#f1f1f1')
    viewColor.configure(fg_color=color[1])

def insertRes():
    txt.delete('1.0', 'end')
    for i in selected:
        txt.insert('end', str(i) + '\n')

def selectedFunc():
    global color
    try:
        now = date.today()
        selected.clear()
        selected.append(brands[langBrands.get()])
        selected.append(years[langYears.get()])
        selected.append(f'''Об'єм двигуна:  {engineCapacity[langEngineCapacity.get()]}''')
        selected.append(f'Вид двигуна:  {typeOfEngine[langTypeOfEngine.get()]}')
        selected.append(f'Модель:  {combbox.get()}\n')
        selected.append('Тюнінг')
        selected.append(langTuning1.get())
        selected.append(langTuning2.get())
        selected.append(langTuning3.get())
        selected.append(f'Колір:  {color[1]}\n')
        selected.append(f'Час створення запиту: {now}')
        insertRes()
    except NameError:
        pass

def save():
    if combbox.get() == 'Не обрано':
        tkinter.messagebox.showwarning('Зауваження', f'Ви не обрали модель автомобіля {brands[langBrands.get()]}')
    else:
        saveFile = tkinter.filedialog.asksaveasfilename(parent=root, defaultextension='txt', filetypes=[("Текстові файли", "*.txt"), ("Усі файли", "*.*")], title="Вибрати файли", initialfile='Моя машина')
        if saveFile:
            with open(saveFile, 'w') as file:
                file.write(txt.get("1.0", 'end'))
        else:
            pass

def updateModels(*args):
    langModelOfCar.set('Не обрано')
    combbox.configure(values=modelOfCar[langBrands.get()])

def rootDestroy():
    if tkinter.messagebox.askokcancel('Вихід', 'Ви дійсно хочете вийти? Все не збережне буде знищено'):
        root.destroy()

def tabs():
    global lF1_1, lF1_2, lF1_3, lF2_1, lF2_2, lF2_3, combbox, lF2_4, viewColor, txt
    lFrames = ['Дані про автомобіль', 'Рік випуску', 'Марка автомобіля']
    lFrames1 = ["Об'єм двигуна", 'Вид двигуна', 'Модель автомобіля', 'Тюнінг автомобіля']


    xIter = 50
    yIter = 65
    xIter1 = 0
    yIter1 = 10
    for i in lFrames:
        if i == 'Марка автомобіля':
            v = -1
            yIter1 = 10
            lF1_1 = LabelFrame(root, text=f'{i}', width=210, height=345, background='grey40', foreground='white',
                               relief='ridge')
            lF1_1.place(x=xIter, y=65)
            for j in brands:
                v += 1
                radbtn = CTkRadioButton(lF1_1, text=f'{j}', hover_color='darkseagreen2', corner_radius=3,
                                    fg_color='darkseagreen4', text_color='khaki', variable=langBrands, value=v, command=selectedFunc)
                radbtn.place(x=5, y=yIter1)
                yIter1 += 40
        elif i == 'Рік випуску':
            v = -1
            yIter += 155
            lF1_2 = LabelFrame(root, text=f'{i}', width=210, height=190, background='grey40',
                               foreground='white', relief='ridge', )
            lF1_2.place(x=50, y=yIter)
            xIter += 20
            yIter1 = 10
            for j in years:
                v += 1
                radbtn1 = CTkRadioButton(lF1_2, text=f'{j}', hover_color='darkseagreen2', corner_radius=3,
                                    fg_color='darkseagreen4', text_color='khaki', variable=langYears, value=v, command=selectedFunc)
                radbtn1.place(x=5, y=yIter1)
                yIter1 += 40
        else:
            lF1_3 = LabelFrame(root, text=f'{i}', width=210, height=120, background='grey40', foreground='white',
                               relief='ridge')
            lF1_3.place(x=xIter, y=yIter)
            xIter += 250

            chbx = CTkCheckBox(lF1_3, text=f'Новий автомобіль', hover_color='darkseagreen2', corner_radius=3,
                               checkmark_color='white', fg_color='darkseagreen4', text_color='khaki', variable=langDataAboutCar, command=selectedFunc, onvalue='Новий автомобіль: Так', offvalue='Іноземне виробництво: Ні')
            chbx.place(x=5, y=yIter1)
            chbx1 = CTkCheckBox(lF1_3, text=f'Іноземного виробництва', hover_color='darkseagreen2', corner_radius=3,
                               checkmark_color='white', fg_color='darkseagreen4', text_color='khaki', variable=langDataAboutCar1, command=selectedFunc, onvalue='Іноземне виробництво: Так', offvalue='Іноземне виробництво: Ні')
            chbx1.place(x=5, y=50)
            yIter1 += 40
    xIter = 50
    yIter = 65
    xIter1 = 0
    yIter1 = 10
    for i in lFrames1:
        if i == "Об'єм двигуна":
            v = -1
            xIter = 610
            lF2_1 = LabelFrame(root, text=f'{i}', width=210, height=190, background='grey40', foreground='white',
                               relief='ridge')
            lF2_1.place(x=840, y=65)
            for j in engineCapacity:
                v += 1
                radbtn = CTkRadioButton(lF2_1, text=f'{j}', hover_color='darkseagreen2', corner_radius=3,
                                        fg_color='darkseagreen4', text_color='khaki', variable=langEngineCapacity, value=v,
                                        command=selectedFunc)
                radbtn.place(x=10, y=yIter1)
                yIter1 += 40
        elif i == 'Вид двигуна':
            v = -1
            yIter += 305
            lF2_2 = LabelFrame(root, text=f'{i}', width=210, height=110, background='grey40',
                               foreground='white', relief='ridge', )
            lF2_2.place(x=840, y=300)
            xIter += 20
            yIter1 = 10
            for j in typeOfEngine:
                v += 1
                radbtn1 = CTkRadioButton(lF2_2, text=f'{j}', hover_color='darkseagreen2', corner_radius=3,
                                         fg_color='darkseagreen4', text_color='khaki', variable=langTypeOfEngine, value=v,
                                         command=selectedFunc)
                radbtn1.place(x=5, y=yIter1)
                yIter1 += 40
        elif i == 'Модель автомобіля':
            lF2_3 = LabelFrame(root, text=f'{i}', width=210, height=110, background='grey40', foreground='white',
                               relief='ridge')
            lF2_3.place(x=580, y=65)
            xIter += 250
            val = 2
            combbox = CTkComboBox(lF2_3, values=[], state='readonly', corner_radius=3,
                                  fg_color='darkseagreen4', text_color='khaki', variable=langModelOfCar, width=180,)
            combbox.place(x=10, y=10)
            combbox.configure(values=modelOfCar[langBrands.get()])
            langBrands.trace('w', lambda *args: updateModels())
            yIter1 += 40
        else:
            v = -1
            lF2_4 = LabelFrame(root, text=f'{i}', width=210, height=200, background='grey40', foreground='white',
                               relief='ridge')
            lF2_4.place(x = 580, y = 210)
            btnChooseColor = CTkButton(lF2_4, text='Вибрати колір автомобіля', width=165, hover_color='darkseagreen2', corner_radius=3,
                                         fg_color='darkseagreen4', text_color='khaki',
                                         command=selectColor)
            btnChooseColor.place(x = 5, y = 10)
            viewColor = CTkFrame(lF2_4, width=26, height=28,)
            viewColor.place(x = 175, y = 10)
            chbbx = CTkCheckBox(lF2_4, text=f'Спойлер', hover_color='darkseagreen2', corner_radius=3,
                               checkmark_color='white', fg_color='darkseagreen4', text_color='khaki',
                               variable=langTuning1, command=selectedFunc, onvalue='Спойлер: Так',
                               offvalue='Спойлер: Ні')
            chbbx.place(x = 10, y = 50)
            chbbx1 = CTkCheckBox(lF2_4, text=f'Сплітер', hover_color='darkseagreen2', corner_radius=3,
                                checkmark_color='white', fg_color='darkseagreen4', text_color='khaki',
                                variable=langTuning2, command=selectedFunc, onvalue='Сплітер: Так',
                                offvalue='Сплітер: Так')
            chbbx1.place(x=10, y=95)
            chbbx2 = CTkCheckBox(lF2_4, text=f'Обвіс кузова', hover_color='darkseagreen2', corner_radius=3,
                                checkmark_color='white', fg_color='darkseagreen4', text_color='khaki',
                                variable=langTuning3, command=selectedFunc, onvalue='Обвіс кузова: Так',
                                offvalue='Обвіс кузова: Так')
            chbbx2.place(x=10, y=140)

        txt = CTkTextbox(root, width=360, height=290, fg_color='white', border_width=2, corner_radius=4, border_color='grey30', text_color='black', font=(None, 21), )
        txt.place(x = 1090, y = 70)
        txtButton1 = CTkButton(root, text='Вивести результат', hover_color='darkkhaki', corner_radius=3, fg_color='darkseagreen4', text_color='white', command=insertRes,)
        txtButton1.place(x = 1110, y = 370)
        txtButton2 = CTkButton(root, text='Зберегти результат', hover_color='darkkhaki', corner_radius=3, fg_color='darkseagreen4', text_color='white', command=save)
        txtButton2.place(x=1290, y=370)

root.protocol('WM_DELETE_WINDOW', rootDestroy)
selected = []
engineCapacity = ['Менше 1200', '1200-1500', '1501-2200', 'Більше 2200']
typeOfEngine = ['Бензин', 'Дизель']
modelOfCar = [['M5 Competition', 'i8', 'E39 M5'], ['Maybach S-Class', 'GLE', 'AMG GT 63 S'], ['911 Turbo S', 'Panamera Turbo S', 'Carrera GT'], ['Golf GT', 'Jetta', 'Tiguan'], ['2107', '2115', '21099'],
              ['RS Q8', 'Audi R8 V10 Plus', 'A6'], ['Corvette Z06', 'Camaro ZL1', 'Impala 1967'], ['Mustang Shelby GT500', 'F-150 Raptor', 'Focus RS']]
tuning = ['Спойлер', 'Сплітер', 'Обвіс кузова']
years = ['До 5 років', '6-10 років', '11-15 років', 'Більше 15 років']
brands = ['BMW', 'Mercedes', 'Porsche', 'Volkswagen', 'VAZ', 'Audi', 'Chevrolet', 'Ford']
langBrands = IntVar()
langYears = IntVar()
langDataAboutCar = StringVar(value='Новий автомобіль: Так')
langDataAboutCar1 = StringVar(value='Іноземне виробництво: Ні')
langTypeOfEngine = IntVar()
langEngineCapacity = IntVar()
langModelOfCar = StringVar(value='Не обрано')
langTuning1 = StringVar(value='Спойлер:  Ні')
langTuning2 = StringVar(value='Сплітер:  Ні')
langTuning3 = StringVar(value='Обвіс кузова:  Ні')


tabs()

root.mainloop()