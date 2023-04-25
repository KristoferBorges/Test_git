"""Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.         """


def calcula_tamanho(texto):
    tamanho = len(texto)
    texto_centralizado = texto.center(tamanho)
    print('-' + f'=' * len(texto) + '==-')
    print(f'  {texto_centralizado}')
    print('-' + f'=' * len(texto) + '==-')


while True:
    string = str(input('Digite uma palavra [* = stop]\n--> '))
    if string == '*':
        break
    calcula_tamanho(string)
