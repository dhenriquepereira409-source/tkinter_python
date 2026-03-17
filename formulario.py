import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário")

#entrada de texto
Label_entrada = ttk.Label(janela, text="Nome")
Label_entrada.pack()
entrada = tk.Entry(janela)
entrada.pack()

#checkbox
checkbox = tk.IntVar()
check = tk.Checkbutton(janela, text="Aceito os termos", variable=checkbox)
check.pack()

#opções
opcao = tk.IntVar()
opc1 = tk.Radiobutton(janela, text="Masculino", variable=opcao, value=1)
opc2 = tk.Radiobutton(janela, text="Feminino", variable=opcao, value=2)
opc3 = tk.Radiobutton(janela, text="Outro", variable=opcao, value=3)
opc1.pack()
opc2.pack()
opc3.pack()

#listbox
lista = tk.Listbox(janela)
lista.insert(1, "Python")
lista.insert(2, "JAVA")
lista.insert(3, "PHP")
lista.insert(4, "JAVASCRIPT")
lista.pack()

#combobox
combo = ttk.Combobox(janela, values=["MG", "RJ", "RN", "SP"])
combo.set("Selecione o Estado: ")
combo.pack()

#botao
def clicar():
    messagebox.showwarning("Aviso", "Botão Acionado!")

btn = ttk.Button(janela, text="Mostrar Mensagem", command=clicar)
btn.pack()

janela.mainloop()