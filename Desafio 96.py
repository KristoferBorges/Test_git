"""Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno."""


def li():
    print('=' * 26)


def calcula_area(base, altura):
    area = base * altura
    print(f'A área tem [{base} x {altura}] = [{area}m²]')


li()
print('{:>20}'.format('Cálculo de ÁREA'))
li()
t_base = float(input("Digite a Base em [m]: "))
t_altura = float(input('Digite a altura em [m]: '))
calcula_area(t_base, t_altura)

