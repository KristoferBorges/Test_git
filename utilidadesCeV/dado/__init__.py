"""
Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie
uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados
para aceitar apenas valores que seja monetários.
"""


def leiaDinheiro(valor):
    valor = str(input('Digite um valor R$ '))
    if valor.isalpha() or valor == '':
        print('VALOR NÃO ACEITO')
    else:
        return float(valor)
