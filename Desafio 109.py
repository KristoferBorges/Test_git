"""
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""

from modulos_k import moeda

dinheiro = 'R$ '


def processos(number, formatacao=True):
    global dinheiro
    dobrado = moeda.dobro(number)
    metade = moeda.metade(number)
    aumentado = moeda.aumentar(number)
    diminuido = moeda.diminuir(number)

    if formatacao:
        dobrado = f'{dinheiro}' + f'{dobrado:,.2f}'
        metade = f'{dinheiro}' + f'{metade:,.2f}'
        aumentado = f'{dinheiro}' + f'{aumentado:,.2f}'
        diminuido = f'{dinheiro}' + f'{diminuido:,.2f}'
        number = f'{dinheiro}' + f'{number:,.2f}'

        dobrado = dobrado.replace('.', ',')
        metade = metade.replace('.', ',')
        aumentado = aumentado.replace('.', ',')
        diminuido = diminuido.replace('.', ',')
        number = number.replace('.', ',')

    print()
    print(f' [!] - Valor digitado [{number:,.2f}]')
    print(f' [!] - Dobro = {dobrado:,.2f}')
    print(f' [!] - Metade = {metade:,.2f}')
    print(f' [!] - Aumentado = {aumentado:,.2f}')
    print(f' [!] - Diminuido = {diminuido:,.2f}')


numero = float(input(f' [?] - DIGITE UM VALOR E VEJA SEU:\n -> Dobro\n -> Metade\n -> + 10%\n -> - 10%\n [?] - '
                     f'{dinheiro} '))
processos(numero)
