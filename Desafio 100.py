"""Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint

numeros = list()


def sorteia(lista):
    for n in range(1, 5 + 1):
        num = randint(0, 100)
        lista.append(num)
    print(f'Os números sorteados foram = {lista}')


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma = soma + n
    print(f'Os valores pares somados é = [{soma}]')


sorteia(numeros)
somaPar(numeros)
