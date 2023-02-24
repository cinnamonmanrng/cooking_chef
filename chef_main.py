import time
from chef_skeleton import *
from chef_func import *

equip1 = Equipment("\033[32mPotato Spatula\033[0m", "Boosts the cooking speed of all recipes by 5 seconds", 0, 5, 1, "a107")
equip2 = Equipment("\033[32;1mAdvanced Potato Spatula\033[0m", "Boosts the cooking speed of all recipes by 10 seconds", 1, 10, 1, "b107")
equip3 = Equipment("\033[36;1mExcellent Potato Masher\033[0m", "Boosts the cooking speed of Roasted Potatoes by 15 seconds", 5, 15, 1, "c107")
recipe1 = Recipe("\033[32mRoasted Potatoes\033[0m", 100, 0, 15, 1, "a106")
recipe2 = Recipe("\033[32mChicken with Roasted Potatoes\033[0m", 100, 0, 15, 1, "b106")
recipe3 = Recipe("\033[32mMashed Potatoes\033[0m", 100, 0, 5, 1, "c106")

def main():
	while True:	
		Equipment.equip_inv.append(equip1)
		Equipment.equip_inv.append(equip2)
		Equipment.equip_inv.append(equip3)
		Equipment.check_equip_inv()

		print("Hello young chef, welcome to the kitchen!")
		playername = input("To start off, what is your name?: ")

		player = Player(playername, 0, 0, 0, 0)
		player_level_up(player)

		Recipe.recipe_inv.append(recipe1)
		Recipe.recipe_inv.append(recipe2)
		print("\033[33;1mNew recipe gained!!\033[0m")
		Recipe.check_recipe_inv()

		cooking_input(player)

		Equipment.check_equip_inv()
		Recipe.check_recipe_inv()

		break
main()