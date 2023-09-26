import random

def sortNumberInLista():
    lista = list()

    for i in range(1, 10 + 1):
        number = random.randint(1, 30)
        if number not in lista:
            lista.append(number)

    return lista

lista = sortNumberInLista()

lista.sort()
print('Tente acertar o número da lista: ')

attempt = int(input('Digite um número: '))
if attempt in lista:
    print('\nVocê acertou!')
    print(f'Os números da lista são: {lista}')
else:
    print('\nVocê errou!')
    print(f'Os números da lista são: {lista}')