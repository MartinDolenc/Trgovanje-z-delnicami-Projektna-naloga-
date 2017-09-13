import Main
import tkinter as tk
from tkinter import messagebox

okno = tk.Tk()

global denar

denar_str = tk.StringVar()

denar_str.set(str(Main.denar) + " $")

text_input = tk.Entry()
text_input.grid(row=0, column=1)
oznaka = tk.Label(okno, textvariable = denar_str)
oznaka.grid(row=0, column=0)


generiraj = tk.Button(okno, text="generiraj delnico", command=lambda :generiraj_delnico(text_input.get()))
generiraj.grid(row=1, column=1)


kolicina_nakupa = tk.Entry()
kolicina_nakupa.grid(row=3, column=3)
kupi = tk.Button(okno, text="kupi", command=lambda :lambda_nakup())
kupi.grid(row=3, column=4)


kolicina_prodaja = tk.Entry()
kolicina_prodaja.grid(row=4, column=3)
kupi = tk.Button(okno, text="prodaj", command=lambda :lambda_prodaja())
kupi.grid(row=4, column=4)


posodobi = tk.Button(okno, text="posodobi graf", command=lambda: delnica.posodobi())
posodobi.grid(row=2, column=2)


posodobi = tk.Button(okno, text="shrani", command=lambda: shrani())
posodobi.grid(row=6, column=1)


posodobi = tk.Button(okno, text="naloži", command=lambda: nalozi())
posodobi.grid(row=7, column=1)


def shrani():
    Main.shrani_delnice()

def nalozi():
    Main.nalozi_delnice()
    denar_str.set(str(Main.denar) + " $")


def lambda_nakup():
    if je_stevilo(kolicina_nakupa):
        delnica.nakup(kolicina_nakupa.get())
        denar_str.set(str(Main.denar) + " $")
    else:
        messagebox.showinfo("Error", "Neveljaven vnos")


def lambda_prodaja():
    if je_stevilo(kolicina_prodaja):
        delnica.prodaja(kolicina_prodaja.get())
        denar_str.set(str(Main.denar) + " $")
    else:
        messagebox.showinfo("Error", "Neveljaven vnos")


def generiraj_delnico(oznaka):
    global delnica
    global delnice_po_abecedi
    if oznaka in Main.delnice_po_abecedi:
        delnica = Main.Delnice([2,1], oznaka, okno)
    else:
        messagebox.showinfo("Error", "Neveljavna oznaka")

def je_stevilo(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


okno.mainloop()
