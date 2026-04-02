import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

DB_file = "estoque.db"

# --- FUNÇÕES DE BANCO DE DADOS ---
def iniciar_db():
    conn = sqlite3.connect(DB_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos(
            id TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    # Cria usuário admin se não existir (Simulação de segurança)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            usuario TEXT PRIMARY KEY,
            senha TEXT NOT NULL
        )
    ''')
    # Insere admin padrão se não existir (Senha: admin123)
    try:
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", ("admin", "admin123"))
    except sqlite3.IntegrityError:
        pass
    conn.commit()
    conn.close()

# --- JANELA DE LOGIN ---
class JanelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Login")
        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')

        frame_principal = ttk.Frame(self.root, padding="30 40")
        frame_principal.pack(fill="both", expand=True)

        ttk.Label(frame_principal, text="Login Controle de Estoque", font=("Arial", 14, "bold"))\
            .grid(row=0, column=0, columnspan=2, pady=(0, 25), sticky='ew')
        
        ttk.Label(frame_principal, text="USUÁRIO").grid(row=1, column=0, sticky='e', pady=8)
        self.usuario_var = tk.StringVar()
        ttk.Entry(frame_principal, textvariable=self.usuario_var, width=25).grid(row=1, column=1, pady=8, sticky='w')

        ttk.Label(frame_principal, text="SENHA").grid(row=2, column=0, sticky='e', pady=8)
        self.senha_var = tk.StringVar()
        self.entrada_senha = ttk.Entry(frame_principal, textvariable=self.senha_var, width=25, show="*")
        self.entrada_senha.grid(row=2, column=1, pady=8, sticky='w')
        self.entrada_senha.bind("<Return>", lambda e: self.verificar_login())
        self.entrada_senha.focus()

        btn_frame = ttk.Frame(frame_principal)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20, sticky='ew') # Ajustado row
        ttk.Button(btn_frame, text='ENTRAR', command=self.verificar_login).pack(side='left')
        ttk.Button(btn_frame, text='SAIR', command=self.root.destroy).pack(side='left', padx=10)

    def verificar_login(self):
        usuario = self.usuario_var.get().strip()
        senha = self.senha_var.get().strip()
        
        conn = sqlite3.connect(DB_file)
        cursor = conn.cursor()
        cursor.execute("SELECT senha FROM usuarios WHERE usuario=?", (usuario,))
        result = cursor.fetchone()
        conn.close()

        # Validação simples (Em produção, use hash de senha)
        if result and result[0] == senha:
            messagebox.showinfo("Bem Vindo", f"Login Realizado com sucesso!\n Olá, {usuario}")
            self.root.withdraw()  # Esconde o login em vez de destruir
            abrir_sistema_estoque(self.root) # Passa a mesma raiz
        else:
            messagebox.showerror("Erro de login", "Usuário ou senha Incorretos")
            self.senha_var.set("")
            self.entrada_senha.focus()

# --- SISTEMA DE ESTOQUE ---
class EstoqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Estoque")
        self.root.geometry("950x650")
        self.root.state('zoomed')
        
        # Configurar fechamento seguro
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.conn = sqlite3.connect(DB_file)
        self.criar_interfaces()

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 10))
        style.configure("Treeview", rowheight=26, font=('Arial', 10))

    def on_close(self):
        if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
            self.conn.close()
            self.root.destroy()

    def criar_interfaces(self):
        frame_botoes = ttk.Frame(self.root, padding="10")
        frame_botoes.pack(fill="x")

        botoes = [
            ("Novo Produto", self.novo_produto),
            ("Editar Produto", self.editar_produto),
            ("Excluir Produto", self.excluir_produto),
            ("Entrada", self.entrada_estoque),
            ("Saída", self.saida_estoque),
            ("Atualizar", self.atualizar_tabela),
            ("SAIR", self.on_close),
        ]
        for texto, cmd in botoes:
            ttk.Button(frame_botoes, text=texto, command=cmd).pack(side="left", padx=5)

        frame_tabela = ttk.Frame(self.root, padding="10")
        frame_tabela.pack(fill="both", expand=True)

        colunas = ("id", "nome", "quantidade", "preco")
        self.tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", selectmode="browse")

        self.tree.heading("id", text="Código")
        self.tree.heading("nome", text="Nome do Produto")
        self.tree.heading("quantidade", text="Quantidade")
        self.tree.heading("preco", text="Preço R$")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("nome", width=150, anchor="center")
        self.tree.column("quantidade", width=100, anchor="center")
        self.tree.column("preco", width=100, anchor="center")

        scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.status_var = tk.StringVar(value="Pronto")
        ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w")\
            .pack(side="bottom", fill="x", ipadx=5)

        self.atualizar_tabela()

    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, quantidade, preco FROM produtos ORDER BY id")
        for row in cursor.fetchall():
            # Garante que tudo seja string ou formato correto para a Treeview
            self.tree.insert("", "end", values=(row[0], row[1], row[2], f"{row[3]:.2f}"))
        
        cursor.execute("SELECT COUNT(*) FROM produtos")
        total = cursor.fetchone()[0]
        self.status_var.set(f"Total de Produtos: {total}  |  Base de Dados {DB_file}")

    def get_produto_selecionado(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("ATENÇÃO", "Selecione um produto na tabela")
            return None
        item_values = self.tree.item(sel[0])["values"]
        id_prod = item_values[0]
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT nome, quantidade, preco FROM produtos WHERE id=?", (id_prod,))
        row = cursor.fetchone()
        return (id_prod, {"nome": row[0], "quantidade": row[1], "preco": row[2]}) if row else None
    
    def novo_produto(self):
        janela_add = tk.Toplevel(self.root)
        janela_add.title("Adicionar Produto")
        janela_add.geometry("450x350")
        janela_add.transient(self.root)
        janela_add.grab_set()

        # Inputs
        inputs = {}
        campos = [("ID", "id"), ("Nome", "nome"), ("Quantidade", "qtd"), ("Preço UND", "preco")]
        for label, key in campos:
            ttk.Label(janela_add, text=f"{label}: ").pack(pady=(20 if key == 'id' else 5, 5))
            entry = ttk.Entry(janela_add, width=25)
            entry.pack()
            inputs[key] = entry

        def salvar():
            id_val = inputs['id'].get().strip().upper()
            nome = inputs['nome'].get().strip()
            try:
                qtd = int(inputs['qtd'].get())
                preco = float(inputs['preco'].get().replace(',', '.'))
            except ValueError:
                messagebox.showerror("ERRO", "Valores Inválidos! Quantidade deve ser inteiro, Preço número.")
                return

            if not id_val or not nome:
                messagebox.showwarning("Atenção", "Código e Nome são Obrigatórios")
                return

            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO produtos (id, nome, quantidade, preco) VALUES (?,?,?,?)",
                               (id_val, nome, qtd, preco))
                self.conn.commit()
                self.atualizar_tabela()
                messagebox.showinfo("Sucesso!", f"Produto {nome} cadastrado!")
                janela_add.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "Este ID já existe!")

        ttk.Button(janela_add, text="Salvar", command=salvar).pack(pady=25)

    def editar_produto(self):
        item = self.get_produto_selecionado()
        if not item: return
        id_prod, dados = item

        janela_edit = tk.Toplevel(self.root)
        janela_edit.title("Editar Produto")
        janela_edit.geometry("450x350")
        janela_edit.transient(self.root)
        janela_edit.grab_set()

        ttk.Label(janela_edit, text=f"ID: {id_prod}").pack(pady=10)

        entries = {}
        campos = [("Nome", "nome", dados["nome"]), ("Quantidade", "qtd", dados["quantidade"]), ("Preco R$", "preco", dados["preco"])]
        
        for label, key, valor in campos:
            ttk.Label(janela_edit, text=f"{label}: ").pack()
            entry = ttk.Entry(janela_edit, width=50)
            entry.insert(0, str(valor)) # Conversão explícita para string
            entry.pack(pady=5)
            entries[key] = entry

        def salvar():
            try:
                nome = entries['nome'].get().strip()
                qnt = int(entries['qtd'].get())
                preco = float(entries['preco'].get().replace(",", "."))
                cursor = self.conn.cursor()
                cursor.execute("UPDATE produtos SET nome=?, quantidade=?, preco=? WHERE id=?",
                               (nome, qnt, preco, id_prod))
                self.conn.commit()
                self.atualizar_tabela()
                janela_edit.destroy()
                messagebox.showinfo("Sucesso", "Produto Atualizado!")
            except Exception as e:
                messagebox.showerror("Erro", f"Verifique os valores. Detalhes: {e}")

        ttk.Button(janela_edit, text="Salvar Alterações", command=salvar).pack(pady=25)

    def excluir_produto(self):
        item = self.get_produto_selecionado()
        if not item: return
        id_prod, dados = item
        if messagebox.askyesno("Confirmação", f"Excluir {dados['nome']} ({id_prod})?"):
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id=?", (id_prod,))
            self.conn.commit()
            self.atualizar_tabela()
            messagebox.showinfo("Sucesso", "Produto Excluído.")

    def movimentar_estoque(self, tipo):
        item = self.get_produto_selecionado()
        if not item: return
        id_prod, dados = item
        titulo = "Entrada" if tipo == "entrada" else "Saída"
        qnt_str = simpledialog.askstring(titulo, f"Quantidade a {tipo} em {dados['nome']}", parent=self.root)
        
        if not qnt_str: return
        try:
            qtd = int(qnt_str)
            if qtd <= 0: raise ValueError
            cursor = self.conn.cursor()
            if tipo == "entrada":
                cursor.execute("UPDATE produtos SET quantidade = quantidade + ? WHERE id=?", (qtd, id_prod))
            else:
                cursor.execute('SELECT quantidade FROM produtos WHERE id=?', (id_prod,))
                atual = cursor.fetchone()[0]
                if qtd > atual:
                    messagebox.showerror("ERRO", f"Estoque Insuficiente! Disponível: {atual}")
                    return
                cursor.execute('UPDATE produtos SET quantidade = quantidade - ? WHERE id=?', (qtd, id_prod))
            self.conn.commit()
            self.atualizar_tabela()
            messagebox.showinfo("Sucesso!", f"Movimentação de {qtd} unidades realizada!")
        except ValueError:
            messagebox.showerror("Erro", "Informe um número Inteiro Positivo")

    def entrada_estoque(self): self.movimentar_estoque("entrada")
    def saida_estoque(self): self.movimentar_estoque("saida")

# --- CONTROLE PRINCIPAL ---
def abrir_sistema_estoque(root):
    # Reutiliza a mesma raiz (root) passada pelo login
    app = EstoqueApp(root)
    # Não chamamos mainloop aqui, pois o mainloop está rodando no __main__

if __name__ == "__main__":
    iniciar_db() # Garante que o DB e tabelas existem
    root = tk.Tk()
    app_login = JanelaLogin(root)
    root.mainloop()