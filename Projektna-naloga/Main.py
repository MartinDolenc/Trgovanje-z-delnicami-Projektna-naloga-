import ystockquote
import tkinter as tk
from tkinter import messagebox

denar = 10000.0
canvas_width = 500.0
canvas_height = 500.0
canvas_zamik = 50.0
kolicina_delnic = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
delnice_po_abecedi = ["amd", "aapl", "kof", "fb", "googl", "intc", "logi", "msft", "tsla", "twtr"]

class Delnice:

    def __init__(self, lokacija, oznaka, okno):
        self.lokacija = lokacija
        self.oznaka = oznaka
        self.trenutna_vrednost = ystockquote.get_last_trade_price(oznaka)
        self.prejsnje_vrednosti = 10*[self.trenutna_vrednost]
        self.okno = okno

        self.posodobi()


    def nakup(self, kolicina):
        global denar

        cena_nakupa = float(ystockquote.get_last_trade_price(self.oznaka))*float(kolicina)

        x = delnice_po_abecedi.index(str(self.oznaka))

        if cena_nakupa <= denar:

            denar -= cena_nakupa
            denar = round(denar, 2)

            kolicina_delnic[x] += int(kolicina)
        else:
            messagebox.showinfo("Error", "Nimate dovolj denarja")

        self.posodobi()


    def prodaja(self, kolicina):
        global denar

        cena_prodaje = float(ystockquote.get_last_trade_price(self.oznaka))*float(kolicina)

        x = delnice_po_abecedi.index(str(self.oznaka))

        if int(kolicina) <= kolicina_delnic[x]:

            denar += cena_prodaje
            denar = round(denar, 2)

            kolicina_delnic[x] -= int(kolicina)
        else:
            messagebox.showinfo("Error", "Nimate dovolj delnic")

        self.posodobi()


    def Canvas_Graf(self):
        self.graf = tk.Canvas(self.okno, width=canvas_width, height=canvas_height)
        self.graf.grid(row=self.lokacija[0], column=self.lokacija[1])
        self.graf.create_line(canvas_zamik, canvas_height-canvas_zamik, canvas_width-canvas_zamik, canvas_height-canvas_zamik, fill="#476042",width=2)
        self.graf.create_line(canvas_zamik, canvas_height-canvas_zamik, canvas_zamik, canvas_zamik, fill="#476042",width=2)
        self.graf.create_text(7, canvas_zamik, text=str((float(self.prejsnje_vrednosti[9])//10)*10 + 10) + " $", anchor="nw")
        self.graf.create_text(7, canvas_height - canvas_zamik, text=str((float(self.prejsnje_vrednosti[9])//10)*10) + " $", anchor="sw")
        self.graf.create_text(canvas_width, 0, text=self.oznaka + ": " + str(self.trenutna_vrednost) + "$", anchor="ne")
        self.graf.create_text(canvas_width, 20, text="število delnic: " + str(kolicina_delnic[delnice_po_abecedi.index(str(self.oznaka))]), anchor="ne")


        razlika_na_y_osi = (canvas_height-2*canvas_zamik)/10

        for x in range(10,0,-1):
            self.graf.create_line(45,(canvas_height - canvas_zamik) - razlika_na_y_osi*x, 55, (canvas_height - canvas_zamik) - razlika_na_y_osi*x, fill="#476042", width=2)


        for x in range(8):
            self.graf.create_line(x*50 + canvas_zamik, ((canvas_height - float(self.prejsnje_vrednosti[x]))%10)*50, (x+1)*50 + canvas_zamik, ((canvas_height - float(self.prejsnje_vrednosti[x+1]))%10)*50, fill="#476042", width=2)


    def posodobi(self):
            self.trenutna_vrednost = ystockquote.get_last_trade_price(self.oznaka)
            self.prejsnje_vrednosti = self.prejsnje_vrednosti[1:] + [self.trenutna_vrednost]
            self.Canvas_Graf()


def shrani_delnice():

    dat = open("shrani.txt", mode="w")

    dat.write(str(kolicina_delnic) + "\n" + str(denar))

    dat.close()


def nalozi_delnice():

    global denar
    global kolicina_delnic

    shranjeno = ""

    shranjeno_samo_števila = []

    dat = open("shrani.txt", mode="r")

    for vrstica in dat:

        shranjeno += vrstica

    a = shranjeno.split("\n")
    b = a[0][1:-1]
    c = b.split(",")

    for x in c:
        shranjeno_samo_števila.append(int(x))

    denar = float(a[1])

    kolicina_delnic = shranjeno_samo_števila

    dat.close()