while True:
    try:
        a = int(input('Digite sua idade:'))
        if a == 0:
            break
    except ValueError:
        print('Seu burro é para digitar numeros inteiros')