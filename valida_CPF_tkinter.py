#!/usr/bin/env python

from tkinter import *
from valida_CPF import cpf_valido

def processar():
    if cpf_valido(cpf.get()):
        resultado.set("CPF Válido!")
    else:
        resultado.set("CPF Inválido!")

def limpar():
    cpf.set('')
    resultado.set('')

app = Tk()
app.title('Valida CPF')
app.geometry('250x150')

Label(app, text='CPF: ').pack()
cpf = StringVar()
Entry(app, textvariable=cpf).pack()

Label(app, text='Resultado: ').pack()
resultado = StringVar()
Entry(app, textvariable=resultado).pack()

Button(app, text='Calcular', command=processar).pack()
Button(app, text='Limpar', command=limpar).pack()

app.mainloop()

