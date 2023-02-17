# chef simulator
	# add player (chef) class *
	# add stats (1 - 5 stars) *
	# develop stats by cooking and other stuff (gain xp from recipes) / timer ending gives xp to player *
		# will need a lot of if statements, optimisation problems inc.
		# also need to fix timer to recognise multiple recipes without manual input
	# equipment and equipment upgrading (equipment parts to upgrade equipment or forge a new one)
	# recipe preparation mechanics (time, queue, booster items affect time)
	# create a list of recipe names, unlockable by quality (upgradeable with items) also how much time they take *
	# late game booster items (hats, clothes and whatever)
	# tutorial
	# saving and loading game mechanics

# cd desktop/'gert work'/'gert coding'/'chef game'

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
	def __init__(self, name, description, rating, quantity):
		self.name = name
		self.description = description
		self.rating = rating
		self.quantity = quantity
	def print_info(self):
		print(f'{self.name}: {self.description} | Rating: {self.rating} | Amount: {self.quantity}') # print info for player inventory check

class Equipment(Item):
	def __init__(self, name, description, rating, quantity):
		super().__init__(name, description, rating, quantity)

class Equip_part(Item):
	def __init__(self, name, description, rating, quantity):
		super().__init__(name, description, rating, quantity)

class Recipe:
	recipe_inv = []

	def __init__(self, name, exp_value, quality, timer):
		self.name = name
		self.exp_value = exp_value
		self.quality = quality
		self.timer = timer # in seconds
		# self.quality_x = quality_x # quality multiplier (0 = 1 | 1 = 1.1 | 2 = 1.2 | 3 = 1.3 | 4 = 1.5 | 5 = 1.8)

#	def gain_xp_recipe(self): # not sure why but this does not add experience points to player when called
#		if self.timer <= 0:
#			Player.experience += self.exp_value

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