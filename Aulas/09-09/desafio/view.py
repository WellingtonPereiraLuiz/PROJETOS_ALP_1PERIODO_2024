
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

def configurar_app(app):
    global mensagem_var

    app.title('Análise e Desenvolvimento de Sistemas')
    app.geometry('1024x600')
    app.configure(background='#F8F8FF')
    app.resizable(True, True)
    app.maxsize(width=1024, height=600)

    mensagem_var = StringVar()
    mensagem_label = Label(app, textvariable=mensagem_var, fg='red', font=('Arial',14,'bold'), bg='white')
    mensagem_label.place(x=100, y=265, width=700, height=20)

def criar_frame(app):
    frame = LabelFrame(app, text='Cadastro', borderwidth=1, relief='solid')
    frame.place(x=10, y=10, width=1000, height=200)
    return frame

def criar_labels(frame):
    lb_1 = Label(frame, text='Contatos: ', fg='red', font=('Arial', 14, 'italic', 'bold'))
    lb_1.place(x=15, y=10, width=70, height=20)
    lb_nome = Label(frame, text='Digite um nome: ', font=('Arial', 14))
    lb_nome.place(x=20, y=35, width=120, height=20)
    lb_sobrenome = Label(frame, text='Digite um sobrenome: ', font=('Arial', 14))
    lb_sobrenome.place(x=20, y=65, width=180, height=20)

def criar_entry(frame):
    global nome, sobrenome
    nome = Entry(frame, font=('Arial', 14))
    nome.place(x=200, y=35, width=400, height=20)
    sobrenome = Entry(frame, font=('Arial', 14))
    sobrenome.place(x=200, y=65, width=400, height=20)
    return nome,sobrenome

def criar_checkbutton(frame):
    global genero_var
    genero_var = StringVar()
    generos = ['Masculino', 'Feminino', 'Outro']
    y_pos = 95
    for gen in generos:
        Radiobutton(frame, text=gen, variable=genero_var, value=gen, font=('Arial', 14)).place(x=200, y=y_pos)
        y_pos += 30
    return genero_var


def criar_botao(app,capturar,mostrar_campo_pesquisa,salvar_edicao,excluir_registro):
    global btn_captura
    style = ttk.Style()
    style.configure('Green.TButton', font=('Arial', 14, 'bold'), background='#90EE90')
    style.configure('Blue.TButton', font=('Arial', 14, 'bold'), background='#ADD8E6')
    style.configure('Red.TButton', font=('Arial', 14, 'bold'), background='#FFB6C1')

    btn_captura = ttk.Button(app, text='Inserir dados', style='Green.TButton', command=capturar)
    btn_captura.place(x=20, y=220, width=155, height=40)

    btn_pesquisar = ttk.Button(app, text='Pesquisar dados', style='Blue.TButton', command=mostrar_campo_pesquisa)
    btn_pesquisar.place(x=185, y=220, width=155, height=40)
    
    btn_atualizar = ttk.Button(app, text='Atualizar dados', style='Green.TButton', command=salvar_edicao)
    btn_atualizar.place(x=350, y=220, width=155, height=40)

    btn_apagar = ttk.Button(app, text='Apagar Registro', style='Red.TButton', command=lambda: excluir_registro(btn_captura, mensagem_var))
    btn_apagar.place(x=350, y=220, width=155, height=40)

    btn_sair = ttk.Button(app, text='Sair', style='Red.TButton', command=app.quit)
    btn_sair.place(x=685, y=220, width=155, height=40)

def criar_campo_pesquisa(app,filtrar_dados):
    global campo_pesquisa, btn_fechar_pesquisa, lb_pesquisar
    lb_pesquisar = Label(app, text='Digite o nome a pesquisar', font=('Arial', 14), bg='white')
    lb_pesquisar.place(x=10, y=270, width=220, height=20)
    campo_pesquisa = Entry(app, font=('Arial', 14))
    campo_pesquisa.place(x=230, y=270, width=370, height=20)
    campo_pesquisa.bind('<KeyRelease>', filtrar_dados)

    btn_fechar_pesquisa = ttk.Button(app, text='Fechar pesquisa', style='Blue.TButton', command=fechar_pesquisa)
    btn_fechar_pesquisa.place(x=610, y=265, width=155, height=30)

def fechar_pesquisa(carregar_dados_arquivo):
    lb_pesquisar.destroy()
    campo_pesquisa.destroy()
    btn_fechar_pesquisa.destroy()
    for i in tree.get_children():
        tree.delete(i)
    for pessoa in carregar_dados_arquivo():
        tree.insert('', 'end', values=pessoa)

def criar_treeview(app,on_item_double_click):
    global tree
    colunas = ('nome', 'sobrenome', 'genero')
    tree= ttk.Treeview(app, columns=colunas, show='headings')
    tree.heading('nome', text='Nome')
    tree.heading('sobrenome', text='Sobrenome')
    tree.heading('genero', text='Gênero')
    tree.column('nome', minwidth=0, width=250)
    tree.column('sobrenome', minwidth=0, width=250)
    tree.column('genero', minwidth=0, width=100)
    tree.place(x=10, y=300, width=1000, height=290)
    tree.bind("<Double-1>", on_item_double_click)

    return tree


