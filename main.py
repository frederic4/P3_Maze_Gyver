# MacGyver scripts game
# PEP8

import pygame

from pygame.locals import K_RIGHT
from pygame.locals import K_LEFT
from pygame.locals import K_DOWN
from pygame.locals import K_UP
from pygame.locals import KEYDOWN
from pygame.locals import QUIT
from constants import cote_window
from labyrinthe import Labyrinthe
from items import Items
from gyver import McGyver


def main():

    pygame.init()

    # Open Pygame window
    window = pygame.display.set_mode((cote_window, cote_window))

    my_laby = Labyrinthe("listlaby.txt")
    my_laby.generate()
    my_laby.display(window)

    items_font = pygame.font.SysFont("arial", 30)  # font end character font
    items_text = items_font.render("Objets récupérés", 1, (0, 255, 0))  # color

    window.blit(items_text, (100, 0))

    pygame.display.flip()

    # create variable
    macgyver = McGyver(my_laby, "Images/MGyver.png", my_laby.mg_init_pos)
    macgyver.draw(window)

    # create randomly placed items
    aiguille = Items(my_laby, pygame.image.load("Images/aiguille.png"), "a")
    aiguille.randomness()
    aiguille.draw(window)

    tube = Items(my_laby, pygame.image.load("Images/tube.png"), "t")
    tube.randomness()
    tube.draw(window)

    ether = Items(my_laby, pygame.image.load("Images/ether.png"), "e")
    ether.randomness()
    ether.draw(window)

    pygame.display.flip()

    pygame.key.set_repeat(400, 30)

    continuer = 1
    while continuer:

        for event in pygame.event.get():  # Waiting for events
            pygame.display.flip()
            if event.type == QUIT:
                continuer = 0

            if event.type == KEYDOWN:

                if event.key == K_RIGHT:
                    macgyver.move("right")
                    macgyver.counter(window)
                    macgyver.draw(window)

                elif event.key == K_DOWN:
                    macgyver.move("down")
                    macgyver.counter(window)
                    macgyver.draw(window)

                elif event.key == K_UP:
                    macgyver.move("up")
                    macgyver.counter(window)
                    macgyver.draw(window)

                elif event.key == K_LEFT:
                    macgyver.move("left")
                    macgyver.counter(window)
                    macgyver.draw(window)

    pygame.display.flip()


if __name__ == '__main__':
    main()
