""" classe labyrinthe"""

import pygame

from constants import sprite_size
from constants import image_wall
from constants import image_gardien
from constants import image_ether
from constants import image_tube
from constants import image_aiguille

pygame.init()


class Labyrinthe:
    def __init__(self, file):  # initialize the labyrinth class
        self.file = "listlaby.txt"
        self.structure = 0
        self.mg_init_pos = []

    def generate(self):  # générer le labyrinthe

        with open(self.file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            laby = []
            num_line = 0
            for line in lines:
                # on parcourt les lignes de la liste

                line.replace("\n", "")
                line_laby = []
                num_case = 0

                for sprite in line:
                    if sprite != "\n":
                        num_case += 1
                        line_laby.append(sprite)
                laby.append(line_laby)

                num_line += 1
            self.structure = laby

    def display(self, window):
        """ méthod displays maze """
        # loading images
        mur = pygame.image.load(image_wall).convert()
        gardien = pygame.image.load(image_gardien).convert_alpha()
        ether = pygame.image.load(image_ether).convert_alpha()
        aiguille = pygame.image.load(image_aiguille).convert_alpha()
        tube = pygame.image.load(image_tube).convert_alpha()

        num_line = 0
        for line in self.structure:
            # browse lists of lines
            num_case = 0
            for sprite in line:
                # calculate position in pixels
                x = num_case * sprite_size
                y = num_line * sprite_size
                if sprite == "m":
                    window.blit(mur, (x, y))
                elif sprite == "g":
                    window.blit(gardien, (x, y))
                elif sprite == "e":
                    window.blit(ether, (x, y))
                elif sprite == "a":
                    window.blit(aiguille, (x, y))
                elif sprite == "t":
                    window.blit(tube, (x, y))
                elif sprite == "h":
                    self.mg_init_pos = [num_case, num_line]

                num_case += 1
            num_line += 1
