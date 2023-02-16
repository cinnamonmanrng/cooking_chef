import pygame

# initalise pygame
pygame.init()

# set window size
window_size = (800, 600)

# create a window
screen = pygame.display.set_mode(window_size)

# name the application
pygame.display.set_caption("Master Chef I")

# define button position and size
button_rect = pygame.Rect(100, 100, 200, 50)

# define the button's appearance
button_color = (255, 255, 255)
border_color = (230, 230, 250)
button_text_color = (0, 0, 0)
font = pygame.font.Font(None, 36)
button_text = font.render("Hello!", True, button_text_color)

# running the application loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONUP:
			# checking if the button was clicked
			mouse_pos = pygame.mouse.get_pos()
			if button_rect.collidepoint(mouse_pos):
				print("Hello there!")

	# draw a border around the button using a second rectangle
	pygame.draw.rect(screen, border_color, (button_rect.left - 5, button_rect.top - 5, button_rect.width + 10, button_rect.height + 10), 2)

	#draw the button on the screen
	pygame.draw.rect(screen, button_color, button_rect)
	screen.blit(button_text, (100 + 65, 100 + 15))

	# update the screen
	pygame.display.update()

# quit pygame
pygame.quit()