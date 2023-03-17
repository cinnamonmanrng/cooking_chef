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
import importlib
from inspect import isfunction

def timer(player, recipe, equipment, equip_use_select):
	double_lootbox_chance = 0.25
	if equip_use_select == True:

		if recipe.unique_id != "rec001" or recipe.unique_id != "rec003" and equipment.unique_id == "eq003":
			print("\033[43mThis equipment cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment

		elif recipe.unique_id != "rec006" and equipment.unique_id == "eq006":
			print("\033[43mThis equipment cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment

		elif recipe.unique_id != "rec011" and equipment.unique_id == "eq007":
			print("\033[43mThis equipment cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment

		elif recipe.unique_id != "rec009" and equipment.unique_id == "eq008":
			print("\033[43mThis equipment cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment

		elif recipe.unique_id == "rec009" and equipment.unique_id == "eq008":
			recipe.exp_value += equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)

		elif equipment.unique_id == "eq001" or equipment.unique_id == "eq005":
			recipe.exp_value += equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)

		elif equipment.unique_id == "eq010":
			recipe.quantity += equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)

		else: 
			recipe.timer -= equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)

	if recipe.timer < 0:
		recipe.timer = 0

	print(recipe.name, "Has started cooking:", recipe.timer)		
	time.sleep(recipe.timer)
	print(recipe.name, "Has finished cooking, you have gained:", recipe.exp_value, "XP!")
	player.experience += recipe.exp_value
	recipe.quantity -= 1

	equip_use_select = False

	if recipe.quantity <= 0:
		player.player_inventory.remove(recipe)

	random_lootbox(recipe, player)
	if random.random() < double_lootbox_chance:
		random_lootbox(recipe, player)
	else:
		pass

	unique_id = recipe.unique_id

	def get_recipe(unique_id):
		recipe_id_dict = {
			"rec001": {"timer": 6, "exp_value": 25*6},
			"rec002": {"timer": 5, "exp_value": 25*5},
			"rec003": {"timer": 10, "exp_value": 25*10},
			"rec004": {"timer": 5, "exp_value": 25*5},
			"rec005": {"timer": 12, "exp_value": 25*12},
			"rec006": {"timer": 14, "exp_value": 25*14},
			"rec007": {"timer": 10, "exp_value": 25*10},
			"rec008": {"timer": 18, "exp_value": 25*18},
			"rec009": {"timer": 15, "exp_value": 25*15},
			"rec010": {"timer": 14, "exp_value": 25*14},
			"rec011": {"timer": 20, "exp_value": 25*20},
			"rec012": {"timer": 19, "exp_value": 25*19}
		}

		if unique_id in recipe_id_dict:
			return recipe_id_dict[unique_id]
		else:
			return None

	recipe_check = get_recipe(unique_id)
	if recipe_check is not None:
		recipe.timer = recipe_check["timer"]
		recipe.exp_value = recipe_check["exp_value"]

def open_lootbox(player):

	def add_to_recipe(loot_item):
		print("\033[33;1mNew recipe gained!!\033[0m")
		loot_item.print_info()
		player.player_inventory.append(loot_item)

	def add_to_equip(loot_item):
		print("\033[33;1mNew item gained!!\033[0m")
		loot_item.print_equip_info()
		player.player_equip_inv.append(loot_item)

	loot_list = LootBox.loot_inv

	if len(loot_list) >= 1:
		LootBox.check_loot_inv()
		print("Do you want to open a LootBox™? (Y/N)")
		loot_open_input = input()
		if loot_open_input.upper() == "Y":
				for index, lootbox in enumerate(loot_list, 1):
					print(index, f"{lootbox.name}")
				try:
					select_box = int(input("Select your lootbox: "))
					lootbox = loot_list[select_box-1]
				except ValueError:
					print("Incorrect Selection, please try again")
					return open_lootbox(player)

				lootbox_dict = {
					"lb001": (Recipe.lootbox1_inv),
					"lb002": (Recipe.lootbox1_inv),
					"lb003": (Equipment.equipbox1_inv),
					"lb004": (Equipment.equipbox2_inv),
					"lb005": (Recipe.lootbox2_inv),
					"lb006": (Recipe.lootbox3_inv)
				}
				loot_random_item = lootbox_dict.get(lootbox.unique_id, (None))

				if loot_random_item is None:
					return

				loot_item = loot_random_item[random.randint(0, len(loot_random_item) - 1)]

				if lootbox.unique_id == "lb001" or lootbox.unique_id == "lb002" or lootbox.unique_id == "lb005" or lootbox.unique_id == "lb006":
					add_to_recipe(loot_item)
				elif lootbox.unique_id == "lb003" or lootbox.unique_id == "lb004":
					add_to_equip(loot_item)

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
			print("\033[45;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()

	elif player.level == 1:
		if player.experience >= player.max_xp:
			player.level = 2
			player.max_xp = 5000
			player.next_level = 3
			print("\033[45;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()

	elif player.level == 2:
		if player.experience >= player.max_xp:
			player.level = 3
			player.max_xp = 10000
			player.next_level = 4
			print("\033[45;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()

	elif player.level == 3:
		if player.experience >= player.max_xp:
			player.level = 4
			player.max_xp = 20000
			player.next_level = 5
			print("\033[45;1mYour rating has increased!!\033[0m") 
			player.print_status()
		else:
			player.print_status()

	elif player.level == 4:
		if player.experience >= player.max_xp:
			player.level = 5
			player.max_xp = 40000
			player.next_level = 6
			print("\033[45;1mYour rating has increased!!\033[0m")
			player.print_status()
		else:
			player.print_status()
	elif player.level == 5:
		if player.experience >= player.max_xp:
			player.level = 6
			player.max_xp = 60000
			player.next_level = 7
			print("\033[45;1mYour rating has increased!!\033[0m")	
			player.print_status()
		else:
			player.print_status()
	elif player.level == 6:
		if player.experience >= player.max_xp:
			player.level = 7
			player.max_xp = 90000
			player.next_level = 8
			print("\033[45;1mYour rating has increased!!\033[0m")	
			player.print_status()
		else:
			player.print_status()
	elif player.level == 7:
		if player.experience >= player.max_xp:
			player.level = 8
			player.max_xp = 120000
			player.next_level = 9
			print("\033[45;1mYour rating has increased!!\033[0m")	
			player.print_status()
		else:
			player.print_status()
	elif player.level == 8:
		if player.experience >= player.max_xp:
			player.level = 9
			player.max_xp = 175000
			player.next_level = 10
			print("\033[45;1mYour rating has increased!!\033[0m")	
			player.print_status()
		else:
			player.print_status()
	elif player.level == 9:
		if player.experience >= player.max_xp:
			player.level = 10
			player.max_xp = "MAX"
			player.next_level = "MAX"
			print("\033[45;1mYour rating has increased!!\033[0m")	
			player.print_status()
		else:
			player.print_status()
	elif player.level == 10:
		player.max_xp = "MAX"
		player.next_level = "MAX"
		player.print_status_maxlvl()

def add_to_loot(boxluck, boxluck_eq):
	print("\033[33;1mNew LootBox™ gained!!\033[0m")
	boxluck[0].loot_print_info()
	beq = boxluck[0]
	LootBox.loot_inv.append(beq)
	if len(boxluck_eq) > 0:
		print("\033[33;1mNew LootBox™ gained!!\033[0m")
		boxluck_eq[0].loot_print_info()
		beq_eq = boxluck_eq[0]
		LootBox.loot_inv.append(beq_eq)
	boxluck = None
	boxluck_eq = None

def random_lootbox(recipe, player):
	random_loot_boxes = {
		0: (LootBox.random_loot_inv1, LootBox.random_looteq_inv1),
		1: (LootBox.random_loot_inv1, LootBox.random_looteq_inv2),
		2: (LootBox.random_loot_inv2, LootBox.random_looteq_inv2),
		3: (LootBox.random_loot_inv3, LootBox.random_looteq_inv3),
		4: (LootBox.random_loot_inv4, LootBox.random_looteq_inv4),
		5: (LootBox.random_loot_inv5, LootBox.random_looteq_inv5)
	}

	random_box, random_box_eq = random_loot_boxes.get(recipe.quality, (None, None))

	if random_box is None or random_box_eq is None:
		return

	boxluck = [random_box[random.randint(0, len(random_box) - 1)]]

	if random.random() < 0.50:
		boxluck_eq = [random_box_eq[random.randint(0, len(random_box_eq) - 1)]]
	else:
		boxluck_eq = []

	if recipe.quality == 5 and random.random() < 0.41:
		random_box = LootBox.random_loot_inv6
		random_box_eq = LootBox.random_looteq_inv6
		boxluck = [random_box[random.randint(0, len(random_box) - 1)]]
		if random.random() < 0.50:
			boxluck_eq = [random_box_eq[random.randint(0, len(random_box_eq) - 1)]]
		else:
			boxluck_eq = []

	add_to_loot(boxluck, boxluck_eq)
	


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

	equip_use_select = str(input("Do you want to use an item for this recipe? (Y/N): "))

	if equip_use_select.upper() == "Y":
		equip_use_select = True
		if len(equip_list) > 0:
			for index, equip in enumerate(equip_list, 1):
				print(index, f"{equip.name}")
			try:
				equip_select = int(input("Select your item: ")) - 1
			except ValueError:
				print("Incorrect selection, please select an item from the list")
				return cooking_input(player)
		elif len(equip_list) <= 0:
			print("You do not have any items to select!")
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
		player_level_up(player)

def save_game(player):

	chef = player.name, player.level, player.experience, player.max_xp, player.next_level, player.player_inventory, player.player_equip_inv, LootBox.loot_inv

	file_name = "chef_1.pkl"
	if os.path.exists(file_name):
		print("\033[43mSave file in slot 1 already exists!\033[0m")

		print("1 - Overwrite Slot 1")
		print("2 - Save in a different slot")
		save_input = int(input("Do you want to overwrite save slot 1 or save in a different slot?: "))


		if save_input == 1:
			with open(file_name, "wb") as file:
				pickle.dump(chef, file)				
				print("\033[42mFile saved successfully to slot 1\033[0m")
		elif save_input == 2:
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
				print("\033[43mGame not saved!!\033[0m")
				pass
		else:
			print("Invalid input, please try again!")
			return save_game(player)

	elif not os.path.exists(file_name):
		ask_to_save = input("Do you want to save your game to slot 1? (Y/N): ")
		if ask_to_save.upper() == "Y":
			with open(file_name, "wb") as file:
				pickle.dump(chef, file)
				print("\033[42mFile saved successfully to slot 1\033[0m")
		elif ask_to_save.upper() == "N":
			print("\033[43mPlayer data not saved!\033[0m")
			pass
def call_func(full_module_name, func_name, *argv):
	module = importlib.import_module(full_module_name)
	for attribute_name in dir(module):
		attribute = getattr(moduel, attribute_name)
		if isfunction(attribute) and attribute_name == func_name:
			attribute(*argv)

def load_game(player):
	if not os.path.exists("chef_1.pkl"):
		print("1 - Save Slot 1 - Empty")

	if os.path.exists("chef_1.pkl"):
		with open("chef_1.pkl", "rb") as menufile:
			load1 = pickle.load(menufile)
			load1_list = list(load1)
			player.name, player.level, player.experience = load1[:3]
			print("1 - Save Slot 1 - " + f"{player.name} " + f"| Rating: {player.get_load_star()} " + "| XP: " + f"{player.experience}")
			menufile.close()

	if not os.path.exists("chef_2.pkl"):
		print("2 - Save Slot 2 - Empty")

	if os.path.exists("chef_2.pkl"):
		with open("chef_2.pkl", "rb") as menufile:
			load2 = pickle.load(menufile)
			load2_list = list(load2)
			player.name, player.level, player.experience = load2[:3]
			print("2 - Save Slot 2 - " + f"{player.name} " + f"| Rating: {player.get_load_star()} " + "| XP: " + f"{player.experience}")
			menufile.close()

	if not os.path.exists("chef_3.pkl"):
		print("3 - Save Slot 3 - Empty")

	if os.path.exists("chef_3.pkl"):
		with open("chef_3.pkl", "rb") as menufile:
			load3 = pickle.load(menufile)
			load3_list = list(load3)
			player.name, player.level, player.experience = load3[:3]
			print("3 - Save Slot 3 - " + f"{player.name} " + f"| Rating: {player.get_load_star()} " + "| XP: " + f"{player.experience}")
			menufile.close()

	print("4 - Go back")
	print("5 - Delete a save file")
	ask_save_load = int(input("Choose your option: "))

	if ask_save_load == 1:
		if os.path.exists("chef_1.pkl"):
			with open("chef_1.pkl", "rb") as file:
				import1 = pickle.load(file)
				import1_list = list(import1)
				player.name, player.level, player.experience, player.max_xp, player.next_level = import1[:5]
				recipes = import1[5]
				equipments = import1[6]
				lootboxes = import1[7]
				player.player_inventory = recipes
				player.player_equip_inv = equipments
				LootBox.loot_inv = lootboxes
			print("Save slot 1 loaded successfully!")
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 2:
		if os.path.exists("chef_2.pkl"):
			with open("chef_2.pkl", "rb") as file:
				import2 = pickle.load(file)
				import2_list = list(import2)
				player.name, player.level, player.experience, player.max_xp, player.next_level = import2[:5]
				recipes = import2[5]
				equipments = import2[6]
				lootboxes = import2[7]
				player.player_inventory = recipes
				player.player_equip_inv = equipments
				LootBox.loot_inv = lootboxes
			print("Save slot 2 loaded successfully!")
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 3:
		if os.path.exists("chef_3.pkl"):
			with open("chef_3.pkl", "rb") as file:
				import3 = pickle.load(file)
				import3_list = list(import3)
				player.name, player.level, player.experience, player.max_xp, player.next_level = import3[:5]
				recipes = import3[5]
				equipments = import3[6]
				lootboxes = import3[7]
				player.player_inventory = recipes
				player.player_equip_inv = equipments
				LootBox.loot_inv = lootboxes
			print("Save slot 3 loaded successfully!")				
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 4:
		call_func('chef_main', 'main_menu', None)
	elif ask_save_load == 5:
		print("1 - Remove save in slot 1")
		print("2 - Remove save in slot 2")
		print("3 - Remove save in slot 3")
		print("4 - Go back")
		delete_save_inp = int(input("Choose your option: "))

		if delete_save_inp == 1:
			if os.path.exists("chef_1.pkl"):
				os.remove("chef_1.pkl")
				print("\033[43mSave file in slot 1 has been removed successfully!\033[0m")
				return load_game(player)
			elif not os.path.exists("chef_1.pkl"):
				print("\033[43mSave slot 1 is empty!")
				return load_game(player)
		elif delete_save_inp == 2:
			if os.path.exists("chef_2.pkl"):
				os.remove("chef_2.pkl")
				print("\033[43mSave file in slot 2 has been removed successfully!\033[0m")
				return load_game(player)
			elif not os.path.exists("chef_2.pkl"):
				print("\033[43mSave slot 2 is empty!")
				return load_game(player)
		elif delete_save_inp == 3:
			if os.path.exists("chef_3.pkl"):
				os.remove("chef_3.pkl")
				print("\033[43mSave file in slot 3 has been removed successfully!\033[0m")
				return load_game(player)
			elif not os.path.exists("chef_3.pkl"):
				print("\033[43mSave slot 3 is empty!")
				return load_game(player)
		elif delete_save_inp == 4:
			return load_game(player)