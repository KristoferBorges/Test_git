"""Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""


dados = dict()
dados['nome'] = str(input('Nome do jogador: '))
qnt_partidas = int(input(f'Quantas partidas o jogador [{dados["nome"]}] Jogou: '))
gols_p = list()
total_gols = 0
for g in range(1, qnt_partidas + 1):
    gols_p.append(int(input(f'Na Partida [{g}] o Jogador [{dados["nome"]}] fez Quantos gols: ')))

total_gols = sum(gols_p)
dados['totaldegols'] = total_gols
dados['gols'] = gols_p[:]
print('=-' * 26)
print(dados)
print('=-' * 26)
for p, g in enumerate(dados['gols']):
    print(f' Na partida [{p + 1}] o jogador [{dados["nome"]}] fez [{g}] Gols!')
print(f'Ao todo o jogador [{dados["nome"]}] fez [{dados["totaldegols"]}]')
