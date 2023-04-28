import pygame
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r'music\digital.mp3')
pygame.mixer.music.play(-1)

test = pygame.mixer.Sound(r'music\escolha12.wav')

window_width = 640
window_height = 480

pygame.display.set_caption('| Choice Player |')
screen = pygame.display.set_mode((window_width, window_height))

font = pygame.font.SysFont('Arial', 25)
title_font = pygame.font.SysFont('Arial', 30)

bg = pygame.image.load(r'img/moldura_Fundo.png').convert_alpha()
bg = pygame.transform.scale(bg, (window_width, window_height))

# Play inicial
play = pygame.image.load('img/start.png')
playClick = pygame.image.load('img/startClick.png')
testeplay = play
pos_testeplay = testeplay.get_rect(center=(window_width // 2, (window_height // 2) + 100))

# Drink
playgame = pygame.image.load('img/start.png')
playClickgame = pygame.image.load('img/startClick.png')
testeplaygame = playgame
pos_testeplaygame = testeplaygame.get_rect(center=(window_width // 2, (window_height // 2) + 100))

players = ['Kristofer', 'Lívia', 'Ramon', 'Fran', 'Jhonatan', 'Rapariga']
amount_of_players = len(players)
chosen_player = ''
text_player = font.render(chosen_player, True, (255, 255, 255))
text_player_rect = text_player.get_rect(center=(0, 0))

player1 = font.render(players[0], True, (255, 255, 255))
player1_rect = player1.get_rect(center=(80, 50))
point1 = 0
point1_text = font.render(str(point1), True, (255, 255, 255))
point1_text_rect = point1_text.get_rect(center=(0, 0))

player2 = font.render(players[1], True, (255, 255, 255))
player2_rect = player2.get_rect(center=(80, 80))
point2 = 0
point2_text = font.render(str(point2), True, (255, 255, 255))
point2_text_rect = point2_text.get_rect(center=(0, 0))

player3 = font.render(players[2], True, (255, 255, 255))
player3_rect = player3.get_rect(center=(80, 110))
point3 = 0
point3_text = font.render(str(point3), True, (255, 255, 255))
point3_text_rect = point3_text.get_rect(center=(0, 0))

player4 = font.render(players[3], True, (255, 255, 255))
player4_rect = player4.get_rect(center=(80, 140))
point4 = 0
point4_text = font.render(str(point4), True, (255, 255, 255))
point4_text_rect = point4_text.get_rect(center=(0, 0))

player5 = font.render(players[4], True, (255, 255, 255))
player5_rect = player5.get_rect(center=(80, 170))
point5 = 0
point5_text = font.render(str(point5), True, (255, 255, 255))
point5_text_rect = point5_text.get_rect(center=(0, 0))

player6 = font.render(players[5], True, (255, 255, 255))
player6_rect = player6.get_rect(center=(90, 200))
point6 = 0
point6_text = font.render(str(point6), True, (255, 255, 255))
point6_text_rect = point6_text.get_rect(center=(0, 0))

menu = 1
while True:
    for event in pygame.event.get():
        # Mouse
        mouse_pos = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_pos, (1, 1))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos_testeplay.collidepoint(mouse_pos) and menu == 1:
                menu = 2
                test.play()
                screen.fill((0, 0, 0))
            elif pos_testeplaygame.collidepoint(mouse_pos) and menu == 2:
                test.play()
                chosen_player = random.choice(players)
                if chosen_player == players[0]:
                    point1 += 1
                elif chosen_player == players[1]:
                    point2 += 1
                elif chosen_player == players[2]:
                    point3 += 1
                elif chosen_player == players[3]:
                    point4 += 1
                elif chosen_player == players[4]:
                    point5 += 1
                elif chosen_player == players[5]:
                    point6 += 1
                screen.fill((0, 0, 0))
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_RETURN and menu == 1:
                menu = 2
                test.play()
                screen.fill((0, 0, 0))
            elif event.key == K_RETURN and menu == 2:
                test.play()
                chosen_player = random.choice(players)
                if chosen_player == players[0]:
                    point1 += 1
                elif chosen_player == players[1]:
                    point2 += 1
                elif chosen_player == players[2]:
                    point3 += 1
                elif chosen_player == players[3]:
                    point4 += 1
                elif chosen_player == players[4]:
                    point5 += 1
                elif chosen_player == players[5]:
                    point6 += 1
                screen.fill((0, 0, 0))
    if menu == 1:
        screen.blit(bg, (0, 0))
        screen.blit(testeplay, pos_testeplay)
    if menu == 2:
        text_player = title_font.render(chosen_player, True, (255, 255, 255))
        text_player_rect = text_player.get_rect(center=(320, 280))

        point1_text = font.render(str(point1), True, (0, 255, 255))
        point1_text_rect = point1_text.get_rect(center=(170, 50))
        screen.blit(point1_text, point1_text_rect)

        point2_text = font.render(str(point2), True, (0, 255, 255))
        point2_text_rect = point2_text.get_rect(center=(170, 80))
        screen.blit(point2_text, point2_text_rect)

        point3_text = font.render(str(point3), True, (0, 255, 255))
        point3_text_rect = point3_text.get_rect(center=(170, 110))
        screen.blit(point3_text, point3_text_rect)

        point4_text = font.render(str(point4), True, (0, 255, 255))
        point4_text_rect = point4_text.get_rect(center=(170, 140))
        screen.blit(point4_text, point4_text_rect)

        point5_text = font.render(str(point5), True, (0, 255, 255))
        point5_text_rect = point5_text.get_rect(center=(170, 170))
        screen.blit(point5_text, point5_text_rect)

        point6_text = font.render(str(point6), True, (0, 255, 255))
        point6_text_rect = point6_text.get_rect(center=(170, 200))
        screen.blit(point6_text, point6_text_rect)

        screen.blit(testeplaygame, pos_testeplaygame)
        screen.blit(text_player, text_player_rect)
        screen.blit(player1, player1_rect)
        screen.blit(player2, player2_rect)
        screen.blit(player3, player3_rect)
        screen.blit(player4, player4_rect)
        screen.blit(player5, player5_rect)
        screen.blit(player6, player6_rect)

    screen.blit(bg, (0, 0))
    pygame.display.update()
