# MacGyver scripts game

import pygame
from pygame.locals import *
from constants import *
from labyrinthe import *
from gyver import *

pygame.init()

#Open Pygame window  
window = pygame.display.set_mode((cote_window, cote_window))

#Loading and pasting of the background
fond = pygame.image.load("images/background.jpg").convert()




my_super_laby = Labyrinthe("listlaby.txt")
my_super_laby.generate()
my_super_laby.display(window)
structure = my_super_laby

pygame.display.flip()

macgyver = McGyver(my_super_laby, "Images/MGyver.png", my_super_laby.mg_init_pos) # création d'une variable 
macgyver.draw(window)

pygame.display.flip()

pygame.key.set_repeat(400, 30)

continuer = 1
while continuer:

	for event in pygame.event.get(): # Waiting for events
		pygame.display.flip()
		if event.type == QUIT:
			continuer = 0
		
		if event.type == KEYDOWN : 

			if event.key == K_RIGHT: # 
				macgyver.move ('right')
				macgyver.draw(window)

			elif event.key == K_DOWN: # 
				macgyver.move ('down')
				macgyver.draw(window) 

			elif event.key == K_UP :
				macgyver.move('up')
				macgyver.draw(window)

			elif event.key == K_LEFT:
				macgyver.move('left')
				macgyver.draw(window)



pygame.display.flip()          