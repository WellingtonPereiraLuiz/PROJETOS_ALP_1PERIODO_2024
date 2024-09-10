import tkinter as Tk
import regex as re
import os
import json
from tkinter import messagebox
import view
import model

def valida_campo(campo, tipo_campo):
    if not campo:
        messagebox.showwarning('Aviso', f'{tipo_campo} invalido')
        return False
    if len(campo) > 50:
        messagebox.showwarning('Aviso', f'{tipo_campo} muito longo. Deve ter no maximo 50 caracteres')
        return False
    
    pattern = r'^[\p{L}\s]{1,50}$'
    if not re.match(pattern, campo):
        messagebox.showwarning('Aviso', f'{tipo_campo} invalido. Não use numeros ou caracteres especiais')
        return False
    
    preposicoes = ['da','de','do','das','dos']
    campo = ' '.join([parte.capitalize() if parte not in preposicoes else parte for parte in re.sub(r'\s+', ' ', campo).split()])
    return campo

def grava_dados_arquivo(pessoa):
    arquivo_json = "cadastro.json"
    dados = []
    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)

        dados.append(pessoa) 
        with open(arquivo_json, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

def carregar_dados_arquivo():
    arquivo_json =  "cadastro.json"
    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, 'r') as arquivo:
            return [(linha['nome'], linha['sobrenome'], linha['genero']) for linha in json.load(arquivo)]
    return[]

def on_item_double_click(editar_registro):
    editar_registro()
    model.btn_captura['state'] = tk.DISABLED
    model.mensagem_var.set('Clique em <<ATUALIZAR DADOS>> ou <<APAGAR REGISTRO>> para excluir')

if __name__ == '__main__':
    app = Tk()
    view.configurar_app(app) 
    frame = view.criar_frame(app)
    view.criar_labels(frame)
    nome, sobrenome = view.criar_entry(frame)
    genero_var = view.criar_checkbutton(frame)
    view.criar_botao(app)
    tree = view.criar_treeview()
    for pessoa in carregar_dados_arquivo():
        tree.insert('', 'end', values=pessoa)
    app.mainloop()

