import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
selecionar = pygame.mixer.Sound(r'music\escolha12.wav')
pygame.mixer.music.load(r'music\digital.mp3')
pygame.mixer.music.play(-1)

# Defina as dimensões da janela
window_width = 640
window_height = 480

# Crie a janela
pygame.display.set_caption(" | JOGO DO PODER |")
screen = pygame.display.set_mode((window_width, window_height))

# Defina a fonte e o tamanho do texto
font = pygame.font.SysFont('Arial', 25)
font_max = pygame.font.SysFont('Arial', 26)

# Background-image - Static
bg = pygame.image.load('img/MolduraComDrag.png').convert_alpha()
bg = pygame.transform.scale(bg, (window_width, window_height))

# Background-image - Moving
bg_moving = pygame.image.load('img/dungeon.jpg').convert_alpha()
bg_moving = pygame.transform.scale(bg_moving, (window_width, window_height))

# Img - Botão de Play
play = pygame.image.load('img/start.png')
playClick = pygame.image.load('img/startClick.png')
testeplay = play
pos_testeplay = testeplay.get_rect(center=(window_width // 2, (window_height // 2) + 100))

# Texto/Imagens Menu 1
powerGame = pygame.image.load('img/powergame2.png')
powerGame_rect = powerGame.get_rect(center=(window_width // 2, window_height // 3))

# Texto/Imagens Menu 2
itensDisponiveis = pygame.image.load('img/itensDisponiveis2.png')
itensDisponiveis_rect = itensDisponiveis.get_rect(center=(window_width // 2, window_height // 6))

coin_text = pygame.image.load('img/cointext2.png')
coin_text_size = (coin_text.get_width() * 0.5, coin_text.get_height() * 0.5)
coin_text = pygame.transform.scale(coin_text, coin_text_size)
coin_text_rect = coin_text.get_rect(center=(window_width // 2 - 23, window_height // 2))

coin = pygame.image.load('img/valor_img4.png')
coin_size = (coin.get_width(), coin.get_height())
coin = pygame.transform.scale(coin, coin_size)
coin_rect = coin.get_rect(center=(window_width // 2, window_height // 5))

item1 = pygame.image.load('img/skip.png')
item1_size = (item1.get_width() * 0.4, item1.get_height() * 0.4)
item1 = pygame.transform.scale(item1, item1_size)
item1_rect = item1.get_rect(center=(120, 175))

item2 = pygame.image.load('img/power.png')
item2_size = (item2.get_width() * 0.0999, item2.get_height() * 0.0999)
item2 = pygame.transform.scale(item2, item2_size)
item2_rect = item2.get_rect(center=(120, 245))

text_item1 = font.render("SKIP BOSS (1)", True, (255, 255, 255))
text_item1_rect = text_item1.get_rect(center=(240, 175))

text_item2 = font.render("PODER EXTRA (2)", True, (255, 255, 255))
text_item2_rect = text_item2.get_rect(center=(262, 250))
# Texto /Imagens Menu 3
text_escolha_item = font.render('', True, (0, 255, 0))
text_escolha_item_rect = text_escolha_item.get_rect(center=(144, 120))

# Valor que o usuário digitou antes de apertar Enter
valorDigitado = []
# Valor final apostado
valorApostado = 0

number_text = ''
# TEXT_SURFACE = 2 L 188
text_surface = font.render(number_text, True, (0, 255, 0))
text_surface_rect = text_surface.get_rect(center=(window_width // 2 - 86, window_height // 2))
letterLimit = 0


# Função de Aposta
def aposta():
    global valorDigitado, valorApostado, letterLimit, menu
    if event.unicode.isdigit():
        # Adicione o número digitado à lista de números
        if letterLimit < 14:
            valorDigitado.append(event.unicode)
            letterLimit = letterLimit + 1
    elif event.key == K_BACKSPACE:
        # Remover o último caractere do texto
        valorDigitado = valorDigitado[:-1]
        if letterLimit > 0:
            letterLimit = letterLimit - 1
    elif event.key == K_RETURN:
        selecionar.play()
        if valorDigitado:
            valorApostado = int(''.join(map(str, valorDigitado)))
        menu = 4


# Menu de seleção/ Variáveis importantes
menu = 1
item_escolhido = 0

while True:
    for event in pygame.event.get():
        # Posição do Mouse
        mouse_pos = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_pos, (1, 1))
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and menu == 3:
            aposta()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Menu de Play
            if pos_testeplay.collidepoint(mouse_pos) and menu == 1:
                menu = 2
                selecionar.play()
                screen.fill((0, 0, 0))
                # Menu de Poderes (Adicionado como screen.blit)
            # Item 1
            if item1_rect.collidepoint(mouse_pos) or text_item1_rect.collidepoint(mouse_pos) and menu == 2:
                menu = 3
                item_escolhido = 1
                selecionar.play()
                screen.fill((0, 0, 0))
            # Item 2
            elif item2_rect.collidepoint(mouse_pos) or text_item2_rect.collidepoint(mouse_pos) and menu == 2:
                menu = 3
                item_escolhido = 2
                selecionar.play()
                screen.fill((0, 0, 0))
                # Efeito ao passar o mouse por cima
            if menu == 3 and item_escolhido == 1:
                text_escolha_item = font.render('ESCOLHIDO: SKIP BOSS (1)', True, (0, 255, 0))
            elif menu == 3 and item_escolhido == 2:
                text_escolha_item = font.render('ESCOLHIDO: PODER EXTRA (2)', True, (0, 255, 0))
        # Deixa a cor da letra amarela após passar por cima
        elif event.type == pygame.MOUSEMOTION and menu == 2:
            if text_item1_rect.collidepoint(event.pos) or item1_rect.collidepoint(event.pos):
                text_item1 = font.render("SKIP BOSS (1)", True, (255, 255, 0))
            else:
                text_item1 = font.render("SKIP BOSS (1)", True, (255, 255, 255))

            if text_item2_rect.collidepoint(event.pos) or item2_rect.collidepoint(event.pos):
                text_item2 = font.render("PODER EXTRA (2)", True, (255, 255, 0))
            else:
                text_item2 = font.render("PODER EXTRA (2)", True, (255, 255, 255))
        if mouse_rect.colliderect(pos_testeplay) and menu == 1:
            testeplay = playClick
        else:
            testeplay = play

    # Back - Moving
    screen.blit(bg_moving, (0, 0))

    rel_x = window_width % bg_moving.get_rect().width
    screen.blit(bg_moving, (rel_x - bg_moving.get_rect().width, 0))
    if rel_x < 640:
        screen.blit(bg_moving, (rel_x, 0))
    window_width = window_width - 0.1

    # Desenhe o texto na tela / baseados em menus
    if menu == 1:
        screen.blit(bg, (0, 0))
        screen.blit(testeplay, pos_testeplay)
        screen.blit(powerGame, powerGame_rect)
    if menu == 2:
        screen.blit(bg, (0, 0))
        screen.blit(text_item1, text_item1_rect)
        screen.blit(text_item2, text_item2_rect)
        screen.blit(itensDisponiveis, itensDisponiveis_rect)
        screen.blit(item1, item1_rect)
        screen.blit(item2, item2_rect)
    if menu == 3:
        screen.blit(coin, coin_rect)
        screen.blit(coin_text, coin_text_rect)
        number_text = ''.join(valorDigitado)
        text_surface = font.render(number_text, True, (255, 0, 60))
        screen.blit(text_surface, text_surface_rect)

    screen.blit(bg, (0, 0))
    pygame.display.update()
