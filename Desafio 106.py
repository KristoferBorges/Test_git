"""Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores."""
import sys
from time import sleep

red = '\033[31m'
green = '\033[32m'
yellow = '\033[1;33m'
blue = '\033[34m'
blueBack = '\033[44m'
normal = '\033[m'
redBack = '\033[41m'
greenBack = '\033[42m'
yellowBack = '\033[43m'


def support(quest):
    if quest not in 'fim':
        sleep(0.4)
        print()
        print(green + '/' * 76 + normal)
        print(yellow)
        help(quest)
        print(normal)
        print(green + '/' * 76 + normal)
        print()
    else:
        print(red + 'CLOSED PROGRAM' + normal)
        sys.exit()
    return


while True:
    # Main Program
    print(blue + '=' * 31)
    print('{:>23}'.format('|SUPPORT SYSTEM|'))
    print('=' * 31)
    print()
    help_r = str(input('[!] - INFORME O COMANDO PARA RECEBER AJUDA!\n--> ')).strip().lower()
    support(help_r)
