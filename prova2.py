import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário")
janela.geometry("400x500")

def enviar():
    nome_exib = nome.get()
    sobrenome_exib = sobrenome.get()
    data_nasc_exib = data_nasc.get()
    cpf_exib = cpf.get()
    cep_exib = cep.get()
    estados_exib = estados.get()
    cidade_exib = cidade.get()

    sexo = opc.get()

    sexo_texto = "Masculino" if sexo == 1 else "Feminino"

    msg = f"Nome: {nome_exib}\n Sobrenome: {sobrenome_exib}\n Data de nascimento: {data_nasc_exib}\n CPF: {cpf_exib}\n CEP: {cep_exib}\n Sexo: {sexo_texto}\n Estado: {estados_exib}\n Cidade: {cidade_exib}"
    messagebox.showinfo("Dados Enviados", msg)

tk.Label(janela, text="Formulário: ", font=("Arial", 14,"bold")).grid(row=1, column=1, pady=6)

tk.Label(janela, text="Nome: ", font=("Arial")).grid(row=2, column=0, pady=6)
nome = tk.Entry(janela, font=("Arial"))
nome.grid(row=2, column=1)

tk.Label(janela, text="Sobrenome: ", font=("Arial")).grid(row=3, column=0, pady=6)
sobrenome = tk.Entry(janela, font=("Arial"))
sobrenome.grid(row=3, column=1)

tk.Label(janela, text="Data de Nascimento: ", font=("Arial")).grid(row=4, column=0, pady=6)
data_nasc = tk.Entry(janela, font=("Arial"))
data_nasc.grid(row=4, column=1)

tk.Label(janela, text="CPF: ", font=("Arial")).grid(row=5, column=0, pady=6)
cpf = tk.Entry(janela, font=("Arial"))
cpf.grid(row=5, column=1)

tk.Label(janela, text="CEP: ", font=("Arial")).grid(row=6, column=0, pady=6)
cep = tk.Entry(janela, font=("Arial"))
cep.grid(row=6, column=1)

#radiobutton
opc = tk.IntVar()
tk.Label(janela, text="Sexo:", font=("Arial")).grid(row=7,column=0)
tk.Radiobutton(janela, text="Masculino", font=("Arial"), value=1,variable=opc)\
    .grid(row=7,column=1)
tk.Radiobutton(janela, text="Feminino",font=("Arial"), value=2,variable=opc)\
    .grid(row=8,column=1)

#COMBOBOX
tk.Label(janela, text="Estado").grid(row=9, column=0)
estados = ttk.Combobox(janela, values=["AM", "MT", "MG", "SP", "RJ", "BA"])
estados.grid(row=9, column=1)

tk.Label(janela, text="Cidade: ", font=("Arial", 12,"bold")).grid(row=10, column=0, pady=6)
cidade = tk.Entry(janela, font=("Arial"))
cidade.grid(row=10, column=1)

#BOTÃO
tk.Button(janela, text="Enviar", command=enviar).grid(row=11,column=1,pady=20)

janela.mainloop()