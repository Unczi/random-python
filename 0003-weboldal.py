from tkinter import *
import webbrowser
def kereses():
    webcim = b_mezo.get()
    webbrowser.open(webcim)
ablak = Tk()
ablak.title("Legjobb böngésző")
cimke = Label(ablak,text="Weboldal címe:")
cimke.grid(row=0,column=0)
b_mezo = Entry(ablak,width=35)
b_mezo.grid(row=0,column=1,padx=10,pady=10)
gomb = Button(ablak,text="Keresés",command=kereses)
gomb.grid(row=1, column=1)
ablak.mainloop()
