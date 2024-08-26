"""
Wellington Pereia Luiz  - pt-br - utf-8 - 25-04-2024
26_08.py


receita_bruta = {'Janeiro': 1500,'Fevereiro':2600,'Março':1450,'Abril':18000,
                 'Maio':2000,'Junho':3150}
print(f'\n A receita bruta da empresa no semestre foi de: {receita_bruta} ')

print(f'\nO tipo de dados da variavel é: {type(receita_bruta)} ')



receita_bruta = {'Janeiro': 1500,'Fevereiro':2600,'Março':1450,'Abril':18000,
                 'Maio':2000,'Junho':3150}

for chave in receita_bruta: #Imprimindo somente as chaves
    print(f'O valor da chave do dicionario é: {chave}')

for chave in receita_bruta: #Imprimindo somente os valores das chaves
    print(f'O valo do rendimento bruto da chave do dicionario é: {receita_bruta[chave]}')
    

receita_bruta = {'Janeiro': 1500,'Fevereiro':2600,'Março':1450,'Abril':18000,
                 'Maio':2000,'Junho':3150}


for chave in receita_bruta: #Imrpimindo as chaves e seus valores
    print(f'Na chave: {chave} o rendimento bruto foi: R$ {receita_bruta[chave]}')

print(f'As chaves do dicionario sao: {receita_bruta.keys()}') #Imprimindo todas as chaves com keys()

for chave in receita_bruta.keys():
    print(f'A receita bruta de cada chave do dicionario é: {receita_bruta[chave]}')



for valor in receita_bruta.values():
    print(f'A receita bruta de cada chave dop dicionario é: {valor}')

for chave, valor in receita_bruta.items():
    print(f'A receita bruta da chave: {chave} é ={valor} - O tipo de dados retornado é: {type(receita_bruta.items())}')



#Interando sobre o dicionario com as funções sum(), mas(), min(), e len():
print(f'A soma dos valores que estão no dicionario é: {sum(receita_bruta.values())}')
print(f'O valor maximo que esta no dicionario é: {max(receita_bruta.values())}')
print(f'O valor minino que esta no dicionario é: {min(receita_bruta.values())}')
print(f'O numero de elementos (chave: valor) que estão no dicionario é: {len(receita_bruta)}')



#CONJUNTOS
#Criando um conjunto vazio - Primeira Forma:
conjunto = set()
print(f'\n Os dados do conjunto são: {conjunto}')
print(f'\n O conjunto tem: {len(conjunto)} elementos')
print(f'\n O tipo da variavel conjunto é: {type(conjunto)}')



conjunto = set({7,8,9,'CURSO','ADS','Algoritmos e Logica',8,9,10,11,'CURSOS'})
print(F'\nConjunto original: 7,8,9,CURSO,ADS,Algoritmos e Logica,8,9,10,11,CURSOS')
print(f'A impressão dos dados acima segue a logica de uma unica string')

print(f'\nDados do conjunto: {conjunto}')

print(f'\nTotal de elementos conjunto: {len(conjunto)}')

print(f'\nO tipo da variavel conjunto é do tipo: {type(conjunto)}')


#Convertendo uma String em conjunto - set()
curso = 'Curso ADS' 

print(f'\nDados da String: {curso}')

print(f'\nTipo de dados da String curso: {type(curso)}')

conjunto = set(curso)

print(f'\nDados do conjunto: {conjunto}')

print(f'\nTipo de dados do conjunto: {type(conjunto)}')

"""

#Convertendo uma lista em conjunto - set()
lista = [1,2,3,4,'Analise',4,3,2,1,False,'Analise',False]

print(f'\nDados da lista:{lista}')
print(f'\nTipo de dados da lista: {type(lista)}')

conjunto = set(lista)

print(f'\nDados do conjunto: {conjunto}')
print(f'\nTipo de dados do conjunto: {type(conjunto)}')
print(f'\nTotal de elementos conjunto: {len(conjunto)}')


