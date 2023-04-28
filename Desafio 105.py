"""Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)"""

sala = dict()


def dados(total=0, maior_n=0, menor_n=0, media_n=0, situation=False):
    """

    :param total: Total de notas.
    :param maior_n: Maior valor das notas.
    :param menor_n: Menor valor das notas.
    :param media_n: Média das notas.
    :param situation: Indicação de qualidade.
    :return: Valores recebidos com as informações de cada variável.
    """
    global sala
    sala['TOTAL'] = total
    sala['MAIOR NOTA'] = maior_n
    sala['MENOR NOTA'] = menor_n
    sala['MEDIA DE NOTAS'] = media_n
    if situation:
        if media_n > 6.0:
            sala['SITUAÇÃO'] = 'BOA'
        elif media_n < 6.0:
            sala['SITUAÇÃO'] = 'RUIM'
        else:
            sala['SITUAÇÃO'] = 'A BAIXO DA MÉDIA'
    return print(sala)


notas = [5, 7, 6, 10, 0]
max_nota = max(notas)
min_nota = min(notas)
soma = 0
qnt = 0
for c in notas:
    soma = soma + c
    qnt = qnt + 1
result = (soma / qnt)
dados(qnt, max_nota, min_nota, result, True)
