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

def timer(recipe, equipment, equip_use_select):
	if equip_use_select == True:
		recipe.timer = recipe.timer - equipment.effect
		print(f"{equipment.name} Has been used!")
		equipment.quantity -= 1
		if equipment.quantity <= 0:
			equipment.equip_inv.remove(equipment)

	if recipe.timer < 0:
		recipe.timer = 0

	print(recipe.name, "Has started cooking:", recipe.timer)		
	time.sleep(recipe.timer)
	print(recipe.name, "Has finished cooking, you have gained:", recipe.exp_value, "XP!")
	recipe.quantity -= 1

	if recipe.quantity <= 0:
		recipe.recipe_inv.remove(recipe)

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


def cooking_input(player):
	recipe_list = Recipe.recipe_inv
	equip_list = Equipment.equip_inv

	print("Select the recipe you want to cook")

	for index, recipe in enumerate(recipe_list, 1):
		print(index, f"{recipe.name}")
	try:
		recipe_index = int(input("Select the desired recipe: ")) - 1
	except ValueError:
		print("Incorrect selection, please enter in a correct number within the inventory")
		return cooking_input(player)


	equip_use_select = str(input("Do you want to use an equipment for this recipe? (Y/N): "))

	if equip_use_select.upper() == "Y":
		equip_use_select = True
		if len(equip_list) > 0:
			for index, equip in enumerate(equip_list, 1):
				print(index, f"{equip.name}")
			try:
				equip_select = int(input("Select your equipment: ")) - 1
			except ValueError:
				print("Incorrect selection, please select an item from the list")
				return cooking_input(player)
		elif len(equip_list) <= 0:
			print("You do not have any equipment to select!")
			equip_use_select = False
			equip_select = None
			equipment = None

	elif equip_use_select.upper() == "N":
		equip_use_select = False
		equip_select = None
		equipment = None
	else:
		print("Invalid input, please try again!")
		return cooking_input(player)

	if recipe_index >= 0:
		try:
			recipe = recipe_list[recipe_index]
			if equip_use_select == True:
				if recipe.name == "\033[32mRoasted Potatoes\033[0m" and equip.name == "\033[36;1mExcellent Potato Masher\033[0m":
					equipment = equip_list[equip_select]
				elif recipe.name != "\033[32mRoasted Potatoes\033[0m" and equip.name == "\033[36;1mExcellent Potato Masher\033[0m":
					print("This equipment cannot be used for this recipe!")
					equip_use_select = None
					equip_select = None
					equipment = None
				else: 
					equipment = equip_list[equip_select]
		except IndexError:
			print("Selection is not in your inventory, please select an item from the inventory!")
			recipe = None
			return cooking_input(player)
		timer(recipe, equipment, equip_use_select)
		player.experience += recipe.exp_value
		player_level_up(player)

# game loop
def main():
	while True:
		equip1 = Equipment("\033[32mPotato Spatula\033[0m", "Boosts the cooking speed of all recipes by 5 seconds", 0, 5, 1)
		equip2 = Equipment("\033[32;1mAdvanced Potato Spatula\033[0m", "Boosts the cooking speed of all recipes by 10 seconds", 1, 10, 1)
		equip3 = Equipment("\033[36;1mExcellent Potato Masher\033[0m", "Boosts the cooking speed of Roasted Potatoes by 15 seconds", 5, 15, 1)
		recipe1 = Recipe("\033[32mRoasted Potatoes\033[0m", 100, 0, 15, 1)
		recipe2 = Recipe("\033[32mChicken with Roasted Potatoes\033[0m", 100, 0, 15, 1)
		recipe3 = Recipe("\033[32mMashed Potatoes\033[0m", 100, 0, 5, 1)		
		Equipment.equip_inv.append(equip1)
		Equipment.equip_inv.append(equip2)
		Equipment.equip_inv.append(equip3)
		Equipment.check_equip_inv()

		print("Hello young chef, welcome to the kitchen!")
		time.sleep(1)
		playername = input("To start off, what is your name?: ")

		player = Player(playername, 0, 0, 0, 0)
		player_level_up(player)

		Recipe.recipe_inv.append(recipe1)
		Recipe.recipe_inv.append(recipe2)
		print("\033[33;1mNew recipe gained!!\033[0m")
		time.sleep(1)
		Recipe.check_recipe_inv()

		cooking_input(player)

		Equipment.check_equip_inv()
		Recipe.check_recipe_inv()

		break
main()