"""Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado."""

import random
import time
from operator import itemgetter

players = {"Kristofer": random.randint(1, 6),
           "Ramon": random.randint(1, 6),
           "Livia": random.randint(1, 6),
           "Fran": random.randint(1, 6)}

result = {}

print('JOGUEM OS DADOS!')
for n, v in players.items():
    time.sleep(0.4)
    print(f'{n} Jogou e tirou = {v}')

result = sorted(players.items(), key=itemgetter(1), reverse=True)

i = 1
print()
for n, v in result:
    print(f'{i}º Posição [{n} Número = {v}]')
    i += 1
