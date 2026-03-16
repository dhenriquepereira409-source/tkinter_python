import tkinter as tk

#CRIAÇÃO DE JANELA
janela_main = tk.Tk()

janela_main.title("Minha Janela")
janela_main.configure(background="#BCFFB6")
janela_main.minsize(200,200)
#janela_main.maxsize(500,500)
janela_main.geometry("300x300")

#OBJETOS EM JANELA
#ETIQUETA
tk.Label(janela_main,
         text="Gato",
         bg ="#BCFFB6",
         font=("Biome", 18,"bold")
         ).pack()

#IMAGENS
imagem = tk.PhotoImage(file="gato.png")
imagem = imagem.subsample(1,1)
tk.Label(janela_main, image=imagem) .pack()

tk.Label(janela_main,
         text="Um gato em Itálico",
         bg ="#BCFFB6",
         font=("Arial", 14)
         ).pack()

janela_main.mainloop()