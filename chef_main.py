# text colour: print("\033[1;32;40m Bright Green  \n")
# reset colour: print("\033[0m Hiya")

import time
from chef_func import *
import subprocess
import importlib
import os
import sys

if getattr(sys, 'frozen', False):
	# running as a compiled exe
	log_message("Using MEIPASS", level=logging.INFO)
	base_dir = sys._MEIPASS
else:
	# running as a script
	log_message("Using SCRIPT", level=logging.INFO)
	base_dir = os.path.abspath(os.path.dirname(__file__))

log_folder = os.path.join(base_dir, "Logs")
save_folder = os.path.join(base_dir, "Saves")

try:
	importlib.import_module('keyboard')
except ImportError:
	install_key = "Y"
	if install_key == "Y":
		print("\033[42mInstalling additional dependencies\033[0m")
		subprocess.call(['pip3', 'install', 'keyboard'])
	else:
		print("\033[43mRequired dependencies not installed, please install manually by using 'pip3 install keyboard', or try opening the application again!\033[0m")
		exit()

import keyboard

version_id = "\033[35;1mbuild:25 / date:07/11/2023\033[0m | Please email: ccg.issues@gmail.com or join our discord (link on github) for any issues you may encounter, Thank you!"


def progress_bar():
	for i in range(101):
		time.sleep(0.05)
		print(f"\r{i:02d}: {'█'*(i//3)}", end="", flush=True)

def tutorial(player):
	global tutorial_completed
	player_level_up(player)
	player.print_status()
	if tutorial_completed == False:
		tutskip = input("Would you like to skip the tutorial? (Y/N): ")
		if tutskip.upper() == "Y":
			tutorial_completed = True
			LootBox.loot_inv.append(lootbox1)
			print("\033[33;1mNew LootBox™ Acquired!\033[0m")
			lootbox1.loot_print_info()
			print("\033[32;1m+200xp\033[0m for skipping the tutorial!")
			player.experience += 200
			log_message("Tutorial Skipped by player", level=logging.INFO)
			main(player)
		elif tutskip.upper() == "N":
			log_message("Tutorial started by player", level=logging.INFO)
			pass
		else:
			print("Invalid input, please try again!")
			tutorial(player)

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
		print("Chef Mike: Every time you cook a recipe, you forget how to cook it again.")
		returninp = input()
		if keyboard.is_pressed('RETURN'):
			returninp = None
			pass
		print("Chef Mike: There are ways to get past this with items later on, but you'll see what I mean soon enough.")
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

		def open_tut_recipe(player):
			print("\nWhat would you like to do?")
			print("1 - Cook a recipe")
			try:
				tut_inp2 = int(input())
			except ValueError:
				print("Invalid selection, please try again!")
				return open_tut_recipe(player)
			if tut_inp2 == 1:
				cooking_input(player)
			else:
				print("Invalid Input, please try again!")
				return open_tut_recipe(player)
		open_tut_recipe(player)
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

		def open_tut_item(player):
			print("What would you like to do?")
			print("1 - Cook a recipe")
			try:
				tut_inp3 = int(input())
			except ValueError:
				print("Invalid selection, please try again!")
				return open_tut_item(player)
			if tut_inp3 == 1:
				cooking_input(player)
			else:
				print("Invalid selection, please try again!")
				return open_tut_item(player)

		open_tut_item(player)

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
				log_message("Tutorial completed", level=logging.INFO)
				main(player)
			elif tut_inp4 == 2:
				tutorial(player, tutorials_skipped)
			else:
				print("Invalid selection, please try again!")
				return finish_tutorial()

		finish_tutorial()




def main(player):
	claim_loot = False

	while True:
		player_level_up(player)
		if player.level < 10:
			player.print_status()
		elif player.level == 10:
			player.print_status_maxlvl()

		def multiple_recipe_display():
			if player.meatballs_cooked >= 1:
				print(f"\033[32m{recipe5.name}\033[0m: " + f"{player.meatballs_cooked}")
			if player.tomatosauce_cooked >= 1:
				print(f"\033[32m{recipe8.name}\033[0m: " + f"{player.tomatosauce_cooked}")
			if player.spaghetti_cooked >= 1:
				print(f"\033[32m{recipe9.name}\033[0m: " + f"{player.spaghetti_cooked}")
			else:
				pass

		multiple_recipe_display()

		print("\033[44m------MAIN MENU------\033[0m")
		print("1 - Cook a recipe")
		print("2 - Browse your storage")
		print("3 - Open a LootBox™")
		print("4 - View your statistics")
		print("5 - Save your game")
		print("6 - Exit game")
		if len(player.player_inventory) <= 0 and len(LootBox.loot_inv) <= 0:
			print("7 - Claim a LootBox™")
			claim_loot = True
		else:
			pass

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
			print("4 - Sell recipes")
			print("5 - Go back")
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
				sell_item(player) # this is sell recipes for now but might also include equipment in the future
				return main(player)
			elif check_inv_input == 5:
				return main(player)
		elif gameloop_input == 3:
			if len(LootBox.loot_inv) <= 0:
				print("\033[43mYou have no LootBox™ in your inventory!\033[0m")
				return main(player)
			else:
				open_lootbox(player)
				return main(player)
		elif gameloop_input == 4:
			print("\033[43mNot yet avaliable!\033[0m")
			return main(player)		
		elif gameloop_input == 5:
			save_game(player)
			return main(player)
		elif gameloop_input == 6:
			log_message("Game Exited by player", level=logging.INFO)
			print("\033[36mThank you for playing!\033[0m")
			exit()
		elif gameloop_input == 7 and claim_loot == True:
			claim_lootbox(player)
			claim_loot = False
			log_message("Player claimed lootbox from claim_loot", level=logging.INFO)
			return main(player)
		else:
			print("\033[43mInvalid selection, please try again!\033[0m")

def main_menu():
	global tutorial_completed
	print("\033[42;15mWelcome to Cooking Chef!\033[0m")
	print("\033[44mYou are playing on:\033[0m " + version_id)
	print("What would you like to do?")
	print("1 - Start a new game")
	print("2 - Load saved game")
	print("3 - Options")
	print("4 - Exit game")

	def player_name_input():
		global playername
		playername = input("Please enter your name chef! (Max 16 char.): ")
		if len(playername) > 16:
			print("Name is too long, please enter a name under 16 characters!")
			log_message("Inputted name was over 16 characters", level=logging.INFO)
			player_name_input()
		else:
			log_message(f"Player set name to: {playername}", level=logging.INFO)
			pass

	try:
		menu_input = int(input("Select your option: "))
	except ValueError:
		print("Please pick an option from the provided list!")
		return main_menu()
	if menu_input == 1:
		player = Player("", 0, 0, 0, 0)
		tutorial_completed = False
		player_name_input()
		player.name = playername
		tutorial(player)
	elif menu_input == 2:
		player = Player("", 0, 0, 0, 0)
		load_game(player)
		if player.name == "":
			menu_input = 1
			player_name_input()
			player.name = playername
			tutorial_completed = False
			tutorial(player)
		else:
			tutorial_completed = True
			main(player)
	elif menu_input == 3:
		global logging_enabled

		print("\033[43mLogs will be force enabled for the time being!")
		print("No other options avaliable, returning to menu")
		return main_menu()

	#	if logging_enabled == True:
	#		print("1. Logs: turn off logging")
	#	elif logging_enabled == False:
	#		print("1. Logs: turn on logging")

	#	print("2. Go back")

	#	try:
	#		ask_menu3_option = int(input("Select your option: "))
	#	except ValueError:
	#		print("Please pick an option from the provided list")
	#		return main_menu()
	#	if ask_menu3_option == 1 and logging_enabled == True:
	#		logging_enabled = False
	#		print("\033[43mLogging has now been turned off!\033[0m")
	#		return main_menu()
	#	elif ask_menu3_option == 1 and logging_enabled == False:
	#		logging_enabled = True
	#		print("\033[43mLogging has now been turned on!\033[0m")
	#		return main_menu()
	#	elif ask_menu3_option == 2:
	#		return main_menu()

	elif menu_input == 4:
		log_message("Game Exited by player", level=logging.INFO)		
		print("\033[36mThank you for playing!\033[0m")
		exit()
	else:
		print("You have entered an invalid input, please try again!")
		return main_menu()

main_menu()