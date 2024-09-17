"""
Wellington Pereia Luiz  - pt-br - utf-8 - 16-09-2024
16_09.py
"""
"""
#Função sem retorn de valor
def minha_funcao():
    print("Ola mundo!!!")
    print("Tudo bem pessoal!!!")

minha_funcao()

#Função com retorno
def quadrado_de_oito():
    return 8*8

retorno = quadrado_de_oito()
print(retorno)
print(f'O quadrado de 8 + 1 é: {quadrado_de_oito()+1}')


# Estrutura condicional para diferentes return’s em uma mesma função.
def funcao_nova():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(funcao_nova())


# Retornando múltiplos valores a partir de uma função
def outra_funcao():
    return 2, 3, 4, 5

n1, n2, n3, n4 = outra_funcao()
print(n1, n2, n3, n4)

# Função com um parâmetro de entrada
def quadrado(numero):
    return numero **2

print(quadrado(11))
print(quadrado(9))
print(quadrado(15))

retorno = quadrado(5)
print(retorno)


# Função com dois parâmetros de entrada
def soma(a, b):
    return a + b

print(soma(2,5))



# Função com três parâmetros de entrada
def outra(n, b, mensagem):
    return (n + b) * mensagem

print(outra(2, 5, 'Python'))


# Nomeando parâmetros nas funções
def nome_completo(nome, sobrenome):
    return f'Seu nome é: {nome} {sobrenome}'

print(nome_completo(sobrenome='Pereira Luiz', nome='Wellington'))
#- Os parâmetros dentro da função precisam estar na ordem que deseja apresentar na tela -

# - Nomeando argumentos nas funções - KeyWord Arguments
def nome_completo(nome, sobrenome):
    return f'Seu nome é: {nome} {sobrenome}'

print(nome_completo(sobrenome='Pereira Luiz', nome='Wellington')) 
#- Nesse caso a ordem dos argumentos não importa -


# Funções com parâmetros opcionais(Não precisam necessariamente de um parâmetro. Um exemplo 
#desse tipo de função é a função print().)
print()
print('\n')
print('Disciplina estrutura de dados')
instituto = 'IFRO - Campus Ariquemes'
print(f'\nAnalise de desenvolvimento de sistemas - {instituto}')


# Funções com parâmetros padrão – default
# Função que utiliza parâmetro/argumentos default.
def eleva_expoente(potencia, n=4):
    return n ** potencia

print(eleva_expoente(8))


# Função que recebe um parâmetro/argumentos default na sua definição, porém, os argumentos são alterados na chamada da função.
def eleva_expoente(potencia = 2, n=4):
    return n ** potencia

print(eleva_expoente(4,4))


# Injetando funcionalidades dentro de outras funções
def mostra_dados(nome='Wellington', instrutor=True):
    if nome == 'Wellington' and instrutor:
        return f'Bem vindo instrutor {nome}'
    elif nome == 'Germano':
        return 'Eu pensei que voce era o instrutor'
    return f'Ola {nome}'

print(mostra_dados())
print(mostra_dados(instrutor = False))
print(mostra_dados('Geraldo'))
print(mostra_dados('Germano'))
print(mostra_dados(nome='Germano'))
print(mostra_dados(nome='genoveva'))


# Passando funções como parâmetros
def soma(n1, n2):
    return n1 + n2

def funcao_como_parametro(n1, n2, funcao = soma):
    return funcao(n1, n2)

def subtracao(n1, n2):
    return n1 - n2

print(funcao_como_parametro(2, 3))
print(funcao_como_parametro(2, 2, subtracao))


# Funções com parâmetros/argumentos obrigatórios.São funções onde o número de argumentos deverá ser igual ao número de parâmetros.
def somar(a, b):
    return a + b

print(somar(2, 49))



# Função com variável global – para o módulo
disciplina = 'Algoritmos e logica de programacao'
print(disciplina)
print(type(disciplina))
print(id(disciplina))
print('\n')

def dizer():
    disciplina = 'Python'
    print(disciplina)
    print(type(disciplina))
    print(id(disciplina))
    return f'{disciplina} é uma linguagen de programacao poderosa'

print(dizer())


# Função com variável local
def dizer_3():
    aluno = 'Joaquim'
    return f'ola {aluno}'

print(dizer_3)

print(aluno)# essa variavel funciona apenas dentro da funcao "dizer_3", pois ela foi criada dentro dessa funcao e devido a isso ela é local

# Função com variável global e local
resultado = 0 #variavel global
def incrementa():
    resultado = resultado + 1 #variavel resultado local nao foi inicializada
    return resultado

print(incrementa())


# Definindo variável global dentro de uma função
resultado = 0 #variavel global

def incrementa():
    global resultado # informando ao Python que vamos utilizar a variavel global
    resultado = resultado + 1 
    return resultado

print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())


# - Funções definidas dentro de outras funções 
# escopo de variável especial - nonloca
def principal():
    contador = 0

    def secundaria():
        nonlocal contador # informa ao Python que a variavel esta na funcao anterior
        contador = contador + 1
        return contador
    return secundaria()

print(principal())
print(principal())
print(principal())

# Funções dentro de Funções:
def epar(x):
    return x % 2 == 0


def par_ou_impar(x):
    if epar(x):
        return "par"
    else:
        return"impar"
    
print(par_ou_impar(8))
print(par_ou_impar(15))


# Função verifica se um determinado valor está contido numa lista: 
def pesquisa(lista, valor):
    for i, x in enumerate(lista):
        if x == valor:
            return x
        return None
    
lista = [15, 25, 30, 35]
print(pesquisa(lista, 25))
print(pesquisa(lista, 41))


# Doctrings documentando partes importantes do código:
print(help(print))
#- Informações sobre o funcionamento da função print()

# Doctrings documentando partes importantes do código:
def diz_ola():
"""
   #funcao que diz Ola mundo!!! 
"""
    return'Ola mundo'

print(diz_ola())

print(help(diz_ola))



# Doctrings documentando partes importantes do código – outra forma. 
print(diz_ola._doc_)


# Doctrings documentando partes importantes do código – usando a propriedade dunder (duplo underline
def eleva_a_potencia(n, potencia = 2):
    """
   # Funcao que retorna por padrao a potencia informada
   # - parametro_1 = n que desejamos gerar o exponencial
   # - parametro_2 = potencia queremos gerar o exponencial
   # - return: retorna o exponencial de n por potencia
""" 

    return n**potencia

print(eleva_a_potencia.__doc__)
# help(eleva_a_potencia)
# Achei esse metodo mais rapido



# Empacotamento de argumentos: *args
def soma_numeros(*args):
    return sum(args)

print(soma_numeros())
print(soma_numeros(1))
print(soma_numeros(1, 2))
print(soma_numeros(1, 2, 3))
print(soma_numeros(1, 2, 3, 4))

# Empacotamento de argumentos: *args
def verifica(*args):
    if 'IFRO' in args and 'Instituto' in args:
        return 'Bem vindo ao IFRO aluno(a)!'
    return 'Desculpe! Não encontrei seu nome na lista de alunos(as)'

print(verifica())
print(verifica(1, True,'Instituto','IFRO' ))
print(verifica(1, 'Instituto', 3.145))


# Desempacotamento de argumentos de uma lista: *args
def soma_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_numeros(*numeros))


# Empacotamento e desempacotamento de parâmetros: **kargs
def animais_preferidos(**animais):
    for pessoa,animal in animais.items():
        print(f'O animal preferido de {pessoa.title()} é {animal.title()}')

animais_preferidos(carlos='cachorro', eunice='gato', everton='cabrito', carla='coelho')


# Empacotamento e desempacotamento de parâmetros: **kargs
def boas_vindas(**academicos):
    if 'ADS' in academicos and academicos['ADS'] == 'Estrutura_dados':
        return f'Seja bem vindo ao mundo Pythonico academico(a) de {academicos['ADS']}'
    elif 'ADS' in academicos:
        return f'{academicos["ADS"]}'
    return 'Acredito que voce nao faça parte de nosso curso'

print(boas_vindas())
print(boas_vindas(ADS='Estrutura_dados'))
print(boas_vindas(ADS='Ola!!'))


# - Empacotamento e desempacotamento de parâmetros: **kargs
def cores(**kargs):
    for pessoa, cor in kargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores(genova='lilas', gertruzes='ocre', gnomica='magenta', gerôncio='roxo')

cores()
cores(gerimundo='marrom')

# Empacotamento e desempacotamento de parâmetros: **kargs
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(18, 'Lais')
minha_funcao(8, 'Crislâine', 8, 10, 6, solteiro=True)
minha_funcao(9, 'Carla', 3, 9, 4, typescript = False, python = True)


# Desempacotando ** kargs
def nomes(**kwargs):
    return f'{kwargs['nome']} {kwargs['sobrenome']}'

nomes_1 = {'nome':'Gerimunda','sobrenome':'Gnomica'}
print(nomes(**nomes_1))


# Desempacotando ** kargs
def calcula(a, b, c):
    print(a + b + c)

lista = [9, 8, 7]
tupla = (9, 8, 7)
conjunto = {9, 8, 7}
dicionario = dict(a=9, b=8, c=7)

calcula(*lista)
calcula(*tupla)
calcula(*conjunto)
calcula(*dicionario)
"""

