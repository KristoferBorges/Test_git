"""Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
em uma lista composta. No final, mostre um boletim contendo
a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
normal = '\033[m'

historico = list()

while True:
    nome = str(input(yellow + 'Nome do Aluno: ' + normal))
    nota1 = float(input(yellow + '[1º] Nota: ' + normal))
    nota2 = float(input(yellow + '[2º] Nota: ' + normal))
    average = (nota1 + nota2) / 2
    if average >= 6:
        resultado = 'APROVADO'
        historico.append([nome, [nota1, nota2], average, resultado])
    else:
        resultado = 'REPROVADO'
        historico.append([nome, [nota1, nota2], average, resultado])
    print('\n')
    cont = str(input(yellow + 'Deseja Continuar? [S/N]' + normal)).upper().strip()
    if cont != 'S':
        break

print("==" * 16)
print(green + f'{"Nº.":<4}{"Nome":<13}{"Media":<8}{"Resultado":9<}' + normal)
print('-' * 32)
for i, a in enumerate(historico):
    print(green + f'{i:<4}{a[0]:<13}{a[2]:<8.1f}{a[3]}' + normal)


while True:
    cont2 = str(input(yellow + '\n[?] Deseja mostrar as notas de algum aluno?    [S/N]' + normal)).upper().strip()
    if cont2 != 'S':
        print('\nProcesso Finalizado')
        break
    print(yellow + '\nInforme o Nº do ALUNO' + normal)
    descnota = int(input('--> '))
    if descnota < len(historico):
        print(green + f'Nome: {historico[descnota][0]} \nNotas: {historico[descnota][1]} \nResultado: '
                      f'{historico[descnota][3]}' + normal)
    else:
        print(red + 'ALUNO NÃO LOCALIZADO' + normal)
