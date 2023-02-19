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

def timer(recipe_list, recipe):
	print(recipe.name, "Has started cooking:", recipe.timer)
	time.sleep(recipe.timer)
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
		recipe1 = Recipe("1. \033[32mRoasted Potatoes\033[0m", 1000, 0, 5)
		recipe2 = Recipe("2. \033[32;1mChicken with Roasted Potatoes\033[0m", 1500, 1, 5)
		recipe3 = Recipe("3. \033[35mMashed Potatoes\033[0m", 3000, 3, 5)

		print("Hello young chef, welcome to the kitchen!")
		time.sleep(1)
		playername = input("To start off, what is your name?: ")

		player = Player(playername, 0, 0, 0, 0)
		player_level_up(player)

		time.sleep(1)

		print("To become a true master of the cooking arts, you will need to learn some recipes")
		time.sleep(1.7)
		print("How about I teach you one right now!")
		time.sleep(1)

		Recipe.recipe_inv.append(recipe1)
		print("\033[33;1mNew recipe gained!!\033[0m")
		time.sleep(1)
		Recipe.check_recipe_inv()

		def tutorial_cooking_input():
			recipe_list = Recipe.recipe_inv

			print("Select the recipe you want to cook")

			for recipe in recipe_list:
				print(f"{recipe.name}")

			recipe_index = int(input("Select the desired recipe: ")) - 1

			if recipe_index >= 0:
				recipe = recipe_list[recipe_index]
				timer(recipe_list, recipe)
				player.experience += recipe.exp_value
				player_level_up(player)
			else:
				print("Invalid entry, please enter a number starting from 0")	

		print("Let's start off by practicing your cooking skills")
		time.sleep(1)
		print("So first you will want to select the option to cook, which I will give you now")
		tutorial_cooking_input()

		time.sleep(1)

		print("Congratulations on cooking your first meal!")
		time.sleep(1)
		print("You have now earned another recipe! use this knowledge wisely")
		Recipe.recipe_inv.append(recipe2)
		print("\033[33;1mNew recipe gained!!\033[0m")
		time.sleep(1)		
		Recipe.check_recipe_inv()
		time.sleep(1)

		print("How about we cook another recipe?")
		time.sleep(1)
		tutorial_cooking_input()
		time.sleep(1)
		Recipe.recipe_inv.append(recipe3)
		print("\033[33;1mNew recipe gained!!\033[0m")
		time.sleep(1)
		Recipe.check_recipe_inv()

		break
main()