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
import random

def timer(recipe_list, recipe):
	print(recipe.name, "Has started cooking:", recipe.timer)
	time.sleep(recipe.timer)
	print(recipe.name, "Has finished cooking, you have gained:", recipe.exp_value, "XP!")

def level_up_1(player):
	if player.level == 0:
		if player.experience >= player.max_xp:
			player.level = 1
			player.max_xp = 2500
			player.next_level = 2
			print("\033[33;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()

def level_up_2(player):
	if player.level == 1:
		if player.experience >= player.max_xp:
			player.level = 2
			player.max_xp = 5000
			player.next_level = 3

def level_up_3(player):
	if player.level == 2:
		if player.experience >= player.max_xp:
			player.level = 3
			player.max_xp = 10000
			player.next_level = 4

def level_up_4(player):
	if player.level == 3:
		if player.experience >= player.max_xp:
			player.level = 4
			player.max_xp = 20000
			player.next_level = 5

def level_up_5(player):
	if player.level == 4:
		if player.experience >= player.max_xp:
			player.level = 5
			player.max_xp = "MAX"
			player.next_level = "MAX"
		

# game loop
def main():
	while True:	
		recipe1 = Recipe("1. \033[32mRoasted Potatoes\033[0m", 30, 0, 5)
		recipe2 = Recipe("2. \033[32mChicken with Roasted Potatoes\033[0m", 45, 0, 150)
		recipe3 = Recipe("3. \033[32mMashed Potatoes\033[0m", 20, 0, 100)

		print("Hello young chef, welcome to the kitchen!")
		time.sleep(1)
		playername = input("To start off, what is your name?: ")

		player = Player(playername, 0, 0, 1000, 1)

		print("\n")
		player.print_status()
		print("\n")
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
				print(recipe.name)

			recipe_index = int(input("Select the desired recipe: ")) - 1

			if recipe_index >= 0:
				recipe = recipe_list[recipe_index]
				timer(recipe_list, recipe)
				player.experience += recipe.exp_value
				level_up_1(player)
			else:
				print("Invalid entry, please enter a number starting from 0")	

		print("Let's start off by practicing your cooking skills")
		time.sleep(1)
		print("So first you will want to select the option to cook, which I will give you now")
		tutorial_cooking_input()

		break
main()