"""Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
import random
from time import sleep


def maiorNumero(lista):
    tamanho = len(lista)
    if tamanho > 0:
        maior = max(lista)
        menor = min(lista)
    else:
        maior = 0
        menor = 0
        tamanho = 0
    print(f'Foram recebidos ao todo [{tamanho}] números!\nO maior número obtido foi [{maior}]\n'
          f'O menor número obtido foi [{menor}]')


def maior_numero(* num):
    listnumber = list()
    print('=' * 26)
    for v in num:
        listnumber.append(v)
        sleep(0.5)
        print(v, end=' ')
    if len(num) > 0:
        maior = max(listnumber)
        menor = min(listnumber)
        tamanho = len(listnumber)
    else:
        tamanho = 0
        maior = 0
        menor = 0
    print(f'Foram recebidos ao todo [{tamanho}] Números!')
    print(f'O maior número é [{maior}]')
    print(f'O menor número é [{menor}]')
    print('=' * 26)


print('=' * 26)
print('     LISTA DE NÚMEROS')
print('=' * 26)
numeros = list()
print('[1] - Números escolhidos pelo usuário!')
print('[2] - Números escolhidos pela máquina!')
print('[3] - Números enviados por parâmetro!')
escolha = int(input('Escolha um valor para prosseguir!\n--> '))
if escolha == 1:
    print('OBS -> [9999 = STOP]')
    while True:
        number = int(input('Digite um número para lista: '))
        if number == 9999:
            print('FIM')
            break
        else:
            numeros.append(number)
    maiorNumero(numeros)
elif escolha == 2:
    i = 0
    qnt = int(input('Quantos números deseja sortear: '))
    while i < qnt:
        number = random.randint(0, 100)
        print(number)
        numeros.append(number)
        i = i + 1
    print('FIM')
    maiorNumero(numeros)
elif escolha == 3:
    maior_numero(3, 4, 6, 8, 9, 10)
    maior_numero(3, 6, 9, 8, 100, 141,)
    maior_numero(9, 10, 70, 6)
    maior_numero(0, 31, 48, 41, 75)
    maior_numero()
