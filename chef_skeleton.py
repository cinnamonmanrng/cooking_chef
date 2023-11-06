import random

# !! "ITEMS" ARE LABELLED AS EQUIPMENT IN THIS AND REST OF THE CODE
class Player:
	player_inventory = [] # inventory for recipes
	player_equip_inv = [] # inventory for items

	def __init__(self, name, level, experience, max_xp, next_level):
		self.name = name
		self.level = level
		self.experience = experience
		self.max_xp = max_xp
		self.next_level = next_level
		self.meatballs_cooked = 0
		self.spaghetti_cooked = 0
		self.tomatosauce_cooked = 0

	def print_status(self):
		print(f"\033[33;1mName:\033[0m {self.name} \n\033[33;1mRating:\033[0m {Experience.get_level_star(self)} \n\033[33;1mXP:\033[0m {self.experience} / {self.max_xp} \033[33;1muntil\033[0m {Experience.next_level_star(self)}")

	def print_status_maxlvl(self):
		print(f"\033[33;1mName:\033[0m {self.name} \n\033[33;1mRating:\033[0m {Experience.get_level_star(self)} \n\033[33;1mXP:\033[0m {self.experience}")

	def check_inv(self):
		if len(self.player_inventory) == 0:
			print("You do not have any recipes!")
		else:
			for recipe in self.player_inventory:
				recipe.print_info()

	def check_equip_inv(self):
		if len(self.player_equip_inv) == 0:
			print("You do not own any items!")
		else:
			for equip in self.player_equip_inv:
				equip.print_equip_info()

	def get_load_star(self):
		load_star_dict = {
			0: "○",
			1: "☆",
			2: "☆☆",
			3: "☆☆☆",
			4: "☆☆☆☆",
			5: "☆☆☆☆☆",
			6: "★☆☆☆☆",
			7: "★★☆☆☆",
			8: "★★★☆☆",
			9: "★★★★☆",
			10: "★★★★★"
		}
		return load_star_dict.get(self.level, "Invalid Level called")

class Experience(Player):
	def __init__(self, experience, next_level, level):
		super().__init__(experience, next_level, level)
		self.next_level = 0

	def get_level_star(self):
		get_level_dict = {
			0: "○",
			1: "☆",
			2: "☆☆",
			3: "☆☆☆",
			4: "☆☆☆☆",
			5: "☆☆☆☆☆",
			6: "★☆☆☆☆",
			7: "★★☆☆☆",
			8: "★★★☆☆",
			9: "★★★★☆",
			10: "★★★★★"
		}
		return get_level_dict.get(self.level, "Invalid Level called")

	def next_level_star(self):
   		next_levels_dict = {
        	(0, 1): "☆",
        	(1, 2): "☆☆",
        	(2, 3): "☆☆☆",
        	(3, 4): "☆☆☆☆",
        	(4, 5): "☆☆☆☆☆",
        	(5, 6): "★☆☆☆☆",
        	(6, 7): "★★☆☆☆",
        	(7, 8): "★★★☆☆",
        	(8, 9): "★★★★☆",
        	(9, 10): "★★★★★",
        	(10, "MAX"): "Max Level Reached"
    	}
   		return next_levels_dict.get((self.level, self.next_level), "Invalid next level returned")


class Item:
	def __init__(self, name, description, rating, quantity):
		self.name = name
		self.description = description
		self.rating = rating
		self.quantity = quantity
	def print_info(self):
		print(f'{self.name}: {self.description} | Rating: {self.rating}') # print info for player inventory check

class Equipment(Item):
	equipbox1_inv = [] # common
	equipbox2_inv = [] # uncommon
	equipbox3_inv = [] # rare
	equipbox4_inv = [] # epic
	equipbox5_inv = [] # legendary
	equipbox6_inv = [] # mythical

	def __init__(self, name, description, rating, effect, quantity, unique_id):
		super().__init__(name, description, rating, quantity)
		self.unique_id = unique_id
		self.effect = effect

	@classmethod
	def check_equip_inv(cls):
		if len(cls.equipbox1_inv) == 0:
			print("You do not have any equipment")
		else:
			for equip in cls.equipbox1_inv:
				equip.print_equip_info()

	def print_equip_info(self):
		print(f'{self.name}: {self.description} | Rating: {Equipment.equip_quality(self)}')

	def equip_quality(self):
		equip_q_dict = {
			0: "☆",
			1: "★",
			2: "★★",
			3: "★★★",
			4: "★★★★",
			5: "★★★★★"
		}
		return equip_q_dict.get(self.rating, "Unrecognised rating")

class LootBox(Item):
	loot_inv = [] # player's lootbox inventory

	# refer to chef_call_list to find specific items in these lists
	# make these into non rarity based lootboxes which instead have a few rare items and mostly less rare items.
	random_loot_inv1 = [] # common
	random_loot_inv1_1 = [] # common and special recipe box
	random_loot_inv2 = [] # common / uncommon
	random_loot_inv2_1 = [] # more uncommon than common
	random_loot_inv3 = [] # uncommon / rare
	random_loot_inv3_1 = [] # more rare than uncommon
	random_loot_inv4 = [] # rare / epic
	random_loot_inv4_1 = [] # more epic than rare
	random_loot_inv5 = [] # epic / legendary
	random_loot_inv5_1 = [] # more legendary
	random_loot_inv6 = [] # mythical
	
	random_looteq_inv1 = []
	random_looteq_inv1_1 = []
	random_looteq_inv2 = []
	random_looteq_inv2_1 = []
	random_looteq_inv3 = []
	random_looteq_inv3_1 = []
	random_looteq_inv4 = []
	random_looteq_inv4_1 = []
	random_looteq_inv5 = []
	random_looteq_inv5_1 = []
	random_looteq_inv6 = [] 

	def __init__(self, name, description, rating, quantity, unique_id):
		super().__init__(name, description, rating, quantity)
		self.unique_id = unique_id
		
	def loot_print_info(self):
		print(f"{self.name}: {self.description} | Rating: {LootBox.loot_rating(self)}")

	@classmethod
	def check_loot_inv(cls):
		if len(cls.loot_inv) == 0:
			print("You do not have any lootboxes!")
		else:
			for lootbox in cls.loot_inv:
				lootbox.loot_print_info()

	def loot_rating(self): 
		loot_r_dict = {
			0: "☆",
			1: "★",
			2: "★★",
			3: "★★★",
			4: "★★★★",
			5: "★★★★★"
		}
		return loot_r_dict.get(self.rating, "Invalid loot rating returned")

class Recipe:
	lootbox1_inv = [] # common
	lootbox1_1_inv = [] # alt common
	lootbox1_2_inv = [] # alt common
	lootbox1_3_inv = [] # lb005 unique
	lootbox2_inv = [] # uncommon
	lootbox2_1_inv = [] # alt uncommon
	lootbox3_inv = [] # rare
	lootbox3_1_inv = [] # alt rare
	lootbox4_inv = [] # epic
	lootbox5_inv = [] # legendary
	lootbox6_inv = [] # mythical

	def __init__(self, name, exp_value, quality, timer, quantity, unique_id):
		self.name = name
		self.exp_value = exp_value
		self.quality = quality
		self.timer = timer # in seconds
		self.quantity = quantity
		self.unique_id = unique_id # used to check unique equipment against recipes in timer function

	@classmethod
	def check_recipe_inv(cls):
		if len(cls.recipe_inv) == 0:
			print("You do not know any recipes, check again later!")
		else:
			for recipe in cls.recipe_inv:
				recipe.print_info()

	def recipe_quality(self):
		recipe_q_dict = {
			0: "☆",
			1: "★",
			2: "★★",
			3: "★★★",
			4: "★★★★",
			5: "★★★★★"
		}
		return recipe_q_dict.get(self.quality, "Unrecognised recipe_quality returned")

	def print_info(self):
		print(f'{self.name}: XP gained from this recipe: {self.exp_value} | Quality: {Recipe.recipe_quality(self)} | Time to cook: {self.timer}')

		