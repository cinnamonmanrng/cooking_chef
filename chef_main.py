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
from chef_func import *
import keyboard

version_id = "build:21.3_10/03/23 | Please email: ccg.issues@gmail.com or join our discord for any issues you may encounter, Thank you!"

# exp mechanic
# 1 second = 25 xp

# initalise recipes
recipe1 = Recipe("\033[32mSimple boiled potatoes\033[0m", 25 * 6, 0, 6, 1, "rec001")
recipe2 = Recipe("\033[32mBacon and egg\033[0m", 25 * 5, 0, 5, 1, "rec002")
recipe3 = Recipe("\033[32mMashed potatoes\033[0m", 25 * 10, 0, 10, 1, "rec003")
recipe4 = Recipe("\033[32mOvercooked tuna\033[0m", 25 * 5, 0, 5, 1, "rec004")
recipe5 = Recipe("\033[32;1mSimple boiled spaghetti\033[0m", 25 * 12, 1, 12, 1, "rec005")

# initalise equipment
equip1 = Equipment("\033[32mBeginner's oven glove\033[0m", "Increases the current recipe's XP by 50", 0, 50, 1, "eq001")
equip2 = Equipment("\033[32mCheap plastic fork\033[0m", "Decreases cooking time of any recipe by 2 seconds", 0, 2, 1, "eq002")
equip3 = Equipment("\033[32mMystery potato flavouring\033[0m", f"Decreases {recipe1.name}'s cooking time by 5 seconds", 0, 5, 1, "eq003")
equip4 = Equipment("\033[32;1mRegular plastic fork\033[0m", "Decreases cooking time of any recipe by 4 seconds", 1, 4, 1, "eq004")
equip5 = Equipment("\033[32;1mStarter chef's handy whisk", "Increases the current recipe's XP by 100", 1, 100, 1, "eq005")

# initalise lootbox
lootbox1 = LootBox("\033[32mJunior chef's LootBox™\033[0m", "A wonderful start for every chef in Emerald's Restaurants™", 0, 1, "lb001")
lootbox2 = LootBox("\033[32mFirst edition LootBox™\033[0m", "Like the name describes, quite old and out of date, but will work for now!", 0, 1, "lb002")
lootbox3 = LootBox("\033[32mAspiring chef's helpful LootBox™\033[0m", "If you need new Items, we've got you covered with this LootBox™!", 0, 1, "lb003")
lootbox4 = LootBox("\033[32;1mOutdated helpful LootBox™\033[0m", "Better Items can be found here!", 1, 1, "lb004")

# adding items to lootbox inventories and lootboxes to player inventory
Equipment.equipbox1_inv.append(equip1)
Equipment.equipbox1_inv.append(equip2)
Equipment.equipbox1_inv.append(equip3)
Equipment.equipbox2_inv.append(equip2)
Equipment.equipbox2_inv.append(equip4)
Equipment.equipbox2_inv.append(equip5)

Recipe.lootbox1_inv.append(recipe1)
Recipe.lootbox1_inv.append(recipe2)
Recipe.lootbox1_inv.append(recipe3)
Recipe.lootbox1_inv.append(recipe4)
Recipe.lootbox1_inv.append(recipe5)

LootBox.random_loot_inv1.append(lootbox1)
LootBox.random_loot_inv1.append(lootbox2)
LootBox.random_looteq_inv1.append(lootbox3)
LootBox.random_looteq_inv2.append(lootbox4)

# gameloop plan:
# initalise menu:
# 1 - new game
# 2 - load saved game
# 3 - options - anything like delete character, colours and other settings once the pygame application is done will go here
# 4 - exit game

def progress_bar():
	for i in range(101):
		time.sleep(0.05)
		print(f"\r{i:02d}: {'#'*(i//3)}", end="", flush=True)

def tutorial(player):
	global tutorial_completed
	player_level_up(player)
	if tutorial_completed == False:
		tutskip = input("Would you like to skip the tutorial? (Y/N): ")
		if tutskip.upper() == "Y":
			tutorial_completed = True
			LootBox.loot_inv.append(lootbox1)
			print("\033[33;1mNew LootBox™ Acquired!\033[0m")
			lootbox1.loot_print_info()
			main(player)
		elif tutskip.upper() == "N":
			pass

		print("To continue along within the tutorial, press the RETURN key, unless you are told to wait!")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: Welcome to your first shift at one of the brand new Emerald Restaurants™, Let's get you settled in!")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			pass
		print("Chef Mike: Let's get you started with a company sponsored LootBox™, this will give you a hand in starting your career.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		LootBox.loot_inv.append(lootbox1)
		print("\033[33;1mNew LootBox™ Acquired!\033[0m")
		lootbox1.loot_print_info()
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: Now let's get that LootBox™ open for you! I'll show you how now through your personal device.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("...Opening  your personal Emerald Tech.™ device, please wait")
		progress_bar()
		print("\n\033[42mWELCOME TO YOUR PERSONAL EMERALD TECH™ DEVICE\033[0m")
		print("...Adding LootBox™ to MENU, please wait!")
		progress_bar()
		print("\nWhat would you like to do?")
		print("3 - Open a LootBox™")

		def open_tut_loot(player):
			try:
				tut_inp1 = int(input())
			except ValueError:
				print("Invalid selection, please try again!")
				return open_tut_loot(player)
			if tut_inp1 == 3:
				open_lootbox(player)
			else:
				print("Invalid option, please try again!")
				return open_tut_loot(player)
			while len(player.player_inventory) <= 0:
				print("Please open your lootbox!")
				open_lootbox(player)

		open_tut_loot(player)

		print("Chef Mike: Good Job! Now we can move on to the next step.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: There is one more thing to mention however...")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: Every time you cook a recipe, you forget how to cook it again, unless you have gotten multiple of the same recipe from your company sponsored lootboxes.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: This is a bit weird, I know, but these days it is fairly common, I guess the company keeps their recipes secret that way.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: Now I will teach you how to cook this recipe!")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: So, let's get started!")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("... Adding recipe to MENU, please wait!")
		progress_bar()

		def cook_tut_recipe(player):
			print("\nWhat would you like to do?")
			print("1 - Cook a recipe")
			try:
				tut_inp2 = int(input())
			except ValueError:
				print("Invalid selection, please try again!")
				return cook_tut_recipe(player)
			if tut_inp2 == 1:
				cooking_input(player)
			else:
				print("Invalid Input, please try again!")
				return cook_tut_recipe(player)
		cook_tut_recipe(player)
		print("Chef Mike: So now you have opened a LootBox™ and cooked a recipe and gained a new LootBox™, and I'm fairly certain you don't remember how you cooked what you just cooked!")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: But don't worry, you'll get more lootboxes through cooking more recipes.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: Now I will teach you how to use items.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: Since items will be extremely important once you gain more recognition, let's start with the basics of items")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: Items can do a huge variety of things to help you cook recipes, they can decrease the time it takes, give you more experience from cooking a recipe and many more things you'll find out later on.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: So let's get started, I'll give you an item I found in storage, and a new recipe, otherwise you get them from specalised lootboxes.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass

		print("...Adding Items to MENU, please wait!")
		progress_bar()
		print("\n\033[33;1mNew Item gained!!\033[0m")
		player.player_equip_inv.append(equip1)
		equip1.print_equip_info()
		print("\033[33;1mNew Recipe gained!!\033[0m")
		player.player_inventory.append(recipe1)
		recipe1.print_info()

		def use_item_tutorial(player):
			print("What would you like to do?")
			print("1 - Cook a recipe")
			try:
				tut_inp3 = int(input())
			except ValueError:
				print("Invalid selection, please try again!")
				return use_item_tutorial(player)
			if tut_inp3 == 1:
				cooking_input(player)
			else:
				print("Invalid selection, please try again!")
				return use_item_tutorial(player)

		use_item_tutorial(player)

		print("Chef Mike: Notice how you gained 50 more experience points for cooking this recipe with that item.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: Looks like you are ready to start your journey in the kitchen.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: Just rememeber what I taught you and you should be fine, Good Luck!")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass

		def finish_tutorial():
			print("1 - Continue to start a new game")
			print("2 - Replay the tutorial")
			try:
				tut_inp4 = int(input("Choose your option: "))
			except ValueError:
				print("Invalid selection, please try again!")
				return finish_tutorial()

			if tut_inp4 == 1:
				tutorial_completed = True
				main(player)
			elif tut_inp4 == 2:
				tutorial(player, tutorials_skipped)
			else:
				print("Invalid selection, please try again!")
				return finish_tutorial()

		finish_tutorial()




def main(player):
	while True:
		player_level_up(player)
		print("\033[44m------MAIN MENU------\033[0m")
		print("1 - Cook a recipe")
		print("2 - Browse your storage")
		print("3 - Open a LootBox™")
		print("4 - View your statistics")
		print("5 - Save your game")
		print("6 - Exit game")
		try:
			gameloop_input = int(input("Which option would you like to continue with?: "))
		except ValueError:
			print("Invalid option, please try again!")
			return main(player)

		if gameloop_input == 1:
			cooking_input(player)
			return main(player)
		elif gameloop_input == 2:
			print("1 - Recipes Notebook")
			print("2 - Item Storage")
			print("3 - LootBox™ Storage")
			print("4 - Go back")
			try:
				check_inv_input = int(input("What would you like to check?: "))
			except ValueError:
				print("\033[43mInvalid Selection, PLease try again!\033[0m")

			if check_inv_input == 1:
				player.check_inv()
				return main(player)
			elif check_inv_input == 2:
				player.check_equip_inv()
				return main(player)
			elif check_inv_input == 3:
				LootBox.check_loot_inv()
				return main(player)
			elif check_inv_input == 4:
				return main(player)
		elif gameloop_input == 3:
			open_lootbox(player)
			return main(player)
		elif gameloop_input == 4:
			print("Not in use")
			return main(player)		
		elif gameloop_input == 5:
			save_game(player)
			return main(player)
		elif gameloop_input == 6:
			print("\033[36mThank you for playing!\033[0m")
			exit()
		else:
			print("\033[43mInvalid selection, please try again!\033[0m")

def main_menu():
	global tutorial_completed
	print("\033[42;15mWelcome to Cooking Chef!\033[0m")
	print("\033[44mYou are playing on:\033[0m " + version_id)
	print("What would you like to do?")
	print("\nSelect your option:")
	print("1 - Start a new game")
	print("2 - Load saved game")
	print("3 - Options")
	print("4 - Exit game")
	try:
		menu_input = int(input())
	except ValueError:
		print("Please pick an option from the provided list!")
		return main_menu()
	if menu_input == 1:
		player = Player("", 0, 0, 0, 0)
		playername = input("Please enter your name, young chef!: ")
		tutorial_completed = False
		player.name = playername
		tutorial(player)
	elif menu_input == 2:
		player = Player("", 0, 0, 0, 0)
		load_game(player)
		if player.name == "":
			menu_input = 1
			playername = input("Please enter your name, young chef!: ")
			player.name = playername
			tutorial_completed = False
			tutorial(player)
		else:
			tutorial_completed = True
			main(player)
	elif menu_input == 3:
		print("\033[43mOptions not avaliable yet, please check again later!\033[0m")
		return main_menu()
	elif menu_input == 4:
		print("\033[36mThank you for playing!\033[0m")
		exit()
	else:
		print("You have entered an invalid input, please try again!")
		return main_menu()

main_menu()