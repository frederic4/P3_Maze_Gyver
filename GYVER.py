
import pygame
from pygame.locals import*
from constantes import*


class McGyver:
		""" Classe permettant de créer McGyver"""
		def __init__ (self, labyrinthe, url_image_gyver, position):
				
				self.mg_image = pygame.image.load(url_image_gyver).convert_alpha()
				
				self.case_x = position[0]
				self.case_y = position[1]

				self.x = position[0]*sprite_size
				self.y = position[1]*sprite_size # position dépendante du paramètre
				self.old_pos = (self.x, self.y)
				

	