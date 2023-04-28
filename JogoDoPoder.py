# import pdb
from pygame import mixer
import random
from time import sleep

# Sons / Musicas
mixer.init()
selecionar = mixer.Sound(r'music\escolha12.wav')
lose = mixer.Sound(r'music\lose.wav')
win = mixer.Sound(r'music\winwin.wav')
boss = mixer.Sound(r'music\infernal2.wav')
# bonus = mixer.Sound(r'C:\Users\krist\Desktop\Estudos\CursoEmVideo\Python\music\bonus.wav')
critico = mixer.Sound(r'music\critico.wav')

mixer.music.load(r'C:\Users\krist\Desktop\Estudos\CursoEmVideo\Python\music\digital.mp3')
mixer.music.play(-1)


# Processo para elevação de poder / nível após certo nível //
def aumento_de_poder():
    global user_level, lv_monster, power_monster, lv_choice
    if user_level > 70 and power_usuario > 20000:
        lv_choice = random.randint(3, 6)
        lv_monster = lv_monster + lv_choice
        power_monster = power_monster * lv_choice


def critico_infernal():
    global power_usuario, point
    if random.randint(1, 5) == 1:
        critico.play()
        print(red + '   INFERNAL USOU SUA ULTMATE E INFRIGIU 5000 DE DANO' + normal)
        print(red + '   -200 Pontos' + normal)
        power_usuario = power_usuario - 4000
        point = point - 200
        sleep(3)


def if_monsters():
    global power_monster
    if card_monster == 'Gigante' or card_monster == 'Monstro do Lago':
        power_monster = power_monster + monster_power_lv4
    elif card_monster == 'Fada' or card_monster == 'Spectro' or card_monster == 'Guerreiro Sombrio' or \
            card_monster == 'Clérigo Corrompido':
        power_monster = power_monster + monster_power_lv3
    elif card_monster == 'Bandido' or card_monster == 'Orc' or card_monster == 'Mago' or card_monster == \
            'Fantasma' or card_monster == 'Arcano' or card_monster == 'Ogro' or card_monster == 'Escorpião' or \
            card_monster == 'Cobra Selvagem' or card_monster == 'Lobo' or card_monster == 'Crocodilo':
        power_monster = power_monster + monster_power_lv2
    elif card_monster == 'Goblin' or card_monster == 'Rato' or card_monster == 'Esqueleto' or card_monster == \
            'Slime' or card_monster == 'Aranha' or card_monster == 'Zumbi' or card_monster == 'Duente':
        power_monster = power_monster + monster_power_lv1


# Cores
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
ciano = '\033[36m'
normal = '\033[m'

# Variáveis importantes!
resultado = ''
escolha = ''
skipBoss = 0
choiceBonus = 0
escolha_usar_item = 0
soma_nivel = 0
aposta = 0
multiplicador = 0.00
lv_monster_print = 0
lv_choice = 0
# pontos
point = 0
pointx = random.randint(1, 10)

# Contador de Batalhas
cont = 0


# Tela inicial
print('\n\n\n\n\n\n\n')
print(yellow + '    -x-x-x-x-|  Bem-vindo(a) |-x-x-x-x-')
print('    -x-x-x-x-|      Ao       |-x-x-x-x-')
print('    -x-x-x-x-| JOGO DO PODER |-x-x-x-x-')
print('\n\n')
print('    Deseja entrar na Dungeon do Boss?')
print(green + '                 Sim' + yellow + ' / ' + red + 'Não              ' + normal)
iniciar_jogo = str(input('    --> ')).upper().strip()
if iniciar_jogo == 'SIM' or iniciar_jogo == 'S':
    # Music
    selecionar.play()
    # Itens e BUFFS dentro do game
    print(ciano + '    -x-x-x-x-| Itens EXTRA |-x-x-x-x-\n')
    print('   Escolha| Descrição| Quantidade')
    print('     [1] - Skip de Boss (1)')
    print('     [2] - CHANCE DE GANHAR PODER EXTRA (2)' + normal)
    item_escolhido = int(input('     ---> '))
    selecionar.play()

    if item_escolhido == 1:
        skipBoss = 1
        print(green + '    Você Escolheu (SKIP DE BOSS)!' + normal)
        print('\n\n')
    elif item_escolhido == 2:
        choiceBonus = 2
        print(green + '    Você Escolheu (BONUS DE PODER)!' + normal)
        print('\n\n')
    else:
        print(red + '    Nenhum item escolhido!' + normal)
        print('\n\n')

    # Inserção de Dinheiro
    print('\n')
    print(yellow + '    MAX - R$ 100,00' + normal)
    print(green + '    Qual valor deseja apostar?')
    aposta = float(input('    R$' + normal))
    selecionar.play()
    print('\n')

# Função de vitória/derrota/empate
    def result():
        global power_monster, power_usuario, user_level, lv_monster, resultado, point, pointx, card_monster, escolha, \
            soma_nivel, valorTotal, aposta, multiplicador
        if power_usuario > power_monster:
            user_level = user_level + 1
            power_usuario = power_usuario + 413
            power_monster = 0
            print(green + '  -x-x-x-x- Usuário Win -x-x-x-x-' + normal)
            print('\n')
            resultado = 'win'
            if resultado == 'win':
                point = point + 10
                multiplicador = multiplicador + 0.01
                card_monster = random.choice(monsters)
                lv_monster = random.randint(1, 4)
        elif power_monster > power_usuario:
            # Redução de poder por batalha / Monstro Win
            if card_monster == 'Infernal':
                point = point - 10
            else:
                point = point - random.randint(3, 10)
            power_usuario = power_usuario - 250
            power_monster = power_monster - 450
            soma_nivel = soma_nivel + 1
            if soma_nivel == 2:
                lv_monster = lv_monster + 1
                soma_nivel = 0

            print(red + '  -x-x-x-x- Monstro Win -x-x-x-x-' + normal)
            print('\n')
            resultado = 'lose'
        elif power_usuario == power_monster:
            print('  -x-x-x-x- Empate -x-x-x-x-')
            print('\n')
            resultado = 'tied'
            power_monster = 0
            card_monster = random.choice(monsters)
            lv_monster = random.randint(1, 4)
            # Redução de poder por batalha / Empate
            power_usuario = power_usuario - 100
            power_monster = power_monster - 500


    # Monstros
    monsters = ['Goblin', 'Rato', 'Esqueleto', 'Slime', 'Aranha', 'Zumbi', 'Duende', 'Bandido', 'Orc', 'Mago',
                'Fantasma',
                'Clérigo Corrompido', 'Gigante', 'Monstro do Lago',
                'Arcano', 'Fada', 'Spectro', 'Guerreiro Sombrio', 'Clérigo Corrompido', 'Gigante', 'Monstro do Lago',
                'Ogro', 'Escorpião', 'Cobra Selvagem', 'Lobo', 'Crocodilo', 'Dragão', 'Infernal']

    # Monstros Divididos por nível
    monsters_lv1 = ['Goblin', 'Rato', 'Esqueleto', 'Slime', 'Aranha', 'Zumbi', 'Duente']
    monsters_lv2 = ['Bandido', 'Orc', 'Mago', 'Fantasma', 'Arcano', 'Ogro', 'Escorpião', 'Cobra Selvagem', 'Lobo',
                    'Crocodilo']
    monsters_lv3 = ['Fada', 'Spectro', 'Guerreiro Sombrio', 'Clérigo Corrompido']
    monsters_lv4 = ['Gigante', 'Monstro do Lago', 'Dragão']
    monsters_lv10 = ['Infernal']

    # Monstros lv1 - power
    monster_power_lv1 = 200

    # Monstros lv2 - power
    monster_power_lv2 = 300

    # Monstros lv3 - power
    monster_power_lv3 = 400

    # Monstros lv4 - power
    monster_power_lv4 = 600

    # Infernal lv10 - oower
    monster_power_lv10 = 10000

    # Personagens + Esquema de Poder
    # Definição de power por nível do usuário
    user_card = ['Guerreiro', 'Espadachim', 'Arqueiro', 'Cavaleiro', 'Arcanista']
    usuario = random.choice(user_card)
    user_level = random.randint(1, 4)

    card_monster = random.choice(monsters)
    lv_monster = random.randint(1, 4)

    power_usuario = 1500
    power_monster = 0

    power_lv1 = 1530
    power_lv2 = 2300
    power_lv3 = 3440
    power_lv4 = 5300

    if user_level == 1:
        power_usuario = power_usuario + power_lv1
    elif user_level == 2:
        power_usuario = power_usuario + power_lv2
    elif user_level == 3:
        power_usuario = power_usuario + power_lv3
    elif user_level == 4:
        power_usuario = power_usuario + power_lv4

    # Condicionais para V/D monstros
    while power_usuario > 0:
        # Variáveis para o Item de bonus
        powerBonus = random.randint(1000, 5000)
        choice = random.randint(1, 20)
        sleep(0.7)
        # Definição de níveis conforme a entidade + poder inicial
        if lv_monster == 1:
            power_monster = power_monster + power_lv1
            aumento_de_poder()
            if card_monster == 'Infernal':
                boss.play()
                print(red + '   VOCÊ ENCONTROU UM BOSS INFERNAL NIVEL 10')
                if skipBoss >= 1:
                    print(green + '    Você possui um item para Fugir!')
                    print('    Deseja Fugir?')
                    print(green + '                 Sim' + yellow + ' / ' + red + 'Não              ' + normal)
                    escolha_usar_item = str(input('    --> ')).upper().strip()
                    if escolha_usar_item == 'SIM' or escolha_usar_item == 'S':
                        selecionar.play()
                        print(ciano + '    Você Fugiu!')
                        print(ciano + '    Seu item foi Consumido!')
                        skipBoss = skipBoss - 1
                        card_monster = random.choice(monsters)
                        lv_monster = random.randint(1, 4)
                        sleep(3)
                    else:
                        selecionar.play()
                        print(ciano + '    Você não usou o item!')
                        power_monster = power_monster + monster_power_lv10
                        lv_monster = 10
                        user_level = user_level - 5
                        power_usuario = power_usuario - 1000
                        print(red + '   DANO CRÍTICO!' + normal)
                        sleep(3)
                        critico_infernal()
                elif skipBoss <= 0:
                    power_monster = power_monster + monster_power_lv10
                    lv_monster = 10
                    user_level = user_level - 5
                    power_usuario = power_usuario - 1000
                    print(red + '   DANO CRÍTICO!' + normal)
                    sleep(3)
                    critico_infernal()
                print('\n')
            if_monsters()
        elif lv_monster == 2:
            power_monster = power_lv2
            aumento_de_poder()
            if card_monster == 'Infernal':
                boss.play()
                print(red + '   VOCÊ ENCONTROU UM BOSS INFERNAL NIVEL 10')
                if skipBoss >= 1:
                    print(green + '    Você possui um item para Fugir!')
                    print('    Deseja Fugir?')
                    print(green + '                 Sim' + yellow + ' / ' + red + 'Não              ' + normal)
                    escolha_usar_item = str(input('    --> ')).upper().strip()
                    if escolha_usar_item == 'SIM' or escolha_usar_item == 'S':
                        selecionar.play()
                        print(ciano + '    Você Fugiu!')
                        print(ciano + '    Seu item foi Consumido!')
                        skipBoss = skipBoss - 1
                        card_monster = random.choice(monsters)
                        lv_monster = random.randint(1, 4)
                        sleep(3)
                    else:
                        selecionar.play()
                        print(ciano + '    Você não usou o item!')
                        power_monster = power_monster + monster_power_lv10
                        lv_monster = 10
                        user_level = user_level - 5
                        power_usuario = power_usuario - 1000
                        print(red + '   DANO CRÍTICO!' + normal)
                        sleep(3)
                        critico_infernal()
                elif skipBoss <= 0:
                    power_monster = power_monster + monster_power_lv10
                    lv_monster = 10
                    user_level = user_level - 5
                    power_usuario = power_usuario - 1000
                    point = point - 100
                    print(red + '   DANO CRÍTICO!' + normal)
                    sleep(3)
                    critico_infernal()
                print('\n')
            if_monsters()
        elif lv_monster == 3:
            power_monster = power_lv3
            aumento_de_poder()
            if card_monster == 'Infernal':
                boss.play()
                print(red + '   VOCÊ ENCONTROU UM BOSS INFERNAL NIVEL 10')
                if skipBoss >= 1:
                    print(green + '    Você possui um item para Fugir!')
                    print('    Deseja Fugir?')
                    print(green + '                 Sim' + yellow + ' / ' + red + 'Não              ' + normal)
                    escolha_usar_item = str(input('    --> ')).upper().strip()
                    if escolha_usar_item == 'SIM' or escolha_usar_item == 'S':
                        selecionar.play()
                        print(ciano + '    Você Fugiu!')
                        print(ciano + '    Seu item foi Consumido!')
                        skipBoss = skipBoss - 1
                        card_monster = random.choice(monsters)
                        lv_monster = random.randint(1, 4)
                        sleep(3)
                    else:
                        selecionar.play()
                        print(ciano + '    Você não usou o item!')
                        power_monster = power_monster + monster_power_lv10
                        lv_monster = 10
                        user_level = user_level - 5
                        power_usuario = power_usuario - 1000
                        print(red + '   DANO CRÍTICO!' + normal)
                        sleep(3)
                        critico_infernal()
                elif skipBoss <= 0:
                    power_monster = power_monster + monster_power_lv10
                    lv_monster = 10
                    user_level = user_level - 5
                    power_usuario = power_usuario - 1000
                    print(red + '   DANO CRÍTICO!' + normal)
                    sleep(3)
                    critico_infernal()
                print('\n')
            if_monsters()
        elif lv_monster == 4:
            power_monster = power_lv4
            aumento_de_poder()
            if card_monster == 'Infernal':
                boss.play()
                print(red + '   VOCÊ ENCONTROU UM BOSS INFERNAL NIVEL 10')
                if skipBoss >= 1:
                    print(green + '    Você possui um item para Fugir!')
                    print('    Deseja Fugir?')
                    print(green + '                 Sim' + yellow + ' / ' + red + 'Não              ' + normal)
                    escolha_usar_item = str(input('    --> ')).upper().strip()
                    if escolha_usar_item == 'SIM' or escolha_usar_item == 'S':
                        selecionar.play()
                        print(ciano + '    Você Fugiu!')
                        print(ciano + '    Seu item foi Consumido!')
                        skipBoss = skipBoss - 1
                        card_monster = random.choice(monsters)
                        lv_monster = random.randint(1, 4)
                        sleep(3)
                    else:
                        selecionar.play()
                        print(ciano + '    Você não usou o item!')
                        power_monster = power_monster + monster_power_lv10
                        lv_monster = 10
                        user_level = user_level - 5
                        power_usuario = power_usuario - 1000
                        print(red + '   DANO CRÍTICO!' + normal)
                        sleep(3)
                        critico_infernal()
                elif skipBoss <= 0:
                    power_monster = power_monster + monster_power_lv10
                    lv_monster = 10
                    user_level = user_level - 5
                    power_usuario = power_usuario - 1000
                    print(red + '   DANO CRÍTICO!' + normal)
                    sleep(3)
                    critico_infernal()
                print('\n')
            if_monsters()
        if choiceBonus > 0 and choice == 1:
            selecionar.play()
            print(green + '    Você Encontrou um item Raro!')
            print('    Recebeu {} de Poder!'.format(powerBonus))
            print(ciano + '    Seu item foi Consumido!')
            choiceBonus = choiceBonus - 1
            power_usuario = power_usuario + powerBonus
            sleep(3)
            print('\n')
        # Condição para ganhar/perder o jogo
        if user_level == 100:
            # Atribuição de valores
            if multiplicador < 2.00:
                multiplicador = 2.00
                valorTotal = (aposta * multiplicador)
                print(green + 'Parabéns!')
                print('   Você venceu a Dungeon!' + normal)
                print('   Pontuação --> ', end='')
                print(f'{point}')
                print('   Batalhas --> {}'.format(cont))
                print(green + '   Valor Acumulado R${:.2f}'.format(valorTotal))
                print(green + '   2x Pela Vitória!' + normal)
                mixer.music.stop()
                win.play()
                x = int(input(''))
                break
            else:
                valorTotal = aposta * multiplicador
                print(green + 'Parabéns!')
                print('   Você venceu a Dungeon!' + normal)
                print('   Pontuação --> ', end='')
                print(f'{point}')
                print('   Batalhas --> {}'.format(cont))
                print(green + '   Valor Acumulado R${:.2f}'.format(valorTotal))
                mixer.music.stop()
                win.play()
                x = int(input(''))
                break
        elif power_usuario <= 350 or user_level <= 0:
            # Atribuição de valores
            if point <= 0:
                point = 0
                valorTotal = 0
            else:
                valorTotal = aposta * multiplicador
            print(yellow + '   -x-x-x-x--x-x-x-x--x-x-x-x--x-' + normal)
            print(yellow + '   -x-x-x-x-' + red + 'Você Morreu!' + yellow + '-x-x-x-x-' + normal)
            print(yellow + '   -x-x-x-x--x-x-x-x--x-x-x-x--x-' + normal)
            print('   Pontuação --> ', end='' + green)
            print(f'{point}' + normal)
            print('   Batalhas --> ', end='' + green)
            print(f'{cont}')
            print(green + '   Valor Acumulado R${:.2f}'.format(valorTotal))
            mixer.music.stop()
            lose.play()
            x = int(input(''))
            break
        # Contador de batalhas

        cont += 1

        # Informação na tela
        print(f'\033[32m   {usuario}\033[m', end=' ')
        print(f'\033[33mLv {user_level}\033[m X \033[31m{card_monster}\033[m', end=' ')
        print(f'\033[33mLv {lv_monster}\033[m')
        print(f'\033[33m   Power: {power_usuario}\033[m', end='   X')
        print(f'\033[33m  Power: {power_monster}\033[m')
        result()
        print('   --> {:.2f}x'.format(multiplicador))
        print('   --> {} Pontos'.format(point))
elif iniciar_jogo == 'NÃO' or iniciar_jogo == 'N':
    print(green + '               Escolheu Bem!' + normal)
    mixer.music.stop()
    lose.play()
    x = int(input(''))

else:
    print(red + '   Resposta errada!' + normal)
    print('    Jogo Pausado!')
