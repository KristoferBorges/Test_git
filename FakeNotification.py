import pygame
import random
pygame.init()
pygame.mixer.init()
selecionar = pygame.mixer.Sound(r'music\notify2.mp3')

pygame.display.set_caption(" | NOTIFY |")
window_width = 640
window_height = 480

screen = pygame.display.set_mode((window_width, window_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            selecionar.play()
        if random.randint(0, 91) == 1:
            selecionar.play()
    notify = random.randint(0, 30390)
    if notify == 1:
        selecionar.play()

    pygame.display.update()
