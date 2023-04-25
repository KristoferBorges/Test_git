"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passo. Seu programa tem que realizar três contagens através da função criada:  """

import time


def calcula_tamanho():
    texto = 'CONTAGEM PERSONALIZADA'
    tamanho = len(texto)
    texto_centralizado = texto.center(tamanho)
    print('-' + f'=' * len(texto) + '==-')
    print(f'  {texto_centralizado}')
    print('-' + f'=' * len(texto) + '==-')


def contador():
    # Contador
    print('=' * 21)
    print('      CONTADOR 1')
    print('=' * 21)
    for n in range(1, 10 + 1):
        time.sleep(0.2)
        print(n)
    print('FINISH')


def contadorInv():
    # Contador inverso
    print('=' * 21)
    print('      CONTADOR 2')
    print('=' * 21)
    for n in range(10, 0, -1):
        print(n)
        time.sleep(0.2)
    print('FINISH')


def contadorPersonalizado(start, end, jump):
    # ContadorPersonalizado
    print('=' * 26)
    print(f'Contagem de [{start}] até [{end}] de [{jump} em {jump}]')
    print('=' * 26)

    if end > start:
        for n in range(start, end + 1, jump):
            print(n)
            time.sleep(0.2)
        print('FINISH')
    elif end < start:
        for n in range(start, end - 1, jump):
            print(n)
            time.sleep(0.1)
        print('FINISH')


contador()
contadorInv()
calcula_tamanho()
inicio = int(input('Digite o INÍCIO: '))
fim = int(input('Digite o FIM: '))
pulo = int(input('Digite os PASSOS: '))
if pulo == 0 and fim > inicio:
    pulo = 1
elif pulo == 0 and fim < inicio:
    pulo = -1
contadorPersonalizado(inicio, fim, pulo)
