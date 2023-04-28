"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

limit = 1
numbers = [[], []]
number = 0
while limit <= 7:
    number = int(input(f'[{limit}º] - Digite um número: '))
    if number % 2 == 0:
        numbers[0].append(number)
        limit = limit + 1
    else:
        numbers[1].append(number)
        limit = limit + 1

numbers[0].sort()
numbers[1].sort()
print('-=' * 30)
print(f'Números pares: {numbers[0]}')
print(f'Númeors Ímpares: {numbers[1]}')
