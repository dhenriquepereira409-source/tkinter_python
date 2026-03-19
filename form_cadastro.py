import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário")
janela.geometry("450x480")

def enviar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    escolaridade = combo_escolaridade.get()
    area = opc.get()

    if opc.get() == 1:
        area = "Técnico em Informática"
    elif opc.get() == 2:
        area = "Técnico em Enfermagem"
    elif opc.get() == 3:
        area = "Técnico em Segurança do Trabalho"
    elif opc.get() == 4:
        area = "Técnico em Gastronomia"

    msg = f"Nome: {nome}\n Idade: {idade}\n Escolaridade: {escolaridade}\n Area de Atuação:{area}"
    messagebox.showinfo("Dados Enviados", msg)

tk.Label(janela, text="Formulário de Cadastro", font=("Arial", 14,"bold")).grid(row=2, column=1, pady=15)

tk.Label(janela, text="Dados Pessoais", font=("Arial", 12,"bold")).grid(row=3, column=1, pady=20)

#entrada de texto
tk.Label(janela, text="Nome:", font=("Arial")).grid(row=4, column=0, pady=8)
entrada_nome= tk.Entry(janela, font=("Arial"))
entrada_nome.grid(row=4, column=1)

tk.Label(janela, text="Idade:", font=("Arial")).grid(row=5, column=0)
entrada_idade= tk.Entry(janela, font=("Arial"))
entrada_idade.grid(row=5, column=1)

tk.Label(janela, text="Dados Profissionais", font=("Arial", 12, "bold")).grid(row=6, column=1, pady=10)

#COMBOBOX
tk.Label(janela, text="Escolaridade:", font=("Arial", 12)).grid(row=7, column=0, pady=15)
combo_escolaridade = ttk.Combobox(janela, values=["Ensino Fundamental", "Ensino Médio", "Ensino Supeior"])
combo_escolaridade.grid(row=7, column=1)

#radiobutton
opc = tk.IntVar()
tk.Label(janela, text="Área de Atuação: ", font=("Arial")).grid(row=8,column=0)
tk.Radiobutton(janela, text="Técnico em Informática", font=("Arial"), value=1,variable=opc)\
    .grid(row=8,column=1)
tk.Radiobutton(janela, text="Técnico em Enfermagem",font=("Arial"), value=2,variable=opc)\
    .grid(row=9,column=1)
tk.Radiobutton(janela, text="Técnico em Segurança do Trabalho",font=("Arial"), value=3,variable=opc)\
    .grid(row=10,column=1)
tk.Radiobutton(janela, text="Técnico em Gastronomia",font=("Arial"), value=4,variable=opc)\
    .grid(row=11,column=1)

#BOTÃO
tk.Button(janela, text="Enviar", command=enviar).grid(row=12,column=1,pady=20)


janela.mainloop()