import time
import sys

sum_p = 0
print('Escolha 6 números: ')
for c in range(1, 6+1):
    number = int(input('({}) Escolha um número: '.format(c)))
    if number % 2 == 0:
        sum_p = number + sum_p

print('Valores de números pares {}'.format(sum_p))
