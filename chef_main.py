# text colour: print("\033[1;32;40m Bright Green  \n")
# reset colour: print("\033[0m Hiya")

# common: \033[32m
# uncommon: \033[32;1m
# rare: \033[34m
# epic: \033[35m
# legendary: \033[31;1m
# mythic/unique: \033[36;1m

import time
from chef_skeleton import *
from chef_func import *

version_id = "build:18_05/03/23 | Please email: ccg.issues@gmail.com for any issues you may encounter, Thank you!"

equip1 = Equipment("\033[32mPotato Spatula\033[0m", "Boosts the cooking speed of all recipes by 5 seconds", 0, 5, 1, "a107")
equip2 = Equipment("\033[32;1mAdvanced Potato Spatula\033[0m", "Boosts the cooking speed of all recipes by 10 seconds", 1, 10, 1, "b107")
equip3 = Equipment("\033[36;1mExcellent Potato Masher\033[0m", "Boosts the cooking speed of Roasted Potatoes by 15 seconds", 5, 15, 1, "c107")
recipe1 = Recipe("\033[32mRoasted Potatoes\033[0m", 100, 0, 15, 1, "a106")
recipe2 = Recipe("\033[32mChicken with Roasted Potatoes\033[0m", 100, 0, 10, 1, "b106")
recipe3 = Recipe("\033[32mMashed Potatoes\033[0m", 100, 0, 5, 1, "c106")     
lootbox1 = LootBox("\033[32mGeneric LootBox™\033[0m", "The most generic LootBox™", 0, 1, "a201")
lootbox2 = LootBox("\033[32;1mNormal LootBox™\033[0m", "The most basic LootBox™ for equipment", 1, 1, "a202")
lootbox3 = LootBox("\033[34mRare LootBox™\033[0m", "Wow it's rare", 2, 1, "b201")

Equipment.equipbox1_inv.append(equip1)
Equipment.equipbox1_inv.append(equip2)
Equipment.equipbox1_inv.append(equip3)
Recipe.lootbox1_inv.append(recipe1)
Recipe.lootbox1_inv.append(recipe2)
Recipe.lootbox1_inv.append(recipe3)
LootBox.loot_inv.append(lootbox1)
LootBox.loot_inv.append(lootbox2)
LootBox.loot_inv.append(lootbox3)

# gameloop plan:
# initalise menu:
# 1 - new game
# 2 - load saved game
# 3 - options - anything like delete character, colours and other settings once the pygame application is done will go here
# 4 - exit game

# once tutorial has finished (create a finished_tutorial variable to check if tutorial has been finished):
# 1 - Cook a recipe
# 2 - browse your inventory
# 3 - open lootboxes
# 4 - save game
# 5 - back to main menu
def main(player):
	while True:

	#	if tutorial_completed == False:
			# tutorial loop	

		player_level_up(player)
		print("\033[44m------MAIN MENU------\033[0m")
		print("1 - Cook a recipe")
		print("2 - Browse your inventory")
		print("3 - Open LootBox™")
		print("4 - Save your game")
		print("5 - Return to menu")
		try:
			gameloop_input = int(input("Which option would you like to continue with?: "))
		except ValueError:
			print("Invalid option, please try again!")
			return main(player)

		if gameloop_input == 1:
			cooking_input(player)
			return main(player)
		elif gameloop_input == 2:
			print("1 - Recipes Notebook")
			print("2 - Item Storage")
			print("3 - LootBox™ Storage")
			print("3 - Go back")
			check_inv_input = int(input("What would you like to check?: "))

			if check_inv_input == 1:
				player.check_inv()
				return main(player)
			elif check_inv_input == 2:
				player.check_equip_inv()
				return main(player)
			elif check_inv_input == 3:
				LootBox.check_loot_inv()
				return main(player)
		elif gameloop_input == 3:
			open_lootbox()
			return main(player)
		elif gameloop_input == 4:
			save_game(player)
			return main(player)
		elif gameloop_input == 5:
			return main_menu()

def main_menu():
	print("\033[42;15mWelcome to Cooking Chef!\033[0m")
	print("\033[44mYou are playing on\033[0m: " + version_id)
	print("What would you like to do?")
	print("\nSelect your option:")
	print("1 - Start a new game")
	print("2 - Load saved game")
	print("3 - Options")
	print("4 - Exit game")
	try:
		menu_input = int(input())
	except ValueError:
		print("Please pick an option from the provided list!")
		return main_menu()
	if menu_input == 1:
		player = Player("", 0, 0, 0, 0)
		playername = input("Please enter your name, young chef!: ")
		player.name = playername
		main(player)
	elif menu_input == 2:
		player = Player("", 0, 0, 0, 0)
		load_game(player)
		if player.name == "":
			menu_input = 1
			playername = input("Please enter your name, young chef!: ")
			player.name = playername			
			main(player)
		else:
			main(player)
	elif menu_input == 3:
		print("\033[43mOptions not avaliable yet, please check again later!\033[0m")
		return main_menu()
	elif menu_input == 4:
		print("\033[36mThank you for playing!\033[0m")
		exit()
	else:
		print("You have entered an invalid input, please try again!")
		return main_menu()

main_menu()