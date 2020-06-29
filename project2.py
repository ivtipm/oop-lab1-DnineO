from tkinter import *
import random

window = Tk()
window.title("TIME")
window.configure(bg='khaki1')
window.geometry("700x500")


class countTime():  # создание класса
    def __init__(self):
        pass

    def Clicked(self):  # этот метод (функция) создает переменные нашего класса из полученных данных из пользователя
        self.hour1 = int(hour1.get())
        self.minute1 = int(minute1.get())
        self.second1 = int(second1.get())
        self.hour2 = int(hour2.get())
        self.minute2 = int(minute2.get())
        self.second2 = int(second2.get())
        self.minPlus = minPlus.get()

        if self.minPlus == "+":  # принимем из пользователя операцию (+ или -)и вычисляем время соотвественно
            if self.minute1>=60 or self.minute2>=60 or self.second1>=60 and self.second2>=60:
                print("Некорректные данные!")
            if self.hour1>=24 or self.hour2>=24:
                print("Некорректные данные!")
            resSec = int(self.second1 + self.second2)
            resMin = int(self.minute1 + self.minute2)
            resHour = int(self.hour1 + self.hour2)

            if resSec > 60:
                self.resSec = resSec - 60
                resMin += 1
            elif resSec == 60:
                self.resSec = 0
                resMin += 1
            else:
                self.resSec = resSec

            if resMin > 60:
                self.resMin = resMin - 60
                resHour += 1
            elif resMin == 60:
                self.resMin = 0
                resHour += 1
            else:
                self.resMin = resMin

            if resHour > 24:
                self.resHour = resHour - 24
            elif resHour == 24:
                self.resHour = 00
            else:
                self.resHour = resHour
        elif self.minPlus == "-":
            resSec = int(self.second1 - self.second2)
            resMin = int(self.minute1 - self.minute2)
            resHour = int(self.hour1 - self.hour2)
            if resSec > 0:
                self.resSec = resSec
            elif resSec == 60:
                self.resSec = 0
            else:
                self.resSec = resSec + 60
                resMin -= 1

            if resMin > 0:
                self.resMin = resMin
            elif resMin == 60:
                self.resMin = 0
            else:
                self.resMin = resMin + 60
                resHour -= 1

            if resHour > 0:
                self.resHour = resHour
            elif resHour == 24:
                self.resHour = 00
            else:
                if self.hour2 > 12:
                    self.resHour = 12 + resHour
                else:
                    self.resHour = 24 + resHour

    def time_to_words(self, number):  # метод для конвертирования число в слово
        f = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
             # прописи цифр сохраним в словаре чтобы потом использовать при конвертировании
             6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
        l = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
             50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
             80: 'восемьдесят', 90: 'девяносто'}
        s = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
             14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
             17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
        n1 = number % 10
        n2 = number - n1
        if (number < 10):
            return (f.get(number))
        elif 10 < number < 20:
            return (s.get(number))
        elif number >= 10 and number in l:
            return (l.get(number))
        else:
            return (l.get(n2) + ' ' + f.get(n1))


def Start():  # этот функция вызывается при нажатии на кнопки "перевод" так как там вложена метод command,и как видно не является методом нашего класса
    time1 = countTime()  # создадим новый экземпляр класса
    time1.Clicked()  # вызываем этот метод для сбора данных и вычислении времени
    answer = str(time1.resHour) + ":" + str(time1.resMin) + ":" + str(time1.resSec)
    showAnswer = Label(window, text=answer, font=("Times New Roman", 20), bg="khaki1", fg="black").grid(column=1, row=7,
                                                                                                        columnspan=3)

    convertedSec = (time1.hour1 * 3600) + (time1.minute1 * 60) + (time1.second1)  # конвертируем в секунды
    convertedMin = "%.2f" % (convertedSec / 60)  # конвертирем в минуты
    convertedHour = "%.2f" % (convertedSec / 3600)  # конвертируем в часы

    convShow1 = Label(window, text=convertedSec, font=("Times New Roman", 20), bg="white", fg="black").grid(column=4,
                                                                                                            row=0)
    convShow2 = Label(window, text=convertedMin, font=("Times New Roman", 20), bg="white", fg="black").grid(column=4,
                                                                                                            row=2)
    convShow3 = Label(window, text=convertedHour, font=("Times New Roman", 20), bg="white", fg="black").grid(column=4,
                                                                                                             row=5)
    min = time1.time_to_words(time1.minute1)
    hour = time1.time_to_words(time1.hour1)
    if time1.minute1 == 0:
        min = " "
    elif time1.hour1 == 0:
        hour = "дванадцать"
    time = "Время:" + " " + str(hour) + " " + str(min)  # использем метод time_to_words нашего класса
    numberinWord = Label(window, text=time, font=("Times New Roman", 25), bg="khaki1", fg="black").grid(column=0, row=8,
                                                                                                        columnspan=5)


const1 = Label(window, text="В секунды:", font=("Times New Roman", 25), bg="khaki1", fg="black").grid(column=3, row=0,
                                                                                                      padx=20)  # создание интерфейса в tkinter
const2 = Label(window, text="В минуты:", font=("Times New Roman", 25), bg="khaki1", fg="black").grid(column=3, row=2,
                                                                                                     padx=20)
const3 = Label(window, text="В часы:", font=("Times New Roman", 25), bg="khaki1", fg="black").grid(column=3, row=5,
                                                                                                   padx=20)

instruct1 = Label(window, text="Часы", font=("Times New Roman", 25), bg="khaki1", fg="black").grid(column=0, row=0)
instruct2 = Label(window, text="Мин.", font=("Times New Roman", 25), bg="khaki1", fg="black").grid(column=1, row=0)
instruct3 = Label(window, text="Сек.", font=("Times New Roman", 25), bg="khaki1", fg="black").grid(column=2, row=0)

hour1 = Entry(window, width=5, font=("Times New Roman", 20))
hour1.grid(column=0, row=1, padx=25, pady=10)

minute1 = Entry(window, width=5, font=("Times New Roman", 20))
minute1.grid(column=1, row=1, padx=25, pady=10)

second1 = Entry(window, width=5, font=("Times New Roman", 20))
second1.grid(column=2, row=1, padx=25, pady=10)

inst = Label(window, text=" '+' или '-' ", font=("Times New Roman", 13), bg="khaki1", fg="black").grid(column=0, row=2)

minPlus = Entry(window, width=5, font=("Times New Roman", 20))
minPlus.grid(column=1, row=2, padx=25, pady=10)

hour2 = Entry(window, width=5, font=("Times New Roman", 20))
hour2.grid(column=0, row=4, padx=25, pady=10)
minute2 = Entry(window, width=5, font=("Times New Roman", 20))
minute2.grid(column=1, row=4, padx=25, pady=10)
second2 = Entry(window, width=5, font=("Times New Roman", 20))
second2.grid(column=2, row=4, padx=25, pady=10)
ready = Label(window, text="Готово!", font=("Times New Roman", 25), bg="khaki1", fg="black").grid(column=1, row=6,
                                                                                                  columnspan=3)

but1 = Button(text="Перевод", bd=2, font=("Times New Roman", 15), bg="black", width=10, fg="white", command=Start).grid(
    column=1, row=5, pady=10)

window.mainloop()
