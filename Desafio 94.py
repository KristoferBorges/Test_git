"""Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram
cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média"""

dados = dict()
dadoscopy = dict()
pessoas = list()
qnt_pessoas = 0
qnt_pessoas_m = 0
media_idade = 0
v_idades = 0
mulheres = list()

while True:
    dados['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo [M/F] ')).upper().strip()
    if sexo not in 'MF':
        print('SOMENTE [M/F]!\n')
    if sexo == 'F':
        mulheres.append(dados['nome'])
        qnt_pessoas_m = qnt_pessoas_m + 1
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F] ')).upper().strip()
        if sexo not in 'MF':
            print('SOMENTE [M/F]!\n')
        else:
            dados['sexo'] = sexo
            if dados['sexo'] == 'F':
                mulheres.append(dados['nome'])
                qnt_pessoas_m = qnt_pessoas_m + 1
    dados['idade'] = int(input('Idade: '))
    v_idades = v_idades + dados['idade']
    pessoas.append(dados.copy())
    dadoscopy = dados.copy()
    dados.clear()
    qnt_pessoas = qnt_pessoas + 1
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break

media_idade = v_idades / qnt_pessoas
print('-=' * 30)
print(pessoas)
print('-=' * 30)
print('')
print(f'Foram cadastradas ao todo [{qnt_pessoas} Pessoas]')
print(f'A média da idade é [{media_idade:.2f} anos]')
if len(mulheres) > 0:
    print(f'Temos em registros [{qnt_pessoas_m} Mulheres], seus nomes são\n [{mulheres}]')
else:
    print('Não temos mulheres em nossos registros!')

print('\nAcima do peso médio temos as seguintes pessoas')
for p in pessoas:
    if p['idade'] > media_idade:
        for k, v in p.items():
            print(f'{k.upper()} = {v}')
