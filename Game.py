import pygame
from pygame.locals import *
from FlappyMan import *

# Rafraichir fenetre
pygame.init()

white = (255, 255, 255)

# Dimensions de la fenetre
fenetreL = 800
fenetreH = 500

# apparaitre fenetre + nom du jeu
fenetre = pygame.display.set_mode((fenetreL, fenetreH))
pygame.display.set_caption("Menu FlappyMan")

# image de fond
fond = pygame.image.load('fond.png')
fenetre.blit(fond, (0, 0))

# titre
titre = pygame.image.load ('titre.png')
fenetre.blit(titre,(250, 30))

# bouton start
play = pygame.image.load('play.png')
fenetre.blit(play, (275, 200))

# bouton start
instruction = pygame.image.load('instruction.png')
fenetre.blit(instruction, (200, 400))

pygame.display.flip()

# pouvoir quitté le programme
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if 250 <= event.pos[0] <= 550 and 200 <= event.pos[1] <= 300:
                    flappyMain()
