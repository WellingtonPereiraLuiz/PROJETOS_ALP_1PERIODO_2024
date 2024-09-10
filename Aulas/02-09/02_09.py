"""
from collections import Counter

lista = ['Márcia','Márcia','Alice','Antonio','Antonio','Pedro','Pedro']

print(f'\nResultado : {Counter(lista)}')

print(f'\nO tipo do resultado é: {type(Counter(lista))}')

lista = [1,1,1,2,2,2,3,3,4,4,4,5,3,45,45,66,42,36,105.19,105.19]

print(f'\nResultado : {Counter(lista)}')

print(f'\nO tipo do resultado é: {type(Counter(lista))}')




frase = ['IFRO Campus Ariquemes']

print(f'\nResultado : {Counter(frase)}')

print(f'\nO tipo do resultado é: {type(Counter(frase))}')



dicionario = {'disciplina':'Algoritmos e lógica de programação'}

print(f'\nDicionario original: {dicionario}')

print(f'\nAcessando a chave disciplina do dicionario: {dicionario["disciplina"]}')

print(f'\nAcessando a chave curso do dicionario: {dicionario["curso"]}')


from collections import defaultdict

dicionario = defaultdict(lambda:'Nome')

print(f'\nO valor do dicionario é: {dicionario}')

dicionario['disciplina'] = 'Algoritmos e lógica de programação'

print(f'\nO dicionario agora possui o elemento: {dicionario}')

print(f'\nAcessando a chave disciplina do dicionario: {dicionario['disciplina']}')

print(f'\nAcessando a chave curso do dicionario: {dicionario["curso"]}')


nome_1 =  {'Gustavo':28,'Andre':33,'João':15,'Alice':9,'Laís':5}

nome_2 = {'Andre':33,'João':15,'Gustavo':28,'Laís':5,'Alice':9}

print(f'\nOs dicionarios nome_1 e nome_2 são iguais? {nome_1 == nome_2}\n')


from collections import OrderedDict

nome_1 = OrderedDict({'Gustavo':28,'Andre':33,'João':15,'Alice':9,'Laís':5})

print(f'\nO dicionario nome_1 possui os elementos: {nome_1}')

print(f'\nO tipo dos dados do dicionario nome_1 é: {type(nome_1)}')

nome_2 = OrderedDict({'Andre':33,'João':15,'Gustavo':28,'Laís':5,'Alice':9})

print(f'\nO dicionario nome_2 possui os elementos: {nome_2}')

print(f'\nO tipo dos dados do dicionario nome_2 é: {type(nome_2)}')

print(f'\nOs dicionarios nome_1 e nome_2 são iguais e estão na mesma ordem? {nome_1 == nome_2}\n')


from collections import OrderedDict

nome = OrderedDict({'Gustavo':28,'Andre':33,'João':15,'Alice':9,'Laís':5})

print(f'\nO dicionario original é:{nome}')

nome.move_to_end('Andre')

print(f'\nO dicionario foi modificado: {nome}\n')


from collections import OrderedDict

nome = OrderedDict({'Gustavo':28,'Andre':33,'João':15,'Alice':9,'Laís':5})

print(f'\nO dicionario original é: {nome}')

nome.move_to_end('Laís',last=False)

print(f'\nO dicionario foi modificado:{nome}\n')



# Tuplas namedtuple - forma_1 de definir
from collections import namedtuple

animal_1 = namedtuple('animal','tipo nome raca idade')

# Tuplas namedtuple - Forma_2 de definir
from collections import namedtuple

animal_2 = namedtuple('animal','tipo, nome, raca, idade')

# Tuplas namedtuple - Forma_3 de definir
from collections import namedtuple

animal_3 = namedtuple('animal',['tipo','nome','raca','idade'])

cachorros = animal_3(tipo='cachorro',nome='Hatiro', raca='hasa apso',idade=2)

gatos = animal_3(tipo='gatos',nome='Ravena', raca='Vira latas',idade=1)

print(f'\nCachorro cadastrado: {cachorros}')

print(f'\nOs dados do cachorro foram armazenados no formato: {type(cachorros)}')

print(f'\nGato cadastrado: {gatos}')

print(f'\nOs dados do gato foram armazenados no formato: {type(gatos)}\n')


print(f'\nTipo: {cachorros[0]}')
print(f'Nome: {cachorros[1]}')
print(f'Raça: {cachorros[2]}')
print(f'Idade: {cachorros[3]}\n')

print(f'Tipo: {gatos[0]}')
print(f'Nome: {gatos[1]}')
print(f'Raça: {gatos[2]}')
print(f'Idade: {gatos[3]}\n')

from collections import deque

deq = deque()

deq.append('Arquemes')
deq.append('Curso de ADS')
deq.appendleft('Campus')
deq.appendleft('IFRO')
print(f'\nOs dados aramazenados no deque são: {deq}')
print(f'\nOs dados do deque foram armazenados no formato: {type(deq)}\n')



print(f'\nOs dados armazenados =no deque são: {deq}')

print(deq.popleft())

print(f'\nOs dados armazenados no deque apos o popleft() são: {deq}')

"""

# CRUD (Create, Reader, Update, Delete) - Python / Tkinter e arquivo
# JSON (JavaScript Object Notation)

"""
Wellington Pereira Luiz - UTF8 - pt-br - 02-09-2024
CRUD (Create, Reader, Update, Delete - com arquivos JSON - JavaScript Object Notation)
"""


#Funções - Modo interativo


#funções Tkinter



# Funções para editar ou excluir registros
        
#Finalmente a porcaria das configs iniciais do Tkinter (desculpe professsor :v)

