import random

class Player:
	player_inventory = []
	player_equip_inv = []

	def __init__(self, name, level, experience, max_xp, next_level):
		self.name = name
		self.level = level
		self.experience = experience
		self.max_xp = max_xp
		self.next_level = next_level

	def print_status(self):
		print(f"Name: {self.name} \nRating: {Experience.get_level_star(self)} \nXP: {self.experience} / {self.max_xp} until {Experience.next_level_star(self)}")

	def check_inv(self):
		if len(self.player_inventory) == 0:
			print("Your inventory is empty!")
		else:
			for recipe in self.player_inventory:
				recipe.print_info()

	def check_equip_inv(self):
		if len(self.player_equip_inv) == 0:
			print("You do not own any items!")
		else:
			for equip in self.player_equip_inv:
				equip.print_equip_info()

class Experience(Player):
	def __init__(self, experience, next_level, level):
		super().__init__(experience, next_level, level)
		self.next_level = 0

	def get_level_star(self):
		if self.level == 0:
			return "Unrecognised"
		elif self.level == 1:
			return "☆"
		elif self.level == 2:
			return "☆☆"
		elif self.level == 3:
			return "☆☆☆"
		elif self.level == 4:
			return "☆☆☆☆"
		elif self.level == 5:
			return "☆☆☆☆☆"
		elif self.level == 6:
			return "★☆☆☆☆"
		elif self.level == 7:
			return "★★☆☆☆"
		elif self.level == 8:
			return "★★★☆☆"
		elif self.level == 9:
			return "★★★★☆"
		elif self.level == 10:
			return "★★★★★"
		else: 
			return "Invalid Level"

	def next_level_star(self):
		if self.level == 0 and self.next_level == 1:
				return "☆"
		elif self.level == 1 and self.next_level == 2:
			return "☆☆"
		elif self.level == 2 and self.next_level == 3:
			return "☆☆☆"
		elif self.level == 3 and self.next_level == 4:
			return "☆☆☆☆"
		elif self.level == 4 and self.next_level == 5:
			return "☆☆☆☆☆"
		elif self.level == 5 and self.next_level == 6:
			return "★☆☆☆☆"
		elif self.level == 6 and self.next_level == 7:
			return "★★☆☆☆"
		elif self.level == 7 and self.next_level == 8:
			return "★★★☆☆"
		elif self.level == 8 and self.next_level == 9:
			return "★★★★☆"
		elif self.level == 9 and self.next_level == 10:
			return "★★★★★"
		elif self.level == 10 and self.next_level == "MAX":
			return "Max Level Reached"
		else:
			return "Invalid next level"


class Item:
	def __init__(self, name, description, rating, quantity):
		self.name = name
		self.description = description
		self.rating = rating
		self.quantity = quantity
	def print_info(self):
		print(f'{self.name}: {self.description} | Rating: {self.rating}') # print info for player inventory check

class Equipment(Item):
	equipbox1_inv = []
	# equipbox2_inv = []

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
		if self.rating == 0:
			return "☆"
		elif self.rating == 1:
			return "★"
		elif self.rating == 2:
			return "★★"
		elif self.rating == 3:
			return "★★★"
		elif self.rating == 4:
			return "★★★★"
		elif self.rating == 5:
			return "★★★★★"
		else:
			print("Unrecognised Rating")

class LootBox(Item):
	loot_inv = []
	random_loot_inv1 = []
	random_looteq_inv1 = []

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
		if self.rating == 0:
			return "☆"
		elif self.rating == 1:
			return "★"
		elif self.rating == 2:
			return "★★"
		elif self.rating == 3:
			return "★★★"
		elif self.rating == 4:
			return "★★★★"
		elif self.rating == 5:
			return "★★★★★"

class Recipe:
	lootbox1_inv = [] # lootbox1 in chef_main, other boxes follow the same criteria
	lootbox2_inv = []

	def __init__(self, name, exp_value, quality, timer, quantity, unique_id):
		self.name = name
		self.exp_value = exp_value
		self.quality = quality
		self.timer = timer # in seconds
		self.quantity = quantity
		self.unique_id = unique_id # used to check unique equipment against recipes

	@classmethod
	def check_recipe_inv(cls):
		if len(cls.recipe_inv) == 0:
			print("You do not know any recipes, check again later!")
		else:
			for recipe in cls.recipe_inv:
				recipe.print_info()

	def recipe_quality(self):
		if self.quality == 0:
			return "☆"
		elif self.quality == 1:
			return "★"
		elif self.quality == 2:
			return "★★"
		elif self.quality == 3:
			return "★★★"
		elif self.quality == 4:
			return "★★★★"
		elif self.quality == 5:
			return "★★★★★"
		else:
			print("Unrecognised quality")

	def print_info(self):
		print(f'{self.name}: XP gained from this recipe: {self.exp_value} | Quality: {Recipe.recipe_quality(self)} | Time to cook: {self.timer}')

		