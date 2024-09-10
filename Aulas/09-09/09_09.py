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
    print()
    media = (nota_1+nota_2+nota_3+nota_4)/4
    print()

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

nome = ""
try:
    nome = input('Digite seu nome: ')

    if nome.isalpha and len(str(nome)) >= 1:
        for letra in nome:
            print(f'A letra do nome digitado  foi: {letra}')
except ValueError:
    print(f'\nDigite apenas caracteres')
finally:
    pass



