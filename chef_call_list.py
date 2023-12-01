from chef_skeleton import *

# basic exp mechanic
# special recipes = recipes that need to have one or more other recipes cooked as a prequisite
# Quality list:
# 0: 1 sec = 25xp / special recipes 0: 1 sec = 40xp
# 1: 1 sec = 35xp 
# 2: 1 sec = 50xp
# 3: 1 sec = 85xp
# 4: 1 sec = 110xp
# 5: 1 sec = 160xp

# common: \033[32m
# uncommon: \033[32;1m
# rare: \033[34m
# epic: \033[35m
# legendary: \033[31;1m
# mythic/unique: \033[36;1m

# initalise recipes
# quality 0
recipe1 = Recipe("\033[32mSimple boiled potatoes\033[0m", 25 * 6, 0, 6, 1, "rec001")
recipe2 = Recipe("\033[32mBacon and egg\033[0m", 25 * 5, 0, 5, 1, "rec002")
recipe3 = Recipe("\033[32mMashed potatoes\033[0m", 25 * 10, 0, 10, 1, "rec003")
recipe4 = Recipe("\033[32mOvercooked tuna\033[0m", 25 * 5, 0, 5, 1, "rec004")
recipe5 = Recipe("\033[32mMeatballs\033[0m", 25 * 9, 0, 9, 1, "rec005")
recipe6 = Recipe("\033[32mOven roasted chicken\033[0m", 25 * 10, 0, 10, 1, "rec006")
recipe7 = Recipe("\033[32mMinced beef\033[0m", 25 * 5, 0, 5, 1, "rec007")
recipe8 = Recipe("\033[32mSeasoned tomato sauce\033[0m", 25 * 7, 0, 7, 1, "rec008")
recipe9 = Recipe("\033[32mBoiled Spaghetti\033[0m", 25 * 8, 0, 8, 1, "rec009")
recipe10 = Recipe(f"\033[32;1mSpaghetti and meatballs in tomato sauce\033[0m | Requires: {recipe5.name}, {recipe8.name} and {recipe9.name}", 40 * 20, 1, 20, 1, "rec010")
recipe11 = Recipe("\033[32mMargherita Pizza\033[0m", 25 * 12, 0, 12, 1, "rec011")
recipe12 = Recipe("\033[32mGrandma's toasted beans\033[0m", 25 * 10, 0, 10, 1, "rec012")
recipe13 = Recipe("\033[32m2040's classic fried egg\033[0m", 25 * 3, 0, 3, 1, "rec013")
recipe14 = Recipe("\033[32mClassic vegetable stir fry\033[0m", 25 * 6, 0, 6, 1, "rec014")
recipe15 = Recipe("\033[32mGrilled pork cubes\033[0m", 25 * 9, 0, 9, 1, "rec015")
recipe26 = Recipe("\033[32mGrilled cheese sandwich\033[0m", 25 * 8, 0, 8, 1, "rec026")
recipe27 = Recipe("\033[32mRoasted vegetables\033[0m", 25 * 7, 0, 7, 1, "rec027")
recipe28 = Recipe("\033[32mScrambled eggs\033[0m", 25 * 4, 0, 4, 1, "rec028")

#quality 1
recipe16 = Recipe("\033[32;1mGrilled octopus legs\033[0m", 35 * 13, 1, 13, 1, "rec016")
recipe17 = Recipe("\033[32;1mGenetically modified chicken strips\033[0m", 35 * 15, 1, 15, 1, "rec017")
recipe18 = Recipe("\033[32;1mBiotech beet salad\033[0m", 35 * 14, 1, 14, 1, "rec018")
recipe19 = Recipe("\033[32;1mIntergalactic grilled cheese\033[0m", 35 * 18, 1, 18, 1, "rec019")
recipe20 = Recipe("\033[32;1mDisco fries\033[0m", 35 * 12, 1, 12, 1, "rec020")
recipe21 = Recipe("\033[32;1mCheesy bacon bites\033[0m", 35 * 16, 1, 16, 1, "rec021")
recipe22 = Recipe("\033[32;1mBlueberry Pie\033[0m", 35 * 20, 1, 20, 1, "rec022")
recipe23 = Recipe("\033[32;1mWatermelon salad\033[0m", 35 * 12, 1, 12, 1, "rec023")
recipe24 = Recipe("\033[32;1mCrispy fish taco\033[0m", 35 * 17, 1, 17, 1, "rec024")
recipe25 = Recipe("\033[32;1mPlain pancakes\033[0m", 35 * 15, 1, 15, 1, "rec025")
recipe29 = Recipe("\033[32;1mCreamy tomato soup\033[0m", 35 * 10, 1, 10, 1, "rec029")
recipe30 = Recipe("\033[32;1mSpicy chicken wings\033[0m", 35 * 9, 1, 9, 1, "rec030")
recipe31 = Recipe("\033[32;1mChocolate chip cookies\033[0m", 35 * 13, 1, 13, 1, "rec031")

# quality 2
recipe32 = Recipe("\033[34mBeef wellington\033[0m", 50 * 20, 2, 20, 1, "rec032")
recipe33 = Recipe("\033[34mSushi platter\033[0m", 50 * 15, 2, 15, 1, "rec033")
recipe34 = Recipe("\033[34mTiramisu\033[0m", 50 * 30, 2, 30, 1, "rec034")

# initalise equipment
# quality 0
equip1 = Equipment("\033[32mBeginner's oven glove\033[0m", "Increases the current recipe's XP by 50", 0, 50, 1, "eq001")
equip2 = Equipment("\033[32mCheap plastic fork\033[0m", "Decreases cooking time of any recipe by 2 seconds", 0, 2, 1, "eq002")
equip3 = Equipment("\033[32mMystery potato flavouring\033[0m", f"Decreases {recipe1.name}'s or {recipe3.name}'s cooking time by 5 seconds", 0, 5, 1, "eq003") # only for rec001 and rec003
equip4 = Equipment("\033[32mGrandma's toaster\033[0m", f"Decreases {recipe12.name}'s cooking time by 5 seconds", 0, 5, 1, "eq004") # only for rec012
equip5 = Equipment("\033[32mRubbery spatula\033[0m", "Decreases cooking time of any recipe by 6 seconds", 0, 6, 1, "eq005")
equip6 = Equipment("\033[32mDollar store frying pan\033[0m", "Increases the current recipe's XP by 75", 0, 75, 1, "eq006")
equip7 = Equipment("\033[32mUnreliable cooking pot\033[0m", "50% chance to increase or decrease a recipe's cooking time by 5 seconds", 0, 5, 1, "eq007")

# quality 1 
equip8 = Equipment("\033[32;1mChef's apron\033[0m", "Increases the current recipe's XP by 85", 1, 85, 1, "eq008")
equip9 = Equipment("\033[32;1mSlightly used blender\033[0m", "Decreases cooking time of any recipe by 9 seconds", 1, 9, 1, "eq009")
equip10 = Equipment("\033[32;1mMixing bowls\033[0m", "Increases the current recipe's XP by 100", 1, 100, 1, "eq010")
equip11 = Equipment("\033[32;1mWholesale knife set\033[0m", f"Decreases {recipe30.name}'s cooking time by 6 seconds", 1, 6, 1, "eq011")
equip12 = Equipment("\033[32;1mBaking stone\033[0m", f"Decreases {recipe31.name}'s or {recipe34.name}'s cooking time by 7 seconds", 1, 7, 1, "eq012")

# quality 2
equip13 = Equipment("\033[34mSous vide machine\033[0m", "Decreases cooking time for any recipe by 13 seconds", 2, 13, 1, "eq013")
equip14 = Equipment("\033[34mFood processor\033[0m", "Increases the current recipe's XP by 175", 2, 175, 1, "eq014")
equip15 = Equipment("\033[34mCopper cookware set\033[0m", f"Decreases {recipe32.name}'s cooking time by 15 seconds", 2, 12, 1, "eq015")
equip16 = Equipment("\033[34mProfessional chef's hat\033[0m", "Increases the current recipe's XP by 185", 2, 185, 1, "eq016")
equip17 = Equipment("\033[34mSecond-hand smoker grill\033[0m", "Decreases cooking time for any recipe by 15 seconds", 2, 15, 1, "eq017")


# initalise lootbox
# quality 0
lootbox1 = LootBox("\033[32mJunior chef's LootBox™\033[0m", "A wonderful start for every chef in Emerald's Restaurants™", 0, 1, "lb001")
lootbox2 = LootBox("\033[32mThe special recipe LootBox™\033[0m", "There's a special recipe in this LootBox™!", 0, 1, "lb002")
lootbox3 = LootBox("\033[32mAspiring chef's helpful LootBox™\033[0m", "If you need new Items, we've got you covered with this LootBox™!", 0, 1, "lb003")
lootbox4 = LootBox("\033[32mOld world LootBox™\033[0m", "This LootBox™ must be atleast 50 years old, at least it still works", 0, 1, "lb004")
lootbox5 = LootBox("\033[32mThe Spaghetti and Meatballs LootBox™\033[0m", "Contains the ingredients for a nice spaghetti and meatballs recipe (recipe acquired separately).", 1, 1, "lb005")

# quality 1
lootbox6 = LootBox("\033[32;1mThe exotic cooking LootBox™\033[0m", "Includes a handful of recipes from many different worlds, designed to appreciate culture", 1, 1, "lb006")
lootbox7 = LootBox("\033[32;1mInspirational item LootBox™\033[0m", "This should help you cook better.", 1, 1, "lb007")
lootbox8 = LootBox("\033[32;1mMystery draw LootBox™\033[0m", "You never know what you'll pull out next!", 1, 1, "lb008")

# quality 2
lootbox9 = LootBox("\033[34mGourmet treasure LootBox™\033[0m", "Contains recipes that has the right taste designed for a gourmet", 2, 1, "lb009")
lootbox10 = LootBox("\033[34mKitchen helper's LootBox™\033[0m", "These items should be useful for a kitchen assistant!", 2, 1, "lb010")

# adding recipes / items to lootbox lists
# items
# quality 0
Equipment.equipbox1_inv.append(equip1)
Equipment.equipbox1_inv.append(equip2)
Equipment.equipbox1_inv.append(equip3)
Equipment.equipbox1_inv.append(equip4)
Equipment.equipbox1_inv.append(equip5)
Equipment.equipbox1_inv.append(equip6)
Equipment.equipbox1_inv.append(equip7)
# quality 1
Equipment.equipbox2_inv.append(equip8)
Equipment.equipbox2_inv.append(equip9)
Equipment.equipbox2_inv.append(equip10)
Equipment.equipbox2_inv.append(equip11)
Equipment.equipbox2_inv.append(equip12)
# quality 2
Equipment.equipbox3_inv.append(equip13)
Equipment.equipbox3_inv.append(equip14)
Equipment.equipbox3_inv.append(equip15)
Equipment.equipbox3_inv.append(equip16)
Equipment.equipbox3_inv.append(equip17)

# recipes
# quality 0
Recipe.lootbox1_inv.append(recipe1)
Recipe.lootbox1_inv.append(recipe2)
Recipe.lootbox1_inv.append(recipe3)
Recipe.lootbox1_inv.append(recipe4)
Recipe.lootbox1_inv.append(recipe6)
Recipe.lootbox1_inv.append(recipe26)
# alt quality 0
Recipe.lootbox1_1_inv.append(recipe5)
Recipe.lootbox1_1_inv.append(recipe7)
Recipe.lootbox1_1_inv.append(recipe8)
Recipe.lootbox1_1_inv.append(recipe9)
Recipe.lootbox1_1_inv.append(recipe10)
Recipe.lootbox1_1_inv.append(recipe27)
# alt 2 quality 0
Recipe.lootbox1_2_inv.append(recipe11)
Recipe.lootbox1_2_inv.append(recipe12)
Recipe.lootbox1_2_inv.append(recipe13)
Recipe.lootbox1_2_inv.append(recipe14)
Recipe.lootbox1_2_inv.append(recipe15)
Recipe.lootbox1_2_inv.append(recipe28)
# lb005 unique
Recipe.lootbox1_3_inv.append(recipe5)
Recipe.lootbox1_3_inv.append(recipe8)
Recipe.lootbox1_3_inv.append(recipe9)

# quality 1
Recipe.lootbox2_inv.append(recipe16)
Recipe.lootbox2_inv.append(recipe17)
Recipe.lootbox2_inv.append(recipe18)
Recipe.lootbox2_inv.append(recipe19)
Recipe.lootbox2_inv.append(recipe29)
Recipe.lootbox2_inv.append(recipe30)
# quality 1 alt
Recipe.lootbox2_1_inv.append(recipe20)
Recipe.lootbox2_1_inv.append(recipe21)
Recipe.lootbox2_1_inv.append(recipe22)
Recipe.lootbox2_1_inv.append(recipe23)
Recipe.lootbox2_1_inv.append(recipe24)
Recipe.lootbox2_1_inv.append(recipe25)
Recipe.lootbox2_1_inv.append(recipe31)
# quality 2
Recipe.lootbox3_inv.append(recipe32)
Recipe.lootbox3_inv.append(recipe33)
Recipe.lootbox3_inv.append(recipe34)

# recipe lootboxes
# quality 0
LootBox.random_loot_inv1.append(lootbox1)
LootBox.random_loot_inv1.append(lootbox2)
LootBox.random_loot_inv1.append(lootbox4)
# quality 0, special recipe
LootBox.random_loot_inv1.append(lootbox5)
# quality 0 / 1
LootBox.random_loot_inv2.append(lootbox5)
LootBox.random_loot_inv2.append(lootbox2)
LootBox.random_loot_inv2.append(lootbox4)
LootBox.random_loot_inv2.append(lootbox6)
# quality 1 
LootBox.random_loot_inv2.append(lootbox6)
LootBox.random_loot_inv2.append(lootbox8)
# quality 2
LootBox.random_loot_inv3.append(lootbox9)

# item lootboxes
# quality 0
LootBox.random_looteq_inv1.append(lootbox3)
# quality 1
LootBox.random_looteq_inv2.append(lootbox3)
LootBox.random_looteq_inv2.append(lootbox7)
# quality 2
LootBox.random_looteq_inv3.append(lootbox10)