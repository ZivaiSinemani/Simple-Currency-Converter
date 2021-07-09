from tkinter import *
from forex_python.converter import CurrencyRates


def convert():
    currency1=c1.get()
    currency2=c2.get()
    rates = CurrencyRates()
    rate=rates.get_rate(currency1, currency2)
    text.config(text=rate)
    
 #This is for the GUI.
screen=Tk()
screen.title("Currency Converter")
screen.config(bg="lightblue")
Label(screen, text="From",bg="lightblue").grid(row=0, pady=5, padx=100)
c1=StringVar()
Entry(screen, textvariable=c1).grid(row=1) 
Label(screen, text="To",bg="lightblue").grid(row=2, pady=5, padx=100)
c2=StringVar()
Entry(screen, textvariable=c2).grid(row=3) 
Button(screen, text="convert", command=convert).grid(row=4, pady=5)
text=Label(screen, font="calibri 12", bg="lightblue", fg="green")
text.grid(row=5, pady=5)

screen.mainloop()
