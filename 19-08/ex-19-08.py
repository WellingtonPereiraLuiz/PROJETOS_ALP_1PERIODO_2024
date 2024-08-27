""" ===================== EXERCÍCIO 1 =====================
from tkinter import *

nomes = []

def capturar():
    nomeText = nome.get()
    nomes.append(nomeText)

    nome.delete(0, END)
    
    if len(nomes) == 5:
        texto = ''
        for i in nomes:
            texto += i + '\n'
            Ib_3['text'] = texto
        nomes.clear()
                
    
app = Tk()
app.title('Análise e Desenvolvimento de Sistemas')
app.geometry('1360x680')
app.configure(background='#F8F8FF')
app.resizable(True, True)
app.minsize(width=1360, height=670)
app.maxsize(width=1360, height=670)

frame = LabelFrame(app, text="Cadastro", borderwidth=1, relief='solid')
frame.place(x=10, y=10, width=1340, height=340)

Ib_1 = Label(frame, text='Contatos:', fg='red', font=("Arial", 14, "bold italic"))
Ib_1.place(x=15, y=5, width=100, height=20)

Ib_2 = Label(frame, text='Digite um nome:', font=("Arial", 14))
Ib_2.place(x=0, y=30, width=200, height=25)

nome = Entry(frame, font=('Arial', 14))
nome.place(x=180, y=35, width=400, height=20)
nome.focus_set()

Ib_3 = Label(app, text='', font=("Arial", 14), background='#F8F8FF')
Ib_3.place(x=135, y=370, width=400, height=200)

btn_captura = Button(app, text='Capturar nome', font=("Arial", 14, "bold"), command=capturar)
btn_captura.place(x=490, y=300, width=180, height=40)

app.mainloop()
"""

# ===================== EXERCÍCIO 2 =====================
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Criando janela principal

nomes = []

def capturar():
    nomeText = nome.get()
    nomes.append(nomeText)

    nome.delete(0, END)
    
    if len(nomes) == 5:
        tree.delete(*tree.get_children())
        for i in range(5):
            tree.insert(parent='', index='end', iid=[i], values=(nomes[i]))
            
        nomes.clear()


    # Inserindo dados na treeview
    #tree.insert(parent='', index='end', iid=0, values=(texto))
    #tree.insert(parent='', index='end', iid=1, text='2', values=("Bruno"))
    #tree.insert(parent='', index='end', iid=2, values=("Carlos"))


root = tk.Tk()

root.title('Análise e Desenvolvimento de Sistemas')
root.geometry('1360x680')
root.configure(background='#F8F8FF')
root.resizable(True, True)
root.minsize(width=1360, height=670)
root.maxsize(width=1360, height=670)

frame = LabelFrame(root, text="Cadastro", borderwidth=1, relief='solid')
frame.place(x=10, y=10, width=1340, height=340)

Ib_1 = Label(frame, text='Contatos:', fg='red', font=("Arial", 14, "bold italic"))
Ib_1.place(x=15, y=5, width=100, height=20)

Ib_2 = Label(frame, text='Digite um nome:', font=("Arial", 14))
Ib_2.place(x=0, y=30, width=200, height=25)

nome = Entry(frame, font=('Arial', 14))
nome.place(x=180, y=35, width=400, height=20)
nome.focus_set()

Ib_3 = Label(root, text='', font=("Arial", 14), background='#F8F8FF')
Ib_3.place(x=135, y=370, width=400, height=200)

btn_captura = Button(root, text='Capturar nome', font=("Arial", 14, "bold"), command=capturar)
btn_captura.place(x=490, y=300, width=180, height=40)

# Criação do Widget
tree = ttk.Treeview(root)

# Definindo as colunas
tree['columns'] = ('Nome')

tree.column("#0", width=0, stretch=tk.NO)
tree.column("Nome", anchor=tk.W, width=120)

# Definindo os cabeçalhos
tree.heading("#0", text="", anchor=tk.W)
tree.heading("Nome", text="Nome", anchor=tk.W)

# Posicionando o widget na janela
tree.pack(pady=20)

tree.place(x=900, y=50, width=150, height=200)

# Executando o loop principal da aplicação.
root.mainloop()


"""

# ========= EXEMPLOS DE CÓDIGOS DO MATERIAL =========

EXEMPLO 1
import tkinter as tk
from tkinter import ttk

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de Treeview")

# Criação do Widget Treeview
tree = ttk.Treeview(root)

# Definição das colunas
tree['columns'] = ('Nome', 'Idade', 'Profissão')

#Formatação das colunas
tree.column("#0", width=0, minwidth=25)
tree.column("Nome", anchor=tk.W, width=120)
tree.column("Idade", anchor=tk.CENTER, width=80)
tree.column("Profissão", anchor=tk.W, width=120)

# Definição dos cabeçalhos
tree.heading("#0", text="", anchor=tk.W)
tree.heading("Nome", text="Nome", anchor=tk.W)
tree.heading("Idade", text="Idade", anchor=tk.CENTER)
tree.heading("Profissão", text="Profissão", anchor=tk.W)

# Adicionando dados
tree.insert(parent='', index='end', iid=0, text='1', values=('Ana', 30, 'Engenheira'))
tree.insert(parent='', index='end', iid=1, text='2', values=('Bruno', 25, 'Programador'))
tree.insert(parent='', index='end', iid=2, text='3', values=('Carlos', 35, 'Designer'))

tree.pack(pady=20)

# Executa o loop principal da aplicação
root.mainloop()


# Criando uma tupla vazia:
EXEMPLO 2
tupla = ()

print(f"\nA tupla tem: {len(tupla)} elementos")

print(f"\nOs elementos da tupla são: {tupla}")

print(f"\nA variável tupla é do tipo: {type(tupla)}\n")


# Criando e Populando uma tupla
EXEMPLO 3
tupla = ('a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f"\nA tupla tem: {len(tupla)} elementos")
print(f"\nOs elementos da tupla são: {tupla}")
print(f"\nA variável tupla é do tipo: {type(tupla)}\n")

# Criando e Populando uma tupla a partir da função range()
EXEMPLO 4
tupla = tuple(range(11))

print(f"\nA tupla tem: {len(tupla)} elementos")
print(f"\nOs elementos da tupla são: {tupla}")
print(f"\nA variável 'tupla' é do tipo: {type(tupla)}")


#  Deletando uma tupla inteiras e todos os seus elementos:
 EXEMPLO 5
tupla = ('a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6, 7, 8, 9)

del tupla

print(f"A tupla tem: {len(tupla)} elementos")
print(f"Os elementos da tupla são: {tupla}")
print(f"A variável 'tupla' é do tipo: {type(tupla)}")


# Inserindo elementos em uma tupla:
 EXEMPLO 6
tupla = ('a', 'b', 'c', 'd', 'f', 'g', 1, 2, 3, 4, 5, 6, 7, 8, 9)

tupla = tupla + ('h', 'i', 'j', 10, 11, 12)

print(f'\nA tupla tem: {len(tupla)} elementos')

print(f'\nOs elementos da tupla são: {tupla}')

print(f'\nA variável tupla é do tipo: {type(tupla)} \n')


#Fatiamento de tupla - Transformando uma tupla em string / int...
 EXEMPLO 7
tupla = ("Algoritmos", 'e', "Lógica de Programação", 2023, 4.3, False)

print(f'\nOs elementos da tupla são: {tupla}')

print(f'\nOs elementos da tupla na posição 0 são: {tupla[0]}')

print(f'\nOs elementos da tupla na posição 1 são: {tupla[1]}')

print(f'\nOs elementos da tupla na posição 2 são: {tupla[2]}')

print(f'\nOs elementos da tupla na posição 3 são: {tupla[3]}')

valor = tupla[4]
print(f'\nOs elementos da tupla na posição 4 são: {valor}')
print(f'\nO Tipo de elementos da tupla na posição 4 são: {type(valor)}\n')

print(f'\nOs elementos da tupla na posição 5 são: {tupla[5]} \n')

# Desempacotamento de tuplas
 EXEMPLO 8
tupla = ("Algoritmos", 'e', "Lógica de Programação", 2023, 4.3, False)

dados_0, dados_1, dados_2, dados_3, dados_4, dados_5 = tupla

print(f'\nO elemento de dados_0 capturado da tupla é: {dados_0}')

print(f'\nO elemento de dados_1 capturado da tupla é: {dados_1}')

print(f'\nO elemento de dados_2 capturado da tupla é: {dados_2}')

print(f'\nO elemento de dados_3 capturado da tupla é: {dados_3}')

print(f'\nO elemento de dados_4 capturado da tupla é: {dados_4}')

print(f'\nO elemento de dados_5 capturado da tupla é: {dados_5}')

print(f'\nO tipo de elemento de dados_5 capturado da tupla é: {type(dados_5)}\n')


# Lendo quantos elementos tem a tupla
EXEMPLO 9
tupla = ("Algoritmos", 'e', "Lógica de Programação", 2023, '1° semestre', 4.3, False)

print(f"\nA tupla tem: {len(tupla)} elementos")

print(f"\nOs elementos da tupla são: {tupla} elementos")


# Operações com tuplas: soma, máximo, minimo 
 EXEMPLO 10
tupla = (8, 15, 7, 10, 12.5, 0.5, 25, 99, 1080.99, -298)

print(f"\nOs elementos da tupla são: {tupla} \n")

print(f"\nOs elementos da tupla são: {sum(tupla)}")

print(f"\nOs elementos da tupla são: {max(tupla)}")

print(f"\nOs elementos da tupla são: {min(tupla)}")


# Concatenando tuplas
EXEMPLO 11
tupla_1 = ('Gertrudez', 'Genoveva', 'Gerimunda', 'Gastronildo', 5, 6, 7)

tupla_2 = (11, 12, 13, 'Marília', 'Marcelo', 'Matias')

print(f'\nOs elementos da tupla_1 são: {tupla_1}')

print(f'\nOs elementos da tupla_2 são: {tupla_2}')

print(f'\nOs elementos concatenados das tupla_1 e 2 são: {tupla_1 + tupla_2}')


# Verificando se um elemento está contido na tupla:
EXEMPLO 12
tupla = ('Gertrudez', 'Genoveva', 'Gerimunda', 'Gastronildo', 5, 6, 7)

print(f'\nOs elementos da tupla são: {tupla}')

print(f'\nVerificando se o elemento "b" está na tupla: {"b" in tupla} \n')


# Iterando sobre tupla:
EXEMPLO 13
tupla = (11, 12, 13, 'Marília', 'Marcelo', 'Matias')

print(f'\nOs elementos da tupla são: {tupla} \n')

for elementos in tupla:
    print(elementos)


# Iterando sobre tupla com for(), enumerate() - gerando índice:
EXEMPLO 14
tupla = ('Algoritmos', 'e', 'Lógica de Programação', 2023, '1º semestre')

print(f'\nOs elementos da tupla são: {tupla} \n')

for indice, valor in enumerate(tupla):
    print('Indice:', indice, 'Elemento da tupla:', valor)


# Iterando sobre tupla - gerando índice para os elementos - while:
EXEMPLO 15
tupla = ('Algoritmos', 'e', 'Lógica de Programação', 2023, '1º semestre')

print(f'\nOs elementos da tupla são: {tupla} \n')

total = len(tupla)
contador = 0

while contador < total:
    print(f'Indice: {contador + 1}, Elemento da tupla: {tupla[contador]}')
    contador += 1


# Iterando sobre tupla - Contando elementos específicos de uma tupla:
EXEMPLO 16
tupla = ('a', 4, 5, 6, 'c', 'd', 'c', 'a', 'a', 'b', 1, 2, 3, 'a', 'A', 'a')

print(f'\nOs elementos da tupla são: {tupla}')

print(f'\nA tupla contém {tupla.count("a")} elementos = a \n')


# Iterando sobre tupla - Contando elementos específicos de uma tupla:
EXEMPLO 17
tupla = ('Instituto Federal de Rondônia - Campus Ariquemes')

print(f'\nOs elementos da tupla são: {tupla}')

print(f'\nA tupla contém {tupla.count("e")} elementos = e \n')


# Acessando os elementos de uma tupla pelo seu índice:
EXEMPLO 18
tupla = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho')

print(f"\nOs elementos da tupla são: {tupla}")

print(f'\nApresentando o elemento que está no índice "4" da tupla = {tupla[4]}')


EXEMPLO 19
# Verificando em qual índice um elemento está na tupla:
tupla = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')

print(f"\nOs elemetnos da tupla são: {tupla}")

print(f'\nO elemento Quinta da tupla está no índice = {tupla.index("Quinta")} \n')


# Aplicando slice em uma tupla => tupla(início: fim: passo)
EXEMPLO 20
tupla = ('Algoritmos', 'e', 'Lógica de Programação', 2023, '1º semestre',)

print(f'\nElementos da tupla: {tupla}')

print(f'\nQuantidade de elementos na tupla: {len(tupla)}')

print(f'\nElementos a partir da posição 0 da tupla {tupla[0:]}')

print(f'\nElementos a partir da posição 0 até a posição 3 da tupla {tupla[:3]}')

print(f'\nElementos a partir da posição 30 até a final tupla {tupla[3:]}')

print(f'\nTodos os elementos da tupla em passo 2 {tupla[::2]}')

print(f'\nTodos os elementos da tupla em passo 4 {tupla[::4]} \n')


# Copiando Tuplas:
EXEMPLO 21
tupla = ('Algoritmos', 'e', 'Lógica de Programação')

print(f'\nElementos da tupla: {tupla}')

tupla_2 = tupla
print(f'\nOs elementos da tupla 2 copiados da tupla são: {tupla_2} \n')


# Criando tuplas a partir de listas - função tuple():
EXEMPLO 22
lista = ['Campus', 'Ariquemes', 2023, True, 532.15]

print(f'\nLista original: {lista}')
print(type(lista))

tupla = tuple(lista)

print(f'\nTupla gerada a partir da lista = {tupla}')
print(type(tupla), '\n')


# Alterando uma lista que está dentro de uma tupla:
EXEMPLO 23
tupla = ('a', 'b', 12, ['Campus', 'Ariquemes', 2023, True, 532.15, 15])

print(f'\nElementos da tupla: {tupla}')

print(f'\nA quantidade de elementos da tupla é: {len(tupla)} \n')

print('Tecle <ENTER>')

print('\nInserindo um elemento na lista que está na tupla')

tupla[3].append('Curso de ADS')

print(f'\nTupla modificada: {tupla}\n')

print(input('Tecle enter para continuar<ENTER>'))

tupla[3][4] = False

print(f'\nTupla com valor False alterando a posição 4 {tupla} \n')

print(input('Tecle <ENTER>'))

tupla[3].insert(1,'IFRO')
print(f'\nTupla com o novo elemento inserido no índice 1 da lista: {tupla}\n')

print(input('Tecl<ENTER>'))
tupla[3].pop()
print(f'\nTupla após retirado o último elemento da lista: {tupla} \n')

print(input('tecle <ENTER>'))
tupla[3].pop(3)
print(f'\nTupla após retirado o elemento do índice 3 da lista: ', tupla)


# Desempacotamento de tuplas com listas
EXEMPLO 24
a, b, c, d = ('IFRO', 'Ariquemes', [1, 2], 2011)

print(f'\nElemento a da tupla: {a}')
print(type(a))

print(f'\nElemento b da tupla: {b}')
print(type(b))

print(f'\nElemento c da tupla: {c}')
print(type(c))

print(f'\nElemento d da tupla: {d}')
print(type(d))


# Usando * (asterisco) para desempacotar vários elementos dentro de listas em tuplas:
EXEMPLO 25
print(f'\nIniciando com a fórmula *a, b, c= (IFRO, Ariquemes, 1, 2, 2011)')

*a, b, c = ('IFRO', 'Ariquemes', 1, 2, 2011)

print(f'\nA recebeu todos os elementos da lista, menos o último que foi para c e o penúltimo que foi para b. a = {a}')

print(f'\nO penúltimo elemento da lista armazenado em b é = {b}')

print(f'\nO último elemento da lista armazenado em c é = {c} \n')

print(input('Tecle <Enter>'))

print(f'\nMudando a fórmula para a, *b, c= (IFRO, Ariquemes, 1, 2, 2011)')

a, *b, c = ('IFRO', 'Ariquemes', 1, 2, 2011)

print(f'\nPrimeiro elemento da lista armazenado em a é = {a}')

print(f'\nb recebeu todos os elementos da lista, menos o primeiro que foi para a e o último que foi para c. b = {b}')

print(f'\nO último elemento da lista armazenado em c é = {c} \n')

print(input('Tecle <ENTER>'))

print(f'\nMudando a fórmula para a, b, *c= (IFRO, Ariquemes, 1, 2, 2011)')

a, b, *c = (1, 2, 3, 4, 5)

print(f'\nPrimeiro elemento da lista armazenado em a é = {a}')

print(f'\nSegundo elemento da lista armazenado em b é = {b}')

print(f'\nc recebeu todos os elementos da lista, menos o primeiro que foi para a e o segundo que foi para b. c = {c} \n')
"""
