from chef_skeleton import *

# basic exp mechanic
# Quality list:
# 0: 1 sec = 25xp
# 1: 1 sec = 35xp
# 2: 1 sec = 50xp
# 3: 1 sec = 85xp
# 4: 1 sec = 110xp
# 5: 1 sec = 160xp

# initalise recipes
recipe1 = Recipe("\033[32mSimple boiled potatoes\033[0m", 25 * 6, 0, 6, 1, "rec001")
recipe2 = Recipe("\033[32mBacon and egg\033[0m", 25 * 5, 0, 5, 1, "rec002")
recipe3 = Recipe("\033[32mMashed potatoes\033[0m", 25 * 10, 0, 10, 1, "rec003")
recipe4 = Recipe("\033[32mOvercooked tuna\033[0m", 25 * 5, 0, 5, 1, "rec004")
recipe5 = Recipe("\033[32;1mSimple boiled spaghetti\033[0m", 35 * 12, 1, 12, 1, "rec005")
recipe6 = Recipe("\033[32;1mMargherita Pizza\033[0m", 35 * 14, 1, 14, 1, "rec006")
recipe7 = Recipe("\033[32;1mVictoria sponge cake\033[0m", 35 * 10, 1, 10, 1, "rec007")
recipe8 = Recipe("\033[32;1mRoasted potatoes\033[0m", 35 * 18, 1, 18, 1, "rec008")
recipe9 = Recipe("\033[32;1mChicken stir fry\033[0m", 35 * 15, 1, 15, 1, "rec009")
recipe10 = Recipe("\033[32;1mTomato pasta\033[0m", 35 * 14, 1, 14, 1, "rec010")
recipe11 = Recipe("\033[34mPeanut butter brownies\033[0m", 50 * 20, 2, 20, 1, "rec011")
recipe12 = Recipe("\033[34mGrilled sausages\033[0m", 50 * 19, 2, 19, 1, "rec012")

# initalise equipment
equip1 = Equipment("\033[32mBeginner's oven glove\033[0m", "Increases the current recipe's XP by 50", 0, 50, 1, "eq001")
equip2 = Equipment("\033[32mCheap plastic fork\033[0m", "Decreases cooking time of any recipe by 2 seconds", 0, 2, 1, "eq002")
equip3 = Equipment("\033[32mMystery potato flavouring\033[0m", f"Decreases {recipe1.name}'s or {recipe3.name}'s cooking time by 5 seconds", 0, 5, 1, "eq003") # only for rec001 and rec003
equip4 = Equipment("\033[32;1mRegular plastic fork\033[0m", "Decreases cooking time of any recipe by 4 seconds", 1, 4, 1, "eq004")
equip5 = Equipment("\033[32;1mStarter chef's handy whisk\033[0m", "Increases the current recipe's XP by 100", 1, 100, 1, "eq005")
equip6 = Equipment("\033[32;1mPizza cutter\033[0m", f"Decrease {recipe6.name}'s cooking time by 9 seconds", 1, 9, 1, "eq006") # only for rec006
equip7 = Equipment("\033[34mAutomatic cake mixer\033[0m", f"Decreases {recipe11.name}'s cooking time by 14 seconds", 2, 14, 1, "eq007") # only for rec011
equip8 = Equipment("\033[32;1mWok pan\033[0m", f"Increases XP by 250 points for {recipe9.name}", 1, 250, 1, "eq008") # only for rec009
equip9 = Equipment("\033[34mImproved oven fan", "Decreases cooking time for any recipe by 10 seconds", 2, 10, 1, "eq009")
equip10 = Equipment("\033[34mMagical recipe note", "Allows you to re-cook the recently cooked recipe", 2, 1, 1, "eq010")

# initalise lootbox
lootbox1 = LootBox("\033[32mJunior chef's LootBox™\033[0m", "A wonderful start for every chef in Emerald's Restaurants™", 0, 1, "lb001")
lootbox2 = LootBox("\033[32mFirst edition LootBox™\033[0m", "Like the name describes, quite old and out of date, but will work for now!", 0, 1, "lb002")
lootbox3 = LootBox("\033[32mAspiring chef's helpful LootBox™\033[0m", "If you need new Items, we've got you covered with this LootBox™!", 0, 1, "lb003")
lootbox4 = LootBox("\033[32;1mOutdated helpful LootBox™\033[0m", "Better Items can be found here!", 1, 1, "lb004")
lootbox5 = LootBox("\033[32;1mWeekly shipment LootBox™\033[0m", "Shipped to the restaurant every week. Expect fresher ingredients.", 1, 1, "lb005")
lootbox6 = LootBox("\033[34mSmart Chef's LootBox™\033[0m", "Every smart chef has one of these LootBoxes™!", 2, 1, "lb006")

# adding items to lootbox inventories and lootboxes to player inventory
# quality 0
Equipment.equipbox1_inv.append(equip1)
Equipment.equipbox1_inv.append(equip2)
Equipment.equipbox1_inv.append(equip3)
# quality 1
Equipment.equipbox2_inv.append(equip4)
Equipment.equipbox2_inv.append(equip5)
Equipment.equipbox2_inv.append(equip6)
Equipment.equipbox2_inv.append(equip8)
# quality 2
Equipment.equipbox3_inv.append(equip7)
Equipment.equipbox3_inv.append(equip9)
Equipment.equipbox3_inv.append(equip10)

# quality 0
Recipe.lootbox1_inv.append(recipe1)
Recipe.lootbox1_inv.append(recipe2)
Recipe.lootbox1_inv.append(recipe3)
Recipe.lootbox1_inv.append(recipe4)
# quality 1
Recipe.lootbox2_inv.append(recipe5)
Recipe.lootbox2_inv.append(recipe6)
Recipe.lootbox2_inv.append(recipe7)
Recipe.lootbox2_inv.append(recipe8)
Recipe.lootbox2_inv.append(recipe9)
Recipe.lootbox2_inv.append(recipe10)
# quality 2
Recipe.lootbox3_inv.append(recipe11)
Recipe.lootbox3_inv.append(recipe12)

# quality 0
LootBox.random_loot_inv1.append(lootbox1)
LootBox.random_loot_inv1.append(lootbox2)
LootBox.random_looteq_inv1.append(lootbox3)
# quality 1
LootBox.random_looteq_inv2.append(lootbox4)
LootBox.random_loot_inv2.append(lootbox2)
LootBox.random_loot_inv2.append(lootbox5)
# quality 2
LootBox.random_loot_inv3.append(lootbox6)