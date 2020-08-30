# Classe objets : 

import pygame
from pygame.locals import *
from constants import *
from labyrinthe import *
from gyver import *
import random 


class Items:

    def __init__ (self, labyrinthe, image, character) :
        
        self.character = character
        self.image = image
        
        self.labyrinthe  = labyrinthe 
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
                    
    def randomness (self) :

        rand_x = random.randint(0,14)
        rand_y = random.randint(0,14)

        while self.labyrinthe.structure[rand_y][rand_x] != '_': 
            
            rand_x = random.randint(0,14)
            rand_y = random.randint(0,14)

        self.case_x = rand_x  
        self.case_y = rand_y   
        self.x = self.case_x * sprite_size
        self.y = self.case_y * sprite_size
        self.labyrinthe.structure[self.case_y][self.case_x] = self.character

    def draw(self, window) :

        window.blit(self.image, (self.x, self.y))