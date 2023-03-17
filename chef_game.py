import importlib
import subprocess
import time

try:
	importlib.import_module('pygame')
except ImportError:
	install_key = "Y"
	if install_key == "Y":
		print("\033[42mInstalling additional dependencies\033[0m")
		subprocess.call(['pip', 'install', 'pygame'])
	else:
		print("\033[43mRequired dependencies not installed, please install manually by using 'pip install pygame', or try opening the application again!\033[0m")
		time.sleep(5)
		exit()
try:
	importlib.import_module('keyboard')
except ImportError:
	install_key = "Y"
	if install_key == "Y":
		print("\033[42mInstalling additional dependencies\033[0m")
		subprocess.call(['pip', 'install', 'keyboard'])
	else:
		print("\033[43mRequired dependencies not installed, please install manually by using 'pip install keyboard', or try opening the application again!\033[0m")
		time.sleep(5)
		exit()

import pygame
import keyboard


def main():
	pygame.init()
	screen = pygame.display.set_mode((1040, 550))
	pygame.display.set_caption("Cooking Chef | Build:(A)1_16/03/2023")

	icon = pygame.image.load("Assets/favicon.png")
	pygame.display.set_icon(icon)

	menuButton = pygame.image.load("Assets/menu_button_1.png")

	def renderGame(screen):
		screen.fill((0,0,0))

		screen.blit(menuButton, (0,0))

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		renderGame(screen)
		pygame.display.update()


if __name__ == "__main__":
	main()