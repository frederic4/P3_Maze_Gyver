""" classe labyrinthe"""

import pygame
from pygame.locals import *
from constants import *

pygame.init()


class Labyrinthe:
    def __init__(self, file):  # Constructeur pour initialiser la classe labyrinthe
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
        """ méthode qui afiche le labyrinthe"""
        # chargement des images
        gyver = pygame.image.load(image_gyver).convert_alpha()
        mur = pygame.image.load(image_wall).convert()
        gardien = pygame.image.load(image_gardien).convert_alpha()
        ether = pygame.image.load(image_ether).convert_alpha()
        aiguille = pygame.image.load(image_aiguille).convert_alpha()
        tube = pygame.image.load(image_tube).convert_alpha()

        num_line = 0
        for line in self.structure:
            # parcourt des listes de lignes
            num_case = 0
            for sprite in line:
                # calcul de la position en pixel
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


# Class OK
