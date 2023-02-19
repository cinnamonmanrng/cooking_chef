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

def timer(recipe, equipment):
	recipe_timer = recipe.timer - equipment.effect
	print(f"{equipment.name} Has been used!")
	equipment.quantity -= 1
	equipment.equip_inv.remove(equipment)

	print(recipe.name, "Has started cooking:", recipe_timer)
	time.sleep(recipe_timer)
	print(recipe.name, "Has finished cooking, you have gained:", recipe.exp_value, "XP!")

def player_level_up(player):
	if player.level == 0:
		player.max_xp = 1000
		player.next_level = 1

		if player.experience >= player.max_xp:
			player.level = 1
			player.max_xp = 2500
			player.next_level = 2
			print("\033[33;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()

	elif player.level == 1:
		if player.experience >= player.max_xp:
			player.level = 2
			player.max_xp = 5000
			player.next_level = 3
			print("\033[33;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()

	elif player.level == 2:
		if player.experience >= player.max_xp:
			player.level = 3
			player.max_xp = 10000
			player.next_level = 4
			print("\033[33;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()

	elif player.level == 3:
		if player.experience >= player.max_xp:
			player.level = 4
			player.max_xp = 20000
			player.next_level = 5
			print("\033[33;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()

	elif player.level == 4:
		if player.experience >= player.max_xp:
			player.level = 5
			player.max_xp = "∞"
			player.next_level = "MAX"
			print("\033[33;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()											

# game loop
def main():
	while True:	
		def cooking_input():
			recipe_list = Recipe.recipe_inv
			equip_list = Equipment.equip_inv

			print("Select the recipe you want to cook")

			for recipe in recipe_list:
				print(f"{recipe.name}")
			try:
				recipe_index = int(input("Select the desired recipe: ")) - 1
			except ValueError:
				print("Incorrect selection, please enter in a correct number within the inventory")
				return cooking_input()

			if len(equip_list) > 0:
				for equip in equip_list:
					print(f"{equip.name}")
				try:
					equip_select = int(input("Select your equipment: ")) - 1
				except ValueError:
					print("Incorrect selection, please select an item from the list")
					return cooking_input()

			if recipe_index >= 0:
				try:
					recipe = recipe_list[recipe_index]
					equipment = equip_list[equip_select]
				except IndexError:
					print("Selection is not in your inventory, please select an item from the inventory!")
					recipe = None
					return cooking_input()

				timer(recipe, equipment)
				player.experience += recipe.exp_value
				player_level_up(player)

		equip1 = Equipment("1. \033[32mPotato Spatula\033[0m", "Boosts the cooking speed of all recipes by 5 seconds", 0, 5, 1)
		Equipment.equip_inv.append(equip1)
		Equipment.check_equip_inv()

		recipe1 = Recipe("1. \033[32mRoasted Potatoes\033[0m", 100, 0, 10)
		recipe2 = Recipe("2. \033[32mChicken with Roasted Potatoes\033[0m", 100, 0, 5)
		recipe3 = Recipe("3. \033[32mMashed Potatoes\033[0m", 100, 0, 5)

		print("Hello young chef, welcome to the kitchen!")
		time.sleep(1)
		playername = input("To start off, what is your name?: ")

		player = Player(playername, 0, 0, 0, 0)
		player_level_up(player)

		Recipe.recipe_inv.append(recipe1)
		print("\033[33;1mNew recipe gained!!\033[0m")
		time.sleep(1)
		Recipe.check_recipe_inv()

		cooking_input()	

		Equipment.check_equip_inv()

		break
main()