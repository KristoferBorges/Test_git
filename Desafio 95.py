"""Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador."""

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas o jogador [{jogador["nome"]}] Jogou: '))
    partidas.clear()
    for c in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols na partida [{c}]: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continua = str(input('Deseja continuar cadastrando? [S/N]')).upper()[0].strip()
        if continua in 'SN':
            break
        else:
            print('Apenas [S/N]\n')
    if continua == 'N':
        break
print('*=' * 35)
print('COD ', end='')
for i in jogador.keys():
    print(f'{i.upper():<18}', end='')
print()
print('--' * 35)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<18}', end='')
    print()
print('--' * 35)
while True:
    localizar = int(input('Veja os dados do jogador: (9999 para parar)'))
    if localizar == 9999:
        break
    if localizar >= len(time):
        print('Jogador não localizado!')
    else:
        print()
        print(f'Dados localizados {time[localizar]["nome"]}: ')
        for i, g in enumerate(time[localizar]['gols']):
            print(f'Na [PARTIDA{i + 1}] o jogador fez [{g}] Gols!')