
import pygame
from pygame.locals import*
from constants import*


class McGyver:
		""" Classe permettant de créer McGyver"""
		def __init__ (self, labyrinthe, url_image_gyver, position):

			self.liste_items_full = ['a', 'e', 't']
			self.liste_items = []

			self.labyrinthe = labyrinthe

			self.mg_image = pygame.image.load(url_image_gyver).convert_alpha()
			
			self.case_x = position[0]
			self.case_y = position[1]

			self.x = position[0]*sprite_size
			self.y = position[1]*sprite_size # position dependent on the parameter
			self.old_pos = (self.x, self.y)
				
			self.items_counter = 0

		def move (self, direction):
			""" Methode permettant de déplacer MCgyver"""
			# créer une méthode checklist quel que soi la direction inventaire objets
			
			
			#Move to the right
			if direction == 'right':
			#Not to exceed the screen
				if self.case_x < (nombre_sprite_cote -1):
					#Check the box is not a wall
					if self.labyrinthe.structure[self.case_y][self.case_x+1] != 'm':
						self.old_pos = (self.x, self.y)#Old position 
						#Moving one box
						self.case_x += 1
						#Real position in pixels
						self.x = self.case_x * sprite_size#New position

			#Move to the left
			if direction == 'left':
				if self.case_x > 0 :
					if self.labyrinthe.structure[self.case_y][self.case_x-1] != 'm':
						self.old_pos = (self.x, self.y)  
						self.case_x -= 1
						self.x = self.case_x * sprite_size 
										
					
			#Moving up
			if direction == 'up':
				if self.case_y > 0 :
					if self.labyrinthe.structure[self.case_y-1][self.case_x] != 'm':
						self.old_pos = (self.x, self.y)
						self.case_y -= 1 
						self.y = self.case_y * sprite_size
						
						
			#Moving down
			if direction == 'down' :
				if self.case_y < (nombre_sprite_cote -1) :
					if self.labyrinthe.structure[self.case_y+1][self.case_x] != 'm':
						self.old_pos = (self.x, self.y) # ancienne position
						self.case_y += 1
						self.y = self.case_y * sprite_size	

			for letter in self.liste_items_full :
				if self.labyrinthe.structure[self.case_y][self.case_x] == letter:
					self.labyrinthe.structure[self.case_y][self.case_x] = '_'
					self.liste_items.append(letter)	
					
					self.items_counter +=1
					print(self.liste_items)

					print (self.items_counter)



			pygame.display.flip()	


		def counter (self, window) :
			if self.items_counter == 1 :
					one = pygame.image.load(image_one).convert()
					window.blit(one, (350,0))
			if self.items_counter == 2 :
					two = pygame.image.load(image_two).convert()
					window.blit(two, (350,0))
			if self.items_counter == 3 :
					three = pygame.image.load(image_three).convert()
					window.blit(three  , (350,0))	


		def draw(self, window):  
					#print (self.y, self.x)
					print (self.case_y, self.case_x)
								
					R  = pygame.Rect(self.old_pos, (30, 30)) #A chaque déplacement on blit une case noire 
					pygame.draw.rect(window, (0,0,0), R)
					window.blit(self.mg_image, (self.x, self.y))

					if self.labyrinthe.structure[self.case_y][self.case_x] == 'g' : 	
						if self.items_counter == 3 :	
				#ou fonctionne aussi if self.y == 420 and self.x == 210: # fonctionne fficher bien le message
							fond = pygame.image.load(image_win).convert() # Affiche bien l'image.
							window.blit(fond, (0,0))
					
						if self.items_counter != 3 :
			#if self.labyrinthe.structure[self.case_y][self.case_x] == 'g' and self.liste_items != []: 
			#if self.labyrinthe.structure[self.case_y][self.case_x] == 'g' and len(self.liste_items) != 3 :
			#if self.labyrinthe.structure[self.case_y][self.case_x] == 'g' and self.items_counter != 3 :# ligne a garder	
							fond = pygame.image.load(image_lost).convert()
							window.blit(fond, (0,0))

					
			
			
				
	