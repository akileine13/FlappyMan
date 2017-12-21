import pygame
import time
from random import *

white = (255, 255, 255)

pygame.init()

surfaceW = 800
surfaceH = 500
ballonW = 70
ballonH = 40
nuageW = 66
nuageH = 350
son = pygame.mixer.Sound("music.wav")


surface = pygame.display.set_mode((surfaceW, surfaceH))
pygame.display.set_caption("Ballon Volant")
clock = pygame.time.Clock()

img = pygame.image.load('superman.png')
img_nuage01 = pygame.image.load('tuyau_haut1.png')
img_nuage02 = pygame.image.load('tuyau_bas1.png')
fond = pygame.image.load ('fond.png')


def score(compte):
    police = pygame.font.Font('BradBunR.ttf', 16)
    texte = police.render("score : " + str(compte), True, white)
    surface.blit(texte, [10, 0])


def nuages(x_nuage, y_nuage, espace):
    surface.blit(img_nuage01, (x_nuage, y_nuage))
    surface.blit(img_nuage02, (x_nuage, y_nuage + nuageH + espace))


def rejoueOuQuitte():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None


def creaTexteObjs(texte, font):
    texteSurface = font.render(texte, True, white)
    return texteSurface, texteSurface.get_rect()


def msgSurface(texte):
    son.stop()
    GOTexte = pygame.font.Font('BradBunR.ttf', 150)
    petitTexte = pygame.font.Font('BradBunR.ttf', 20)

    titreTexteSurf, titreTexteRect = creaTexteObjs(texte, GOTexte)
    titreTexteRect.center = surfaceW / 2, ((surfaceH / 2) - 50)
    surface.blit(titreTexteSurf, titreTexteRect)

    petitTexteSurf, petitTexteRect = creaTexteObjs \
        ("Appuyez sur une touche pour rejouer", petitTexte)
    petitTexteRect.center = surfaceW / 2, ((surfaceH / 2) + 50)
    surface.blit(petitTexteSurf, petitTexteRect)

    pygame.display.update()
    time.sleep(2)

    while rejoueOuQuitte() == None:
        clock.tick()

    flappyMain()


def gameOver(score_actuel):
    msgSurface("Perdu!")


def ballon(x, y, image):
    surface.blit(image, (x, y))


def flappyMain():
    son.play()
    pygame.mixer.music.set_volume(0.3)
    x = 150
    y = 200
    y_move = 0

    x_nuage = surfaceW
    y_nuage = randint(-282, 20)
    espace = ballonH * 4
    nuage_vitesse = 2

    score_actuel = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -2
            if event.type == pygame.KEYUP:
                y_move = 2

        y += y_move

        surface.blit(fond, (0,0))
        ballon(x, y, img)

        nuages(x_nuage, y_nuage, espace)

        score(score_actuel)

        x_nuage -= nuage_vitesse

        if y > surfaceH - 40 or y < -10:
            gameOver(score_actuel)

        if x_nuage < (-1 * nuageW):
            x_nuage = surfaceW
            y_nuage = randint(-282, 20)

            if 5 <= score_actuel < 10:
                nuage_vitesse = 2.5
                espace = ballonH * 3.5
            if 10 <= score_actuel < 15:
                nuage_vitesse = 3
                espace = ballonH * 3
            if 15 <= score_actuel < 20:
                nuage_vitesse = 3.5
                espace = ballonH * 3
            if 20 <= score_actuel < 30:
                nuage_vitesse = 4
                espace = ballonH * 3
            if 30 <= score_actuel < 40:
                nuage_vitesse = 4.5
                espace = ballonH * 3
            if 40 <= score_actuel < 40:
                nuage_vitesse = 5
                espace = ballonH * 2.5
            if 50 <= score_actuel:
                nuage_vitesse = 8
                espace = ballonH * 2

        if x + ballonW > x_nuage + 40:
            if y < y_nuage + nuageH - 50:
                if x - ballonW < x_nuage + nuageW - 10:
                    # print("touche haut!!!")
                    gameOver(score_actuel)

        if x + ballonW > x_nuage + 40:
            if y + ballonH > y_nuage + nuageH + espace + 50:
                if x - ballonW < x_nuage + nuageW - 10:
                    # print("touche bas!!!")
                    gameOver(score_actuel)

        if x_nuage < (x - nuageW) < x_nuage + nuage_vitesse + 0.5:
            score_actuel += 1

        pygame.display.update()
