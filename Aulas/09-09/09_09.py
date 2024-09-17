<<<<<<< HEAD
# Trabalhando com try, except e finally
"""EXEMPLO 1
try:  # tente fazer isso
    nota_1 = float(input('Digite a 1ª nota: '))
    nota_2 = float(input('Digite a 2ª nota: '))
    nota_3 = float(input('Digite a 3ª nota: '))
    nota_4 = float(input('Digite a 4ª nota: '))
    
    print()
    print(f'A soma das quatro notas é: {nota_1+nota_2+nota_3+nota_4}')
    print()
    print(f'A média das quatro notas é: {(nota_1+nota_2+nota_3+nota_4)/4}')
except ValueError:  # apresente a mensagem abaixo se ocorrer um erro
    print('Digite apenas números: ')
finally:
    print('Bloco finalizado')
"""

"""EXEMPLO 2
try:  # tente fazer isso
    nota_1 = float(input('Digite a 1ª nota: '))
    nota_2 = float(input('Digite a 2ª nota: '))
    nota_3 = float(input('Digite a 3ª nota: '))
    nota_4 = float(input('Digite a 4ª nota: '))
    
=======
"""
#Trabalhando com try, except e finall
try: # tente fazer isso
    nota_1 = float(input('Digite a 1° nota:'))
    nota_2 = float(input('Digite a 2° nota:'))
    nota_3 = float(input('Digite a 3° nota:'))
    nota_4 = float(input('Digite a 4° nota:'))
    print()
    print(f'A soma das quatro notas é:{nota_1+nota_2+nota_3+nota_4}')
    print()
    print(f'A media das quatro notas é:{(nota_1+nota_2+nota_3+nota_4)/4}')
except ValueError:
    print('Digite apenas numeros')
finally:
    print('Bloco finalizado')

    

#Trabalhando com try, except e finall
try: #tente fazer isso
    nota_1 = float(input('Digite a 1° nota:'))
    nota_2 = float(input('Digite a 2° nota:'))
    nota_3 = float(input('Digite a 3° nota:'))
    nota_4 = float(input('Digite a 4° nota:'))
>>>>>>> 717e4fe0d228027569f13740abc9247581446a22
    print()
    media = (nota_1+nota_2+nota_3+nota_4)/4
    print()

<<<<<<< HEAD
    print(f'A soma das quatro notas é: {nota_1+nota_2+nota_3+nota_4}')
    print()
#   print(f'A média das quatro notas é: {media}')
 
    if media >= 60:
        print(f'Aprovado com média {media}')
    elif media < 60 and media >= 40:
        print(f'Exame - media: {media}')
    elif media < 40 and media > 30:
        print(f'Só o conselho para ajudar - média: {media}')
    else:
        print(f'Retido na disciplina - média {media}')
    
except ValueError: # apresente a mensagem abaixo se ocorrer um erro
    print(f'Digite apenas números:')
finally:
    pass
"""

"""EXEMPLO 3
=======
    print(f'A soma das quatro notas é:{nota_1+nota_2+nota_3+nota_4}')
    print()
    #print(f'A media das quatro notas é:{media}')

    if media >= 60:
        print(f'Aprovado com media:{media}')
    elif media < 60 and media >= 40:
        print(f'Exame - media:{media}')
    elif media < 40 and media > 30:
        print(f'So o conselho para ajudar - media:{media}')
    else:
        print(f'Retido da disciplina - media:{media}')
    
except ValueError: #apresente a mensagem abaixo se ocorrer um erro
    print('Digite apenas numeros:')
finally:
    pass
        
"""
#Faça um script, onde o usuário digite seu nome completo em uma string e usando o for, imprima cada letra do nome.

>>>>>>> 717e4fe0d228027569f13740abc9247581446a22
nome = ""
try:
    nome = input('Digite seu nome: ')

<<<<<<< HEAD
    if nome.isalpha and len(str(nome))>=1:
        for letra in nome:
            print(f'A letra do nome digitado foi {letra}')
except ValueError:
    print(f'\nDigite apenas caracteres')

finally:
    pass
"""


"""EXEMPLO 4
try:
    disciplina = input('Digite o nome da discipllina: ')

    if not disciplina.isalpha():
        print('Digte apenas caractares')

    else:
        for indice, letra in enumerate(disciplina):
            if(indice % 2) != 0:
                print(f'{indice}:{letra}')

except Exception as e:
    print(f'Uma exceção ocorreu: {e}')

finally:
    pass
"""

"""EXEMPLO 5
try:
    nome_curso = input('Digite o nome do Curso disciplina: ')
    print()
    if nome_curso.isalpha and len(str(nome_curso)) > 0:

        for indice_letra in enumerate(nome_curso):

            if((indice_letra[1].upper())) in 'AEIOU':
                print(indice_letra[1].upper())
except ValueError:
    print('Digite apenas caracteres')
finally:
    pass
"""

"""EXEMPLO 6
try:
    cidade_nasceu = input('Digite o nome da cidade onde nasceu: ')
    print()
    if cidade_nasceu.isalpha():
        for letra in cidade_nasceu:
            if letra.upper() in 'BCDFGHJKLMNPQRSTVXWZÇ':
                print(letra.upper())
    else:
        print('Digite apenas caracteres')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

finally:
    pass
"""

"""EXEMPLO 7
import time

for tabela in range(32, 124):
    print(f'O código da tabela ASC é: {tabela} - que corresponde = {chr(tabela)}')
    time.sleep(0.0005)
"""

"""EXEMPLO 8
import time
nr = 0
for i in range(8):
    print(f' Indice: {i}')
    nr +=1
    time.sleep(0.0005)

print(f'\nO total de índices mostrados na tela é: {nr} \n')
"""

"""EXEMPLO 9
try:
    indice_inicial = int(input('Digite o índice inicial: '))
    indice_final = int(input('Digite o índice final...: '))
    print()
    if indice_inicial < 0:
      print(f'O índice inicial: {indice_inicial} não pode ser menor que 0 - programa encerrado.')
    elif indice_final <= indice_inicial:
       print(f'O índice inicial: {indice_inicial} não pode ser maior ou igual ao índice final: {indice_final} - programa encerrado.')
    else:
       for i in range(indice_inicial, indice_final):
          print(f'índice {i}')
    print(f'\nO total de índices mostrados na tela é: {indice_final - indice_inicial}\n')
except ValueError:
   print('\nDigite apenas números inteiros... \n')
"""

"""EXEMPLO 10
try:
    nr = 0
    indice_inicial = int(input('Digite o índice inicial: '))
    indice_final = int(input('Digite o índice final...'))
    print()

    # Critério H: O número índice inicial não pode ser menor que zero nem maior ou igual ao úmero do índice final

    if indice_inicial < 0 or indice_inicial >= indice_final:
        print(f'O índice inicial: {indice_inicial} não pode ser menor que zero ou maior ou igual ao índice final: {indice_final} - programa encerrado')
    else:
        numeros_ignorados = [] # uma lista para armazenar os números a serem ignorados
        # Critério J: Permitir que o usuário possa definir 3 números que deverão ser ignorados
        while len(numeros_ignorados) < 3: #peça ao usuário para inserir 3 números para ignorar
            numero_ignorado = int(input('Digite um número para ignorar:'))
            if numero_ignorado not in numeros_ignorados:
                numeros_ignorados.append(numero_ignorado)
            else:
                print('Esse número já foi escolhido para ser ignorado, escolha outro número.')

        for i in range(indice_inicial, indice_final, 5):
            if i not in numeros_ignorados: # só imprima o número se ele não estiver na lista de números ignorados
              print(f'índice: {i}')
              nr += 1

        # Critério I: Deve ser apresentado no mínimo 4 elementos na tela
        if nr < 4:
            print(f'Quantidade de índices incompatível com os critérios pedidos no script: pedidos = 4, intervalo tem apenas: {nr}')
        else:
            print(f'O total de índices mostrados na tela é: {nr}')

except ValueError:
    print('Digite apenas números inteiros...')
"""

"""EXEMPLO 11
num = 42

print(f'\nA variável num: {num} é do tipo:{type(num)}')

print(f'\nO endereço de memória da variável num é {id(num)}')

print(f'\nVariáveis globais do módulo: {globals()}\n')
"""

# Python reatribuição de variáveis:
"""EXEMPLO 12
num = 'Curso de ADS'

print(f'\nA variável num: {num} é do tipo: {type(num)}')

print(f'\nO endereço de memória da variável num é: {id(num)}')

print(f'\nVariáveis globais do módulo: {globals()} \n')
"""

"""EXEMPLO 13
if True:
    variavel_local = 10
    print(f'\nO valor da variavel_local é dentro do if é: {variavel_local} \n')

print(f'O valor da variável_local fora do bloco if é: {variavel_local}')


variavel_local += 50

for i in range(2):
    variavel_local += 30
    print(f'\nO valor da variavel_local dentro do for é: {variavel_local}')
    break

variavel_local += 5

while True:
    variavel_local += 5
    print(f'\nO valor da variavel_local dentro do while é: {variavel_local} \n')
    break

variavel_local += 5

print(f'O valor da variavel_local fora do bloco while é: {variavel_local}\n')
"""

# Imprimindo uma string com for em uma linha:
"""EXEMPLO 14
disciplina = 'Algoritmo e lógica de programação'
for nome in disciplina:
    print(nome, end='')
"""

# Imprimindo uma mesma string com for várias vezes
"""EXEMPLO 15
for numero in range(1, 9):
    print('ADS' * numero)
"""

"""EXEMPLO 16
def soma(valor_1, valor_2):
    print(valor_1 + valor_2)

soma(25, 100)
"""

"""EXEMPLO 17
def parImpar(numero):
    return numero % 2 == 0

def par_ou_impar(numero):
    if parImpar(numero) == True:
        return 'par'
    else:
        return 'impar'
    
print(par_ou_impar(123))
print(par_ou_impar(48))
"""

"""EXEMPLO 18
# função de pesquisa na lista e retorna valor na variável
def pesquisa(lista, valor_a_pesquisar):
    try:
        # Retorna o índice do valor_a_pesquisar se ele estiver na lista
        return lista.index(valor_a_pesquisar)
    except ValueError:
        # Retorna None se o valor_a_pesquisar não for encontrado na lista
        return None
    
# lista de exemplo
lista_1 = [51, 25, 2021, 2022, 'IFRO']

# Imprime o índice onde está o elemento
print(pesquisa(lista_1, 2022))
print(pesquisa(lista_1, 'IFRO'))

print('Imprimindo o argumento passado')

# Chama a função e imprime na tela o argumento passsado ao chamar a função
# caso ele exista na lista.

indice = pesquisa(lista_1, 51)
if indice is not None: # Se o índice existir (ou seja, não for None)
    print(lista_1[indice])
else:
    print("Elemento não encontrado na lista.")
"""

# função que imprime o cabeçalho de uma empresa
"""EXEMPLO 19
empresa = 'Dias e Dias Parados'
def imp_cabecalho():
    print(empresa)

# chamando a função
imp_cabecalho()
"""

# - função jogar moeda e verifica se vai dar cara ou coroa
"""EXEMPLO 20
from random import random

def joga_moeda():
    #gera um número pseudo randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return'Cara'
    else:
        return'Coroa'
print(joga_moeda())
"""

"""EXEMPLO 21
# – Recebendo parâmetros e argumentos.
def multiplica(num1, num2): # função com dois parametros
    return num1 * num2

def outra(num1, b, mensagem): # Função com três parâmetros
    return (num1 + b) * mensagem

print(multiplica(4, 5)) # dois argumentos

print(outra(2, 5, 'IFRO')) # três argumentos
"""

# função que retorna um o nome completo passado por parâmetro
"""EXEMPLO 22
def nome_completo(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'

print(nome_completo('Claudinei', 'de Oliveira'))
print(nome_completo(nome='Gertrudezi', sobrenome='de Gomes Pascoal'))
"""

# - Funções com parâmetro padrão
"""EXEMPLO 23
print('IFRO Campus Ariquemes')
"""

# - Funções com parâmetros obrigatórios
"""EXEMPLO 24
def quadrado(numero):
    return numero ** 2

print(quadrado(5))
"""

# função onde a passagem de parâmetro não seja obrigatória - Valor defaul
"""EXEMPLO 25
def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(4,3))

print(exponencial(2))
"""
=======
    if nome.isalpha and len(str(nome)) >= 1:
        for letra in nome:
            print(f'A letra do nome digitado  foi: {letra}')
except ValueError:
    print(f'\nDigite apenas caracteres')
finally:
    pass



>>>>>>> 717e4fe0d228027569f13740abc9247581446a22
