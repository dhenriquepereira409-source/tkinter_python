import tkinter as tk

#CRIAÇÃO DE JANELA
janela_main = tk.Tk()

janela_main.title("Minha Janela")
janela_main.configure(background="#84D0FF")
janela_main.minsize(200,200)
#janela_main.maxsize(500,500)
janela_main.geometry("300x300")

#OBJETOS EM JANELA
#ETIQUETA
tk.Label(janela_main,
         text="Hello World",
         bg ="#84D0FF",
         font=("Biome", 17,"bold")
         ).pack()

tk.Label(janela_main,
         text="Douglas Henrique",
         bg ="#84D0FF",
         font=("Arial", 12)
         ).pack()
#IMAGENS
imagem = tk.PhotoImage(file="unnamed.png")
imagem = imagem.subsample(6,4)
tk.Label(janela_main, image=imagem) .pack()

janela_main.mainloop()