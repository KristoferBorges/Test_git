"""
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar
os números como um valor monetário formatado.
"""

from modulos_k import moeda


def processos(number):
    dobrado = moeda.dobro(number)
    metade = moeda.metade(number)
    aumentado = moeda.aumentar(number)
    diminuido = moeda.diminuir(number)
    print()
    print(f' [!] - Valor digitado [{moeda.moeda(number)}]')
    print(f' [!] - Dobro = {moeda.moeda(dobrado)}')
    print(f' [!] - Metade = {moeda.moeda(metade)}')
    print(f' [!] - Aumentado = {moeda.moeda(aumentado)}')
    print(f' [!] - Diminuido = {moeda.moeda(diminuido)}')


numero = float(input(' [?] - DIGITE UM VALOR E VEJA SEU:\n -> Dobro\n -> Metade\n -> + 10%\n -> - 10%\n [?] - R$ '))
processos(numero)
