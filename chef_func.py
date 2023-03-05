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
		player.player_inventory.remove(recipe)

def open_lootbox():
	loot_list = LootBox.loot_inv

	if len(loot_list) >= 1:
		LootBox.check_loot_inv()
		print("Do you want to open a LootBox™? (Y/N)")
		loot_open_input = input()
		if loot_open_input.upper() == "Y":
				for index, lootbox in enumerate(loot_list, 1):
					print(index, f"{lootbox.name}")
				try:
					select_box = int(input("Select your lootbox: ")) - 1
				except ValueError:
					print("Incorrect Selection, please try again")
					return open_lootbox()
				lootbox.loot_open()
				lootbox.quantity -= 1
				if lootbox.quantity <= 0:
					lootbox.loot_inv.remove(lootbox)
		elif loot_open_input.upper() == "N":
			print("\033[43mLootBox™ not opened!\033[0m")
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
	recipe_list = player.player_inventory
	equip_list = player.player_equip_inv

	print("Select the recipe you want to cook")

	for index, recipe in enumerate(recipe_list, 1):
		print(index, f"{recipe.name}")

	if len(recipe_list) <= 0:
		print("\033[43mYou have no recipes in your inventory to cook!\033[0m")
		return
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

	chef = player.name, player.level, player.experience, player.max_xp, player.next_level, player.player_inventory, player.player_equip_inv, LootBox.loot_inv

	file_name = "chef_1.pkl"
	if os.path.exists(file_name):
		print("\033[43mSave file in slot 1 already exists!\033[0m")

		save_input = input("Do you want to overwrite save slot 1? (Y/N): ")

		if save_input.upper() == "Y":
			with open(file_name, "wb") as file:
				pickle.dump(chef, file)				
				print("\033[42mFile saved successfully to slot 1\033[0m")
		elif save_input.upper() == "N":
			print("1. Save Slot 2")
			print("2. Save Slot 3")
			print("3. Leave without saving")
			try:
				new_save_input = int(input("Choose your save file slot: ")) - 1
			except ValueError:
				print("Incorrect value, please try again!")
				return save_game(player)

			if new_save_input == 0:
				if os.path.exists("chef_2.pkl"):
					print("\033[43mSave file in slot 2 already exists!\033[0m")
					overwrite_2 = input("Do you want to overwrite the save in slot 2? (Y/N): ")
					if overwrite_2.upper() == "Y":
						with open("chef_2.pkl", "wb") as file:
							pickle.dump(chef, file)					
							print("\033[42mGame saved successfully to slot 2\033[0m")
					elif overwrite_2.upper() == "N":
						print("\033[43mSave slot 2 not overwritten!\033[0m")
						return save_game(player)
					else:
						print("Invalid selection, please try again!")
						return save_game(player)
				elif not os.path.exists("chef_2.pkl"):
					with open("chef_2.pkl", "wb") as file:
						pickle.dump(chef, file)
						print("\033[42mGame saved successfully to slot 2\033[0m")	

			elif new_save_input == 1:
				if os.path.exists("chef_3.pkl"):
					print("\033[43mSave file in slot 3 already exists!\033[0m")
					overwrite_3 = input("Do you want to overwrite the save in slot 3? (Y/N): ")
					if overwrite_3.upper() == "Y":
						with open("chef_3.pkl", "wb") as file:
							pickle.dump(chef, file)				
							print("\033[42mGame saved successfully to slot 3\033[0m")
					elif overwrite_3.upper() == "N":
						print("\033[43mSave slot 3 not overwritten!\033[0m")
						return save_game(player)
					else:
						print("Invalid selection, please try again!")
						return save_game(player)
				elif not os.path.exists("chef_3.pkl"):
					with open("chef_3.pkl", "wb") as file:
						pickle.dump(chef, file)
						print("\033[42mGame saved successfully to slot 3\033[0m")	

			elif new_save_input == 2:
				print("\033[43mGame exited without saving!\033[0m")
				print("\033[36mThank you for playing!\033[0m")
				exit()
		else:
			print("Invalid input, please try again!")
			return save_game(player)

	elif not os.path.exists(file_name):
		ask_to_save = input("Do you want to save your game to slot 1? (Y/N): ")
		if ask_to_save.upper() == "Y":
			with open(file_name, "wb") as file:
				pickle.dump(chef, file)
				print("File saved successfully to slot 1")
		elif ask_to_save.upper() == "N":
			print("\033[43mPlayer data not saved!\033[0m")
			pass

def load_game(player):
	print("1 - Save Slot 1")
	print("2 - Save Slot 2")
	print("3 - Save Slot 3")
	print("4 - Go back") # list names and rating
	print("5 - Delete a save file")
	ask_save_load = int(input("Which save slot do you want to open?: "))

	if ask_save_load == 1:
		if os.path.exists("chef_1.pkl"):
			with open("chef_1.pkl", "rb") as file:
				import1 = pickle.load(file)
				import1_list = list(import1)
				player.name, player.level, player.experience, player.max_xp, player.next_level = import1[:5]
				recipes = import1[5]
				equipments = import1[6]
				lootboxes = import1[7]
				print(recipes + equipments + lootboxes)
				player.player_inventory = recipes
				player.player_equip_inv = equipments
				LootBox.loot_inv = lootboxes
				print(import1) # remove this after development
			print("Save slot 1 loaded successfully!")
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 2:
		if os.path.exists("chef_2.pkl"):
			with open("chef_2.pkl", "rb") as file:
				import2 = pickle.load(file)
				player.name, player.level, player.experience, player.max_xp, player.next_level, player.player_inventory, player.player_equip_inv, LootBox.loot_inv = import2
				print(import2) # remove this after development
			print("Save slot 2 loaded successfully!")
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 3:
		if os.path.exists("chef_3.pkl"):
			with open("chef_3.pkl", "rb") as file:
				import3 = pickle.load(file)
				player.name, player.level, player.experience, player.max_xp, player.next_level, player.player_inventory, player.player_equip_inv, LootBox.loot_inv = import3
				print(import3) # remove this after development
			print("Save slot 3 loaded successfully!")				
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 4:
		return # maybe use os.path.exists for this?