"""
Wellington Pereia Luiz  - pt-br - utf-8 - 25-04-2024
19_08.py
"""

''' Exercício 1

import tkinter as tk
from tkinter import messagebox

# Função para capturar o nome
def capturar_nome():
    nome = entrada_nome.get()
    if nome:  # Verifica se o campo não está vazio
        if len(nomes) < 5:
            nomes.append(nome)  # Adiciona o nome à lista
            entrada_nome.delete(0, tk.END)  # Limpa o campo de entrada
            if len(nomes) == 5:  # Quando atingir 5 nomes
                exibir_nomes()  # Exibe os nomes
        else:
            messagebox.showinfo("Limite atingido", "Você já inseriu 5 nomes.")
    else:
        messagebox.showwarning("Campo vazio", "Por favor, insira um nome.")

# Função para exibir os nomes na interface
def exibir_nomes():
    for i, nome in enumerate(nomes):
        label_nome = tk.Label(janela, text=nome)
        label_nome.place(x=120, y=150 + i*20)  # Posiciona cada nome abaixo do anterior

# Criação da janela principal
janela = tk.Tk()
janela.title("Capturar Nomes")
janela.geometry("300x300")

# Lista para armazenar os nomes
nomes = []

# Rótulo e campo de entrada
label_instrucao = tk.Label(janela, text="Insira um nome:")
label_instrucao.place(x=20, y=20)

entrada_nome = tk.Entry(janela)
entrada_nome.place(x=120, y=20)

# Botão para capturar nome
botao_capturar = tk.Button(janela, text="Capturar Nome", command=capturar_nome)
botao_capturar.place(x=120, y=50)

# Inicia o loop principal da interface
janela.mainloop()

'''

'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para capturar o nome e armazenar na lista
def capturar_nome():
    nome = entrada_nome.get()
    if nome:  # Verifica se o campo não está vazio
        if len(nomes) < 5:
            nomes.append(nome)  # Adiciona o nome à lista
            entrada_nome.delete(0, tk.END)  # Limpa o campo de entrada
            if len(nomes) == 5:  # Quando atingir 5 nomes
                exibir_nomes_treeview()  # Exibe os nomes no Treeview
        else:
            messagebox.showinfo("Limite atingido", "Você já inseriu 5 nomes.")
    else:
        messagebox.showwarning("Campo vazio", "Por favor, insira um nome.")

# Função para exibir os nomes no Treeview
def exibir_nomes_treeview():
    for i, nome in enumerate(nomes):
        tree.insert('', 'end', text=str(i+1), values=(nome,))

# Criação da janela principal
janela = tk.Tk()
janela.title("Capturar Nomes")
janela.geometry("400x300")

# Lista para armazenar os nomes
nomes = []

# Rótulo e campo de entrada
label_instrucao = tk.Label(janela, text="Insira um nome:")
label_instrucao.place(x=20, y=20)

entrada_nome = tk.Entry(janela)
entrada_nome.place(x=120, y=20)

# Botão para capturar nome
botao_capturar = tk.Button(janela, text="Capturar Nome", command=capturar_nome)
botao_capturar.place(x=120, y=50)

# Criação do Treeview
tree = ttk.Treeview(janela, columns=('Nome',), show='headings')
tree.heading('Nome', text='Nome')
tree.column('Nome', anchor='center', width=150)

# Posicionamento do Treeview
tree.place(x=50, y=100)

# Inicia o loop principal da interface
janela.mainloop()

'''
