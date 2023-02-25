import time
from chef_skeleton import *
from chef_func import *

equip1 = Equipment("\033[32mPotato Spatula\033[0m", "Boosts the cooking speed of all recipes by 5 seconds", 0, 5, 1, "a107")
equip2 = Equipment("\033[32;1mAdvanced Potato Spatula\033[0m", "Boosts the cooking speed of all recipes by 10 seconds", 1, 10, 1, "b107")
equip3 = Equipment("\033[36;1mExcellent Potato Masher\033[0m", "Boosts the cooking speed of Roasted Potatoes by 15 seconds", 5, 15, 1, "c107")
recipe1 = Recipe("\033[32mRoasted Potatoes\033[0m", 100, 0, 15, 1, "a106")
recipe2 = Recipe("\033[32mChicken with Roasted Potatoes\033[0m", 100, 0, 15, 1, "b106")
recipe3 = Recipe("\033[32mMashed Potatoes\033[0m", 100, 0, 5, 1, "c106")
lootbox1 = LootBox("\033[32mGeneric LootBox™\033[0m", "The most generic LootBox!", 0, 1, "a201")

def main():
	while True:	
		Equipment.equip_inv.append(equip1)
		Equipment.equip_inv.append(equip2)
		Equipment.equip_inv.append(equip3)
		Recipe.recipe_inv.append(recipe1)
		Recipe.recipe_inv.append(recipe2)
		Recipe.recipe_inv.append(recipe3)

		LootBox.loot_inv.append(lootbox1)
		Equipment.check_equip_inv()
		LootBox.check_loot_inv()

		print("Hello young chef, welcome to the kitchen!")
		playername = input("To start off, what is your name?: ")

		player = Player(playername, 0, 0, 0, 0)
		player_level_up(player)

		open_lootbox()

		player.player_inventory.append(recipe1)
#		Recipe.recipe_inv.append(recipe1)
#		Recipe.recipe_inv.append(recipe2)
#		Recipe.recipe_inv.append(recipe3)
#		print("\033[33;1mNew recipe gained!!\033[0m")
		player.check_inv()

		cooking_input(player)

		Equipment.check_equip_inv()
		player.check_inv()

		break

def main_menu():
	print("\033[42mWelcome to Cooking Chef!\033[0m")
	print("What would you like to do?")
	print("\nSelect your option:")
	print("1 - Play Game")
	print("2 - Exit Game")
	try:
		menu_input = int(input())
	except ValueError:
		print("Please pick an option from the provided list!")
		return main_menu()
	if menu_input == 1:
		main()
	elif menu_input == 2:
		print("\033[36mThank you for playing!\033[0m")
		exit()
	else:
		print("You have entered an invalid input, please try again!")
		return main_menu()

main_menu()