import pygame
import os
# from chef_main import *

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Cooking Chef | indev Build:19_05/03/2023")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.fill((255, 255, 255))
	pygame.draw.circle(screen, (255, 0, 0), (250, 250), 50)


	pygame.display.update()