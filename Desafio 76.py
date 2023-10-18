listagem = ('Feijão', 17.60, 'Batata', 4.20, 'Frango', 36.30, 'Abacate', 9.20)

print('=' * 40)
print('{:.^40}'.format('Lista de Produtos'))
print('=' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

