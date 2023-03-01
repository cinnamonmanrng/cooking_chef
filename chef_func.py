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
import os
import pickle

def timer(player, recipe, equipment, equip_use_select):
	if equip_use_select == True:
		if recipe.unique_id != "a106" and equipment.unique_id == "c107":
			print("This equipment cannot be used for this recipe!")
			equip_use_select = False
			equipment = None
		else:
			recipe.timer = recipe.timer - equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)

	if recipe.timer < 0:
		recipe.timer = 0

	print(recipe.name, "Has started cooking:", recipe.timer)		
	time.sleep(recipe.timer)
	print(recipe.name, "Has finished cooking, you have gained:", recipe.exp_value, "XP!")
	recipe.quantity -= 1

	if recipe.quantity <= 0:
		Player.player_inventory.remove(recipe)

def open_lootbox():
	loot_list = LootBox.loot_inv

	if len(LootBox.loot_inv) <= 1:
		print("Do you want to open a LootBox™? (Y/N)")
		loot_open_input = input()
		if loot_open_input.upper() == "Y":
			for index, lootbox in enumerate(loot_list, 1):
				print(index, f"{lootbox.name}")
				select_box = input("Select your lootbox: ")
				lootbox.loot_open()
				lootbox.quantity -= 1
				lootbox.loot_inv.remove(lootbox)
		elif loot_open_input.upper() == "N":
			pass
		else:
			print("Invalid input, Please try again!")

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
			player.max_xp = 40000
			player.next_level = 6
			print("\033[33;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()
	elif player.level == 5:
		if player.experience >= player.max_xp:
			player.level = 6
			player.max_xp = 60000
			player.next_level = 7
			print("\033[33;1mYour rating has increased!!\033[0m")	
			player.print_status()
		else:
			player.print_status()
	elif player.level == 6:
		if player.experience >= player.max_xp:
			player.level = 7
			player.max_xp = 80000
			player.next_level = 8
			print("\033[33;1mYour rating has increased!!\033[0m")	
			player.print_status()
		else:
			player.print_status()
	elif player.level == 7:
		if player.experience >= player.max_xp:
			player.level = 8
			player.max_xp = 100000
			player.next_level = 9
			print("\033[33;1mYour rating has increased!!\033[0m")	
			player.print_status()
		else:
			player.print_status()
	elif player.level == 8:
		if player.experience >= player.max_xp:
			player.level = 9
			player.max_xp = 150000
			player.next_level = 10
			print("\033[33;1mYour rating has increased!!\033[0m")	
			player.print_status()
		else:
			player.print_status()
	elif player.level == 9:
		if player.experience >= player.max_xp:
			player.level = 10
			player.max_xp = "MAX"
			player.next_level = "MAX"
			print("\033[33;1mYour rating has increased!!\033[0m")	
			player.print_status()
#			equip4 = Equipment("\033[36;1mMythical Chef's Hat\033[0m", "Boosts cooking speed of all recipes by 35 seconds", 5, 35, 200, "put id here")
#			Equipment.equip_inv.append(equip4)
#			equip4.print_equip_info()
		else:
			player.print_status()
	elif player.level == 10:
		player.max_xp = "MAX"
		player.next_level = "MAX"
		player.print_status()

def cooking_input(player):
	recipe_list = Player.player_inventory
	equip_list = Player.player_equip_inv

	print("Select the recipe you want to cook")

	for index, recipe in enumerate(recipe_list, 1):
		print(index, f"{recipe.name}")

	if len(recipe_list) <= 0:
		print("You have no recipes in your inventory to cook!")
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
				equipment = equip_list[equip_select]
		except IndexError:
			print("Selection is not in your inventory, please select an item from the inventory!")
			recipe = None
			return cooking_input(player)
		timer(player, recipe, equipment, equip_use_select)
		player.experience += recipe.exp_value
		player_level_up(player)

def save_game(player):

	chef_1 = player.name, player.level, player.experience, player.max_xp, player.next_level, player.player_inventory, player.player_equip_inv, LootBox.loot_inv

	file_name = "chef_1.pkl"
	if os.path.exists(file_name):
		print("Save file already exists!")

		save_input = input("Do you want to overwrite save slot 1? (Y/N): ")

		if save_input.upper() == "Y":
			with open(file_name, "wb") as file:
				pickle.dump(chef_1, file)				
				print("File saved successfully to slot 1")
		elif save_input.upper() == "N":
			print("1. Save Slot 2")
			print("2. Save Slot 3")
			try:
				new_save_input = int(input("Choose your save file slot: ")) - 1
			except ValueError:
				print("Incorrect value, please try again!")
				return save_game(player)

			if new_save_input == 0:
				with open("chef_2.pkl", "wb") as file:
					pickle.dump(chef_1, file)					
					print("File saved successfully to slot 2")
			elif new_save_input == 1:
				with open("chef_3.pkl", "wb") as file:
					pickle.dump(chef_1, file)				
					print("File saved successfully to slot 3")					

		else:
			print("Invalid input, please try again!")
			return save_game(player)

	elif not os.path.exists(file_name):
		with open(file_name, "wb") as file:
			pickle.dump(chef_1, file)
			print("File saved successfully to slot 1")

def load_game(player):
	print("1 - Save Slot 1")
	print("2 - Save Slot 2")
	print("3 - Save Slot 3")
	print("4 - Continue without loading")
	ask_save_load = int(input("Which save slot do you want to open?: "))

	if ask_save_load == 1:
		if os.path.exists("chef_1.pkl"):
			with open("chef_1.pkl", "rb") as file:
				import1 = pickle.load(file)
				player.name, player.level, player.experience, player.max_xp, player.next_level, player.player_inventory, player.player_equip_inv, LootBox.loot_inv = import1
			print("Save slot 1 loaded successfully!")
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 2:
		if os.path.exists("chef_2.pkl"):
			with open("chef_2.pkl", "rb") as file:
				import2 = pickle.load(file)
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 3:
		if os.path.exists("chef_3.pkl"):
			with open("chef_3.pkl", "rb") as file:
				import3 = pickle.load(file)
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 4:
		pass