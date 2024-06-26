from tkinter import *

janela = Tk()

janela.geometry("400x400")

label = Label(
    janela,
    text="Bem vindo ao curso de TKinter",
    font="Arial 14",
    relief="raised",
    background="green",
    foreground="white")

label.pack()

janela.mainloop()
