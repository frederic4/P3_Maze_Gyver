""" classe labyrinthe"""

import pygame
from pygame.locals import *
from constants import *

pygame.init()

class Labyrinthe:
    def __init__ (self, file):# Constructeur pour initialiser la classe labyrinthe
        self.file = "listlaby.txt"
        self.structure = []

    def generate (self):# générer le labyrinthe

        with open(self.file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            laby = []
            for line in lines :
            # on parcourt les lignes de la liste

                line.replace('\n','') 
                line_laby = []
                num_case = 0

                for sprite in line :
                    if sprite != '\n':
                        num_case += 1
                        line_laby.append(sprite)
                laby.append(line_laby)

            self.structure = laby
                     

                
