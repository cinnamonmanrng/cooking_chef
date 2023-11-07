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
from chef_call_list import *
import os
import pickle
import importlib
from inspect import isfunction
import logging
from logging.handlers import RotatingFileHandler

logging_enabled = True # starts with logging enabled, used for option to turn off logging in later statements.

def toggle_logging(enable=True): # controls enabling and disabling the logging mechanic
	global logging_enabled
	logging_enabled = enable

def logging_setup():
	log_file = os.path.join("Logs", "chefgame.log")

	handler = RotatingFileHandler(log_file, maxBytes=500 * 1024, backupCount=2)

	logging.basicConfig(
			level=logging.INFO,
			format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
			handlers=[handler]
		)

def log_message(message, level=logging.INFO): # function that can be called to create a log message in the specified file
	if logging_enabled:
		logging.log(level, message)

toggle_logging()
logging_setup()
log_message("Logging initalised - GameVer=24.1", level=logging.INFO)

def progress_bar(recipe):
	for i in range(1, recipe.timer + 1):
		time.sleep(1)
		print(f"\r{i:02d}/{recipe.timer:02d}: {'๑'*(i)}", end="", flush=True)

def call_func(full_module_name, func_name, *argv):
	module = importlib.import_module(full_module_name)
	for attribute_name in dir(module):
		attribute = getattr(module, attribute_name)
		if isfunction(attribute) and attribute_name == func_name:
			attribute(*argv)

def timer(player, recipe, equipment, equip_use_select):
	double_lootbox_chance = 0.25

	# special recipe cooking
	if recipe.unique_id != "rec010":
		pass
	elif recipe.unique_id == "rec010" and player.meatballs_cooked < 1 or player.spaghetti_cooked < 1 or player.tomatosauce_cooked < 1:
		print("You do not have the right ingredients to cook this recipe, please cook the required recipes before cooking this one!")
		return
	elif recipe.unique_id == "rec010" and player.meatballs_cooked >= 1 and player.spaghetti_cooked >= 1 and player.tomatosauce_cooked >= 1:
		player.meatballs_cooked -= 1
		player.spaghetti_cooked -= 1
		player.tomatosauce_cooked -= 1
		pass

	if equip_use_select == True:

# items with individual recipe requirements (refers to chef_call_list)

		if recipe.unique_id == "rec001" and equipment.unique_id == "eq003":
			recipe.timer -= equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)
		elif recipe.unique_id == "rec003" and equipment.unique_id == "eq003":
			recipe.timer -= equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)
		elif recipe.unique_id != "rec001" and equipment.unique_id == "eq003":
			print("\033[43mThis Item cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment
		elif recipe.unique_id != "rec003" and equipment.unique_id == "eq003": 
			print("\033[43mThis Item cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment

		if recipe.unique_id == "rec012" and equipment.unique_id == "eq004":
			recipe.timer -= equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)
		elif recipe.unique_id != "rec012" and equipment.unique_id == "eq004":
			print("\033[43mThis Item cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment


		if recipe.unique_id == "rec030" and equipment.unique_id == "eq011":
			recipe.timer -= equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)
		elif recipe.unique_id == "rec030" and equipment.unique_id == "eq011":
			print("\033[43mThis Item cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment

		if recipe.unique_id == "rec031" and equipment.unique_id == "eq012":
			recipe.timer -= equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)
		elif recipe.unique_id == "rec034" and equipment.unique_id == "eq012":
			recipe.timer -= equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)
		elif recipe.unique_id == "rec031" and equipment.unique_id == "eq012":
			print("\033[43mThis Item cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment
		elif recipe.unique_id == "rec034" and equipment.unique_id == "eq012":
			print("\033[43mThis Item cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment

		if recipe.unique_id == "rec032" and equipment.unique_id == "eq015":
			recipe.timer -= equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)
		elif recipe.unique_id == "rec032" and equipment.unique_id == "eq015":
			print("\033[43mThis Item cannot be used for this recipe!\033[0m")
			equip_use_select = False
			equipment = None
			return equip_use_select, equipment

# general items (work with any recipe)

		if equipment.unique_id == "eq002" or equipment.unique_id == "eq005" or equipment.unique_id == "eq009" or equipment.unique_id == "eq013" or equipment.unique_id == "eq017":
			recipe.timer -= equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)

		if equipment.unique_id == "eq001" or equipment.unique_id == "eq006" or equipment.unique_id == "eq008" or equipment.unique_id == "eq010" or equipment.unique_id == "eq014" or equipment.unique_id == "eq016":
			recipe.exp_value += equipment.effect
			print(f"{equipment.name} Has been used!")
			equipment.quantity -= 1
			if equipment.quantity <= 0:
				player.player_equip_inv.remove(equipment)

		if equipment.unique_id == "eq007":
			if random.random() < 0.50:
				recipe.timer -= equipment.effect
				print(f"{equipment.name} Has been used and timer has been decreased!")
				equipment.quantity -= 1
				if equipment.quantity <= 0:
					player.player_equip_inv.remove(equipment)
			else:
				recipe.timer += equipment.effect
				print(f"{equipment.name} Has been used and timer has been increased!")
				equipment.quantity -= 1
				if equipment.quantity <= 0:
					player.player_equip_inv.remove(equipment)

	if recipe.timer < 0:
		recipe.timer = 0

	def multiple_recipe_cooks():
		# spaghetti and meatballs in tomato sauce (rec010)
		if recipe.unique_id == "rec005":
			player.meatballs_cooked += 1
		else:
			player.meatballs_cooked += 0
		if recipe.unique_id == "rec008":
			player.tomatosauce_cooked += 1
		else:
			player.tomatosauce_cooked += 0
		if recipe.unique_id == "rec009":
			player.spaghetti_cooked += 1
		else:
			player.spaghetti_cooked += 0

	print(recipe.name, "Has started cooking:", recipe.timer)
	log_message(f"Player cooking {recipe.name} for {recipe.timer}", level=logging.INFO)		
	progress_bar(recipe)
	print("\n", recipe.name, "Has finished cooking, you have gained:", recipe.exp_value, "XP!")
	log_message(f"Player cooked {recipe.name} and got {recipe.exp_value}", level=logging.INFO)
	player.experience += recipe.exp_value
	recipe.quantity -= 1

	multiple_recipe_cooks()

	equip_use_select = False
	log_message("equip_use_select was reset", level=logging.INFO)

	if recipe.quantity <= 0:
		player.player_inventory.remove(recipe)
		log_message(f"{recipe} removed from player", level=logging.INFO)

	random_lootbox(recipe, player)
	if random.random() < double_lootbox_chance:
		random_lootbox(recipe, player)
		log_message("Player got double_lootbox_chance", level=logging.INFO)
	else:
		pass

	unique_id = recipe.unique_id

	def get_recipe(unique_id):
		recipe_id_dict = {
			"rec001": {"timer": 6, "exp_value": 25*6},
			"rec002": {"timer": 5, "exp_value": 25*5},
			"rec003": {"timer": 10, "exp_value": 25*10},
			"rec004": {"timer": 5, "exp_value": 25*5},
			"rec005": {"timer": 9, "exp_value": 25*9},
			"rec006": {"timer": 10, "exp_value": 25*10},
			"rec007": {"timer": 5, "exp_value": 25*5},
			"rec008": {"timer": 7, "exp_value": 25*7},
			"rec009": {"timer": 8, "exp_value": 25*8},
			"rec010": {"timer": 20, "exp_value": 40*20},
			"rec011": {"timer": 12, "exp_value": 25*12},
			"rec012": {"timer": 10, "exp_value": 25*10},
			"rec013": {"timer": 3, "exp_value": 25*3},
			"rec014": {"timer": 6, "exp_value": 25*6},
			"rec015": {"timer": 9, "exp_value": 25*9},
			"rec016": {"timer": 13, "exp_value": 35*13},
			"rec017": {"timer": 15, "exp_value": 35*15},
			"rec018": {"timer": 14, "exp_value": 35*14},
			"rec019": {"timer": 18, "exp_value": 35*18},
			"rec020": {"timer": 12, "exp_value": 35*12},
			"rec021": {"timer": 16, "exp_value": 35*16},
			"rec022": {"timer": 20, "exp_value": 35*20},
			"rec023": {"timer": 12, "exp_value": 35*12},
			"rec024": {"timer": 17, "exp_value": 35*17},
			"rec025": {"timer": 15, "exp_value": 35*15},
			"rec026": {"timer": 8, "exp_value": 25*8},
			"rec027": {"timer": 7, "exp_value": 25*7},
			"rec028": {"timer": 4, "exp_value": 25*4},
			"rec029": {"timer": 10, "exp_value": 35*10},
			"rec030": {"timer": 9, "exp_value": 35*9},
			"rec031": {"timer": 13, "exp_value": 35*13},
			"rec032": {"timer": 20, "exp_value": 50*20},
			"rec033": {"timer": 15, "exp_value": 50*15},
			"rec034": {"timer": 30, "exp_value": 50*30}
		}

		if unique_id in recipe_id_dict:
			return recipe_id_dict[unique_id]
		else:
			return None

		log_message("Recipe ID got", level=logging.INFO)

	recipe_check = get_recipe(unique_id)
	if recipe_check is not None:
		recipe.timer = recipe_check["timer"]
		recipe.exp_value = recipe_check["exp_value"]

def open_lootbox(player):

	def add_to_recipe(loot_item):
		print("\033[33;1mNew recipe gained!!\033[0m")
		loot_item.print_info()
		player.player_inventory.append(loot_item)
		log_message(f"Player got recipe: {loot_item}", level=logging.INFO)

	def add_to_equip(loot_item):
		print("\033[33;1mNew item gained!!\033[0m")
		loot_item.print_equip_info()
		player.player_equip_inv.append(loot_item)
		log_message(f"Player got item: {loot_item}", level=logging.INFO)

	loot_list = LootBox.loot_inv

	if len(loot_list) >= 1:
		LootBox.check_loot_inv()
		print("Do you want to open a LootBox™? (Y/N)")
		loot_open_input = input()
		if loot_open_input.upper() == "Y":
				for index, lootbox in enumerate(loot_list, 1):
					print(index, f"{lootbox.name}")
					log_message("Lootbox menu init", level=logging.INFO)
				try:
					select_box = int(input("Select your lootbox: "))
					lootbox = loot_list[select_box-1]
				except ValueError as error:
					print("Incorrect Selection, please try again")
					log_message("Player selected invalid value in loot_open_input", level=logging.INFO)
					return open_lootbox(player)
				except IndexError as error:
					print("Incorrect Selection, please try again")
					log_message("Player caused IndexError in loot_open_input", level=logging.INFO)
					return open_lootbox(player)

				lootbox_dict = {
					"lb001": (Recipe.lootbox1_inv),
					"lb002": (Recipe.lootbox1_1_inv),
					"lb003": (Equipment.equipbox1_inv),
					"lb004": (Recipe.lootbox1_2_inv),
					"lb005": (Recipe.lootbox1_3_inv),
					"lb006": (Recipe.lootbox2_inv),
					"lb007": (Equipment.equipbox2_inv),
					"lb008": (Recipe.lootbox2_1_inv),
					"lb009": (Recipe.lootbox3_inv),
					"lb010": (Equipment.equipbox3_inv)
				}
				loot_random_item = lootbox_dict.get(lootbox.unique_id, (None))

				if loot_random_item is None:
					return

				loot_item = loot_random_item[random.randint(0, len(loot_random_item) - 1)]

				Recipe.unique_id = loot_random_item[0].unique_id

				if len(player.player_inventory) > 0:
					if player.player_inventory[0].unique_id == "rec010":
						if len(player.player_inventory) == 1:
							loot_random_item = None
							return open_lootbox(player)
				else:
					pass

				if lootbox.unique_id == "lb001" or lootbox.unique_id == "lb002" or lootbox.unique_id == "lb004" or lootbox.unique_id == "lb005" or lootbox.unique_id == "lb006" or lootbox.unique_id == "lb008" or lootbox.unique_id == "lb009":
					add_to_recipe(loot_item)
				elif lootbox.unique_id == "lb003" or lootbox.unique_id == "lb007" or lootbox.unique_id == "lb010":
					add_to_equip(loot_item)

				lootbox.quantity -= 1
				if lootbox.quantity <= 0:
					lootbox.loot_inv.remove(lootbox)
		elif loot_open_input.upper() == "N":
			print("\033[43mLootBox™ not opened!\033[0m")
			log_message("Player quit lootbox opening", level=logging.INFO)
			pass
		else:
			print("Invalid input, Please try again!")

def player_level_up(player):
	if player.level == 0:
		player.max_xp = 2000
		player.next_level = 1

		if player.experience >= player.max_xp:
			player.level = 1
			player.max_xp = 4500
			player.next_level = 2
			print("\033[45;1mYour rating has increased!!\033[0m")
			log_message("Level increased to 1", level=logging.INFO)
		else:
			pass

	elif player.level == 1:
		if player.experience >= player.max_xp:
			player.level = 2
			player.max_xp = 7000
			player.next_level = 3
			print("\033[45;1mYour rating has increased!!\033[0m")
			log_message("Level increased to 2", level=logging.INFO)
		else:
			pass

	elif player.level == 2:
		if player.experience >= player.max_xp:
			player.level = 3
			player.max_xp = 12500
			player.next_level = 4
			print("\033[45;1mYour rating has increased!!\033[0m")
			log_message("Level increased to 3", level=logging.INFO)
		else:
			pass

	elif player.level == 3:
		if player.experience >= player.max_xp:
			player.level = 4
			player.max_xp = 20000
			player.next_level = 5
			print("\033[45;1mYour rating has increased!!\033[0m")
			log_message("Level increased to 4", level=logging.INFO)
		else:
			pass

	elif player.level == 4:
		if player.experience >= player.max_xp:
			player.level = 5
			player.max_xp = 40000
			player.next_level = 6
			print("\033[45;1mYour rating has increased!!\033[0m")
			log_message("Level increased to 5", level=logging.INFO)
		else:
			pass

	elif player.level == 5:
		if player.experience >= player.max_xp:
			player.level = 6
			player.max_xp = 60000
			player.next_level = 7
			print("\033[45;1mYour rating has increased!!\033[0m")
			log_message("Level increased to 6", level=logging.INFO)
		else:
			pass

	elif player.level == 6:
		if player.experience >= player.max_xp:
			player.level = 7
			player.max_xp = 90000
			player.next_level = 8
			print("\033[45;1mYour rating has increased!!\033[0m")
			log_message("Level increased to 7", level=logging.INFO)
		else:
			pass

	elif player.level == 7:
		if player.experience >= player.max_xp:
			player.level = 8
			player.max_xp = 120000
			player.next_level = 9
			print("\033[45;1mYour rating has increased!!\033[0m")
			log_message("Level increased to 8", level=logging.INFO)
		else:
			pass

	elif player.level == 8:
		if player.experience >= player.max_xp:
			player.level = 9
			player.max_xp = 175000
			player.next_level = 10
			print("\033[45;1mYour rating has increased!!\033[0m")
			log_message("Level increased to 9", level=logging.INFO)
		else:
			pass

	elif player.level == 9:
		if player.experience >= player.max_xp:
			player.level = 10
			player.max_xp = "MAX"
			player.next_level = "MAX"
			print("\033[45;1mYour rating has increased!!\033[0m")
			log_message("Level increased to 10", level=logging.INFO)
		else:
			pass

	elif player.level == 10:
		player.max_xp = "MAX"
		player.next_level = "MAX"

def add_to_loot(boxluck, boxluck_eq):
	try:
		print("\033[33;1mNew LootBox™ gained!!\033[0m")
		boxluck.loot_print_info()
		beq = boxluck
		LootBox.loot_inv.append(beq)
		log_message("Player gained rec lootbox", level=logging.INFO)
		if boxluck_eq != None:
			print("\033[33;1mNew LootBox™ gained!!\033[0m")
			boxluck_eq.loot_print_info()
			beq_eq = boxluck_eq
			LootBox.loot_inv.append(beq_eq)
			log_message("Player gained eq lootbox", level=logging.INFO)
		boxluck = None
		boxluck_eq = None
	except Exception as error:
		print("Random Lootbox function failed, please see the log file for details")
		log_message(error, level=logging.INFO)

def random_lootbox(recipe, player):
	random_loot_boxes = {
		0: (LootBox.random_loot_inv1, LootBox.random_looteq_inv1),
		1: (LootBox.random_loot_inv1, LootBox.random_looteq_inv1),
		2: (LootBox.random_loot_inv2, LootBox.random_looteq_inv2),
		3: (LootBox.random_loot_inv2, LootBox.random_looteq_inv2),
		4: (LootBox.random_loot_inv3, LootBox.random_looteq_inv3),
		5: (LootBox.random_loot_inv3, LootBox.random_looteq_inv3),
		6: (LootBox.random_loot_inv4, LootBox.random_looteq_inv4),
		7: (LootBox.random_loot_inv4, LootBox.random_looteq_inv4),
		8: (LootBox.random_loot_inv5, LootBox.random_looteq_inv5),
		9: (LootBox.random_loot_inv5, LootBox.random_looteq_inv5),
		10: (LootBox.random_loot_inv6, LootBox.random_looteq_inv6)
	}

	random_box, random_box_eq = random_loot_boxes.get(player.level, (None, None))

	if random_box is None or random_box_eq is None:
		log_message("Invalid player level for random_box / random_box_eq", level=logging.INFO)
		return

	boxluck = random_box[random.randint(0, len(random_box) - 1)]

	if player.level < 2 and random.random() < 0.50:
		boxluck_eq = random_box_eq[random.randint(0, len(random_box_eq) - 1)]
	elif player.level >= 2 and random.random() < 0.65:
		boxluck_eq = random_box_eq[random.randint(0, len(random_box_eq) - 1)]
	elif player.level >= 4 and random.random() < 0.75:
		boxluck_eq = random_box_eq[random.randint(0, len(random_box_eq) - 1)]
	elif player.level >= 6 and random.random() < 0.80:
		boxluck_eq = random_box_eq[random.randint(0, len(random_box_eq) - 1)]
	elif player.level >= 8 and random.random() < 0.99:
		boxluck_eq = random_box_eq[random.randint(0, len(random_box_eq) - 1)]
	else:
		boxluck_eq = None

	add_to_loot(boxluck, boxluck_eq)
	log_message("add_to_loot called with boxluck_eq", level=logging.INFO)
	

def cooking_input(player):
	recipe_list = player.player_inventory
	equip_list = player.player_equip_inv

	if len(recipe_list) <= 0:
		print("\033[43mYou have no recipes in your inventory to cook!\033[0m")
		return

	print("Select the recipe you want to cook")

	for index, recipe in enumerate(recipe_list, 1):
		print(index, f"{recipe.name}")
		
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

def sell_item(player):
	print("1 - Sell recipes")
	print("2 - Go back")
	try:
		log_message("Sell recipes initalised", level=logging.INFO)
		player_selection = int(input("What would you like to do?: "))
	except ValueError:
		print("\033[43mSelection was invalid, please try again!\033[0m")

	if player_selection == 1:
		if len(player.player_inventory) > 0:
			for index, recipe in enumerate(player.player_inventory, 1):
				xpvalue = recipe.exp_value // 5
				print(index, f"{recipe.name} XP gained from selling this recipe: {xpvalue}")
				log_message("Recipe list printed for player in sell_item", level=logging.INFO)
			try:
				rec_del_select = int(input("Which recipe would you like to sell?: "))
			except ValueError:
				print("\033[43mSelection is invalid, please try again!\033[0m")
				return sell_item(player)
			if rec_del_select >= 1:
				recipe.quantity -= 1
				player.experience += xpvalue
				print("You gained: " + f"\033[32;1m+{xpvalue}\033[0m " + "XP!" )
				if recipe.quantity <= 0:
					player.player_inventory.remove(recipe)
				log_message(f"player sold {recipe} for {xpvalue}", level=logging.INFO)	
			elif rec_del_select <= 0:
				print("Your selection is invalid, please try again!")
				return sell_item(player)
		elif len(player.player_inventory) <= 0:
			print("\033[43mYou have no recipes to choose from!\033[0m")
			return sell_item(player)
			log_message("Player returned due to empty inv", level=logging.INFO)
	elif player_selection == 2:
		return
		log_message("Player voluntarily exited sell_item", level=logging.INFO)

def claim_lootbox(player):
	if len(player.player_inventory) <= 0 and len(LootBox.loot_inv) <= 0:
		print("\033[33mSince you have no recipes or LootBox™ in your inventory, here is a spare one, don't lose all your recipes again!\033[0m")
		print("\033[33;1mNew LootBox™ gained!!")
		LootBox.loot_inv.append(lootbox1)
		lootbox1.loot_print_info()
		log_message("Player recieved claim_lootbox", level=logging.INFO)
		return

def save_game(player):
	spc_recipes = [player.meatballs_cooked, player.tomatosauce_cooked, player.spaghetti_cooked]

	chef = player.name, player.level, player.experience, player.max_xp, player.next_level, player.player_inventory, player.player_equip_inv, LootBox.loot_inv, spc_recipes

	file_name = "Saves/chef_1.pkl"
	if os.path.exists(file_name):
		print("\033[43mSave file in slot 1 already exists!\033[0m")

		print("1 - Overwrite Slot 1")
		print("2 - Save in a different slot")
		save_input = int(input("Do you want to overwrite save slot 1 or save in a different slot?: "))


		if save_input == 1:
			with open(file_name, "wb") as file:
				pickle.dump(chef, file)				
				print("\033[42mFile saved successfully to slot 1\033[0m")
				log_message("Save slot 1 overwritten by player", level=logging.INFO)
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
				if os.path.exists("Saves/chef_2.pkl"):
					print("\033[43mSave file in slot 2 already exists!\033[0m")
					overwrite_2 = input("Do you want to overwrite the save in slot 2? (Y/N): ")
					if overwrite_2.upper() == "Y":
						with open("Saves/chef_2.pkl", "wb") as file:
							pickle.dump(chef, file)					
							print("\033[42mGame saved successfully to slot 2\033[0m")
							log_message("Game save overwritten to slot 2 by player", level=logging.INFO)
					elif overwrite_2.upper() == "N":
						print("\033[43mSave slot 2 not overwritten!\033[0m")
						log_message("Game save overwrite denied by player to slot 2", level=logging.INFO)
						return save_game(player)
					else:
						print("Invalid selection, please try again!")
						return save_game(player)
				elif not os.path.exists("Saves/chef_2.pkl"):
					with open("Saves/chef_2.pkl", "wb") as file:
						pickle.dump(chef, file)
						print("\033[42mGame saved successfully to slot 2\033[0m")
						log_message("Game saved to slot 2 by player", level=logging.INFO)	

			elif new_save_input == 1:
				if os.path.exists("Saves/chef_3.pkl"):
					print("\033[43mSave file in slot 3 already exists!\033[0m")
					overwrite_3 = input("Do you want to overwrite the save in slot 3? (Y/N): ")
					if overwrite_3.upper() == "Y":
						with open("Saves/chef_3.pkl", "wb") as file:
							pickle.dump(chef, file)				
							print("\033[42mGame saved successfully to slot 3\033[0m")
							log_message("Game overwritten to slot 3 by player", level=logging.INFO)
					elif overwrite_3.upper() == "N":
						print("\033[43mSave slot 3 not overwritten!\033[0m")
						return save_game(player)
					else:
						print("Invalid selection, please try again!")
						return save_game(player)
				elif not os.path.exists("Saves/chef_3.pkl"):
					with open("Saves/chef_3.pkl", "wb") as file:
						pickle.dump(chef, file)
						print("\033[42mGame saved successfully to slot 3\033[0m")	
						log_message("Game saved to slot 3 by player", level=logging.INFO)

			elif new_save_input == 2:
				print("\033[43mGame not saved!!\033[0m")
				log_message("Game not saved by player", level=logging.INFO)
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
				log_message("Game saved to slot 1 by player", level=logging.INFO)
		elif ask_to_save.upper() == "N":
			print("\033[43mPlayer data not saved!\033[0m")
			log_message("Game save denied by player to slot 1", level=logging.INFO)
			pass
		else:
			print("Invalid input, please try again!")
			save_game(player)

def load_game(player):
	if not os.path.exists("Saves/chef_1.pkl"):
		print("1 - Save Slot 1 - Empty")

	if os.path.exists("Saves/chef_1.pkl"):
		with open("Saves/chef_1.pkl", "rb") as menufile:
			load1 = pickle.load(menufile)
			load1_list = list(load1)
			player.name, player.level, player.experience = load1[:3]
			print("1 - Save Slot 1 - " + f"{player.name} " + f"| Rating: {player.get_load_star()} " + "| XP: " + f"{player.experience}")
			menufile.close()

	if not os.path.exists("Saves/chef_2.pkl"):
		print("2 - Save Slot 2 - Empty")

	if os.path.exists("Saves/chef_2.pkl"):
		with open("Saves/chef_2.pkl", "rb") as menufile:
			load2 = pickle.load(menufile)
			load2_list = list(load2)
			player.name, player.level, player.experience = load2[:3]
			print("2 - Save Slot 2 - " + f"{player.name} " + f"| Rating: {player.get_load_star()} " + "| XP: " + f"{player.experience}")
			menufile.close()

	if not os.path.exists("Saves/chef_3.pkl"):
		print("3 - Save Slot 3 - Empty")

	if os.path.exists("Saves/chef_3.pkl"):
		with open("Saves/chef_3.pkl", "rb") as menufile:
			load3 = pickle.load(menufile)
			load3_list = list(load3)
			player.name, player.level, player.experience = load3[:3]
			print("3 - Save Slot 3 - " + f"{player.name} " + f"| Rating: {player.get_load_star()} " + "| XP: " + f"{player.experience}")
			menufile.close()

	print("4 - Go back")
	print("5 - Delete a save file")
	try:
		ask_save_load = int(input("Choose your option: "))
	except ValueError:
		print("Selection is not in range, please select an option from the provided list!")
		return load_game(player)

	if ask_save_load == 1:
		if os.path.exists("Saves/chef_1.pkl"):
			with open("Saves/chef_1.pkl", "rb") as file:
				import1 = pickle.load(file)
				import1_list = list(import1)
				player.name, player.level, player.experience, player.max_xp, player.next_level = import1[:5]
				recipes = import1[5]
				equipments = import1[6]
				lootboxes = import1[7]
				player.player_inventory = recipes
				player.player_equip_inv = equipments
				LootBox.loot_inv = lootboxes
				spc_recipes = import1[8]
				player.meatballs_cooked = spc_recipes[0]
				player.tomatosauce_cooked = spc_recipes[1]
				player.spaghetti_cooked = spc_recipes[2]
			print("Save slot 1 loaded successfully!")
			log_message("Save file loaded from slot 1 by player", level=logging.INFO)
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 2:
		if os.path.exists("Saves/chef_2.pkl"):
			with open("Saves/chef_2.pkl", "rb") as file:
				import2 = pickle.load(file)
				import2_list = list(import2)
				player.name, player.level, player.experience, player.max_xp, player.next_level = import2[:5]
				recipes = import2[5]
				equipments = import2[6]
				lootboxes = import2[7]
				player.player_inventory = recipes
				player.player_equip_inv = equipments
				LootBox.loot_inv = lootboxes
				spc_recipes = import2[8]
				player.meatballs_cooked = spc_recipes[0]
				player.tomatosauce_cooked = spc_recipes[1]
				player.spaghetti_cooked = spc_recipes[2]
			print("Save slot 2 loaded successfully!")
			log_message("Save file loaded from slot 2 by player", level=logging.INFO)
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 3:
		if os.path.exists("Saves/chef_3.pkl"):
			with open("Saves/chef_3.pkl", "rb") as file:
				import3 = pickle.load(file)
				import3_list = list(import3)
				player.name, player.level, player.experience, player.max_xp, player.next_level = import3[:5]
				recipes = import3[5]
				equipments = import3[6]
				lootboxes = import3[7]
				player.player_inventory = recipes
				player.player_equip_inv = equipments
				LootBox.loot_inv = lootboxes
				spc_recipes = import3[8]
				player.meatballs_cooked = spc_recipes[0]
				player.tomatosauce_cooked = spc_recipes[1]
				player.spaghetti_cooked = spc_recipes[2]
			print("Save slot 3 loaded successfully!")
			log_message("Save file loaded from slot 3 by player", level=logging.INFO)				
		else:
			print("Save slot is empty, please try again!")
			return load_game(player)
	elif ask_save_load == 4:
		call_func('chef_main', 'main_menu')
	elif ask_save_load == 5:
		print("1 - Remove save in slot 1")
		print("2 - Remove save in slot 2")
		print("3 - Remove save in slot 3")
		print("4 - Go back")
		delete_save_inp = int(input("Choose your option: "))

		if delete_save_inp == 1:
			if os.path.exists("Saves/chef_1.pkl"):
				os.remove("Saves/chef_1.pkl")
				print("\033[43mSave file in slot 1 has been removed successfully!\033[0m")
				log_message("Save slot 1 deleted by player", level=logging.INFO)
				return load_game(player)
			elif not os.path.exists("Saves/chef_1.pkl"):
				print("\033[43mSave slot 1 is empty!\033[0m")
				return load_game(player)
		elif delete_save_inp == 2:
			if os.path.exists("Saves/chef_2.pkl"):
				os.remove("Saves/chef_2.pkl")
				print("\033[43mSave file in slot 2 has been removed successfully!\033[0m")
				log_message("Save slot 2 deleted by player", level=logging.INFO)
				return load_game(player)
			elif not os.path.exists("Saves/chef_2.pkl"):
				print("\033[43mSave slot 2 is empty!\033[0m")
				return load_game(player)
		elif delete_save_inp == 3:
			if os.path.exists("Saves/chef_3.pkl"):
				os.remove("Saves/chef_3.pkl")
				print("\033[43mSave file in slot 3 has been removed successfully!\033[0m")
				log_message("Save slot 3 deleted by player", level=logging.INFO)
				return load_game(player)
			elif not os.path.exists("Saves/chef_3.pkl"):
				print("\033[43mSave slot 3 is empty!\033[0m")
				return load_game(player)
		elif delete_save_inp == 4:
			return load_game(player)