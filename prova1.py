import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário")
janela.geometry("500x300")

def enviar():

    msg = f"Usuários logados com sucesso!"
    messagebox.showinfo("Dados Enviados", msg)

#ETIQUETA
tk.Label(janela, text="Formulário: ", font=("Arial", 14,"bold")).grid(row=2, column=1, pady=6)

tk.Label(janela, text="Usuário: ", font=("Arial", 12,"bold")).grid(row=4, column=0, pady=6)
usuario = tk.Entry(janela, font=("Arial"))
usuario.grid(row=4, column=1)

tk.Label(janela, text="Senha: ", font=("Arial", 12,"bold")).grid(row=5, column=0)
senha = tk.Entry(janela, font=("Arial"))
senha.grid(row=5, column=1)

#BOTÃO
tk.Button(janela, text="Enviar", command=enviar).grid(row=12,column=1,pady=20)

#IMAGEM
imagem = tk.PhotoImage(file="imagem.png")
imagem = imagem.subsample(5,5)
tk.Label(janela, image=imagem).grid(row=4, column=6, padx=30)

janela.mainloop()