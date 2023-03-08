import pygame
import os
# from chef_main import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Cooking Chef | indev Build:20_06/03/2023")

icon = pygame.image.load("favicon.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background.png")
background.set_alpha(100)
screen.blit(background, (0, 0))

font = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 16)
text_surface1 = font.render("An announcment from Jonathan Emerald Corporation©!", True, (255, 100, 65))
text_surface2 = font2.render("This application is currently under maintenance, please come back later!", True, (255, 100, 65))

screen.blit(text_surface1, (100, 200))
screen.blit(text_surface2, (120, 220))

pygame.display.flip()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	clock.tick(60)

pygame.quit()