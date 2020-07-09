# MacGyver scripts game

import pygame
from pygame.locals import *
from constants import *

pygame.init()

#Open Pygame window  
window = pygame.display.set_mode((cote_window, cote_window))

#Loading and pasting of the background
fond = pygame.image.load("images/background.jpg").convert()

continuer = 1
while continuer:

	for event in pygame.event.get(): # Waiting for events
		pygame.display.flip()
		if event.type == QUIT:
			continuer = 0