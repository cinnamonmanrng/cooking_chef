class Player:
	player_inventory = []

	def __init__(self, name, level, experience, max_xp, next_level):
		self.name = name
		self.level = level
		self.experience = experience
		self.max_xp = max_xp
		self.next_level = next_level

	def print_status(self):
		print(f"{self.name} | Rating: {Experience.get_level_star(self)} | XP: {self.experience} / {self.max_xp} until {Experience.next_level_star(self)}")

	def check_inventory(self):
		if len(self.inventory) == 0:
			print("Your inventory is empty, check again later!")
		else:
			for item in self.inventory:
				Item.print_info()

class Experience(Player):
	def __init__(self, experience, next_level, level):
		super().__init__(experience, next_level, level)
		self.next_level = 0

	def get_level_star(self):
		if self.level == 0:
			return "Unrecognised"
		elif self.level == 1:
			return "★"
		elif self.level == 2:
			return "★★"
		elif self.level == 3:
			return "★★★"
		elif self.level == 4:
			return "★★★★"
		elif self.level == 5:
			return "★★★★★"
		else: 
			return "Invalid Level"

	def next_level_star(self):
		if self.level == 0 and self.next_level == 1:
				return "☆"
		elif self.level == 1 and self.next_level == 2:
			return "★☆"
		elif self.level == 2 and self.next_level == 3:
			return "★★☆"
		elif self.level == 3 and self.next_level == 4:
			return "★★★☆"
		elif self.level == 4 and self.next_level == 5:
			return "★★★★☆"
		elif self.level == 5 and self.next_level == "MAX":
			return "★★★★★"
		else:
			return "Invalid next level"


class Item:
	def __init__(self, name, description, rating, effect, quantity):
		self.name = name
		self.description = description
		self.rating = rating
		self.effect = effect
		self.quantity = quantity
	def print_info(self):
		print(f'{self.name}: {self.description} | Rating: {self.rating} | Amount: {self.quantity}') # print info for player inventory check

class Equipment(Item):
	equip_inv = []

	def __init__(self, name, description, rating, effect, quantity):
		super().__init__(name, description, rating, effect, quantity)

	@classmethod
	def check_equip_inv(cls):
		if len(cls.equip_inv) == 0:
			print("You do not have any equipment")
		else:
			for equip in cls.equip_inv:
				equip.print_equip_info()

	def print_equip_info(self):
		print(f'{self.name}: {self.description} | Rating: {Equipment.equip_quality(self)} | Amount: {self.quantity}')

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


class Booster(Item):
	def __init__(self, name, description, rating, effect, quantity, duration):
		super().__init__(name, description, rating, effect, quantity)
		self.duration = duration

	def print_booster_info(self):
		print(f'{self.name}: {self.description} | Rating: {self.rating} | Amount: {self.quantity} | Duration: {self.duration}')


class Recipe:
	recipe_inv = []

	def __init__(self, name, exp_value, quality, timer):
		self.name = name
		self.exp_value = exp_value
		self.quality = quality
		self.timer = timer # in seconds
		# self.quality_x = quality_x # quality multiplier (0 = 1 | 1 = 1.1 | 2 = 1.2 | 3 = 1.3 | 4 = 1.5 | 5 = 1.8)

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