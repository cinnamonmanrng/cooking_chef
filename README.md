# Cooking Chef

## Minimum Requirements:
OS: Windows 8 or later / MacOS: 12.2 Monterey or later
</br>
Python: Python 3.8 or later 
</br>
No other requirements
</br>
## Installing Python:
Because of the change to a dedicated installer and exe file in Build 25, the game should no longer require you to install python 3 manually.
## Issues or enquiries:
If you have any enquiries, submit them to: cookingchefgame@gmail.com or ask within [Cooking Chef Discord](https://discord.gg/CFQdynhFNd)
</br>
If you encounter issues with the game or need technical support, submit these to with all the log files to your report and your python version: ccg.issues@gmail.com or join our discord: [Cooking Chef Discord](https://discord.gg/CFQdynhFNd)
</br>
## Version History:
<b>Version History only shows the 5 most recent updates, if you wish to see older updates, please refer to the patch_notes.txt file</b>
### Build 25.1 / Windows:
- Fixed: Issue where chefgame.log would give a permission error whenever the logging function would try to write to that file. The exception was previously unhandled so that's why the error popped up.
- Fixed: Visual colour bug when opening options menu
### Build 25 / Windows:
- Added: There is now an installer that installs the game and python dependencies needed by the game for the user.
- Fixed: Issue where you could cause an IndexError by picking a number out of the range of options when choosing what LootBox to open.
- Fixed: Issue where in some cases after the player gains a rating higher than 0 the game would set the random item box list to be empty so it cannot be accessed by random lootbox and would crash the game.
- Fixed: A small bug where if the player got to ratings 1 - 3 - 5 - 7 - 9, the game would give you the same lootboxes over and over again until the next rating.
- Changed: Special Recipes are temporarily removed due to 3 different issues with one special recipe, will be added back when I can figure out a fix for it.
- Current issues known and fixed in next update: 
1. Special recipes get given to players even when the player has no more recipes to cook, the best thing you can do to counteract this is to sell that recipe and claim the inventory empty lootbox from the main menu (you will see it once your inventory is empty of lootboxes)
2. Special recipes have their ingredients count reduced regardless of whether it gets cooked or not, so when you use an item that cannot be used on a special recipe, you will also lose the ingredients used for that recipe, this can be annoying but the easiest way to counteract this is to make sure you don't use items that can only be used on specific recipes on the currently available special recipe (spaghetti and meatballs in tomato sauce)
3. Also a weird small bug with special recipes where if you gain a special recipe it for some reason doesn't let you open lootboxes until you sell that special recipe. working on a fix for next build.
### Build 24.1 / Windows
- Changed: Save files will now be generated and stored in "Saves" folder inside the main game folder, creates less clutter overall.
- Changed: Cleared some unused files in the game folder
- Fixed: Visual bug when trying to delete a save file from an empty slot where the notification colour of the message "Save file slot (2 or 3) is empty" would fill every bit of text with the same colour.
- Added: Logging system that stores log files in "Logs" folder, creates log entries of specific events and errors that are used for reference in case there is a bug needing a fix.
- Added: More recipes, items and lootboxes for qualities 0 to 2
### Build 24 / Windows
- Changed: player's status will now be printed through the main function opposed to using the level up function, this avoids double printing it after finishing a recipe
- Changed: recipe progress bar now prints with a different symbol
- Changed: using an item on a recipe now correctly displays "item" instead of the script term "equipment"
- Changed: Older recipes, items and lootboxes have now been replaced by new ones
- Changed: selling a recipe now gives the player 1/5 of the xp amount instead of 1/4
- Changed: random lootboxes chances for an item lootbox now change based on player level, a player below level 2 has a 50% chance to recieve an item lootbox, from level 2 to level 4 the chance increases to 65%, level 4 to 6 chance is 75%, level 6 to 8 chance is 80% and above level 8 chance is 99%
- Changed: Levels 1 - 4 now have different xp requirements, level 1 starts at 2000 xp, level 2 at 4500, level 3 at 7000 and level 4 at 12500
- Added: New recipes, items and lootboxes with a wider variety of recipes and items from different lootboxes
- Added: Recipes that require one or more other recipes to be cooked beforehand, these recipes will also reward the player with more experience but they will also take more time
- Added: Option to claim a LootBox™ in the game menu ("main" function) when the player has no more recipes and no lootboxes to open
- Fixed: Issue where selling a recipe would give you a decimal number from the xp amount
- Fixed: Player will no longer be given a special recipe when they have no other recipes in their inventory
- Special Recipe: Even though you can select an item before cooking a special recipe, it will not use the item if you do not have the correct ingredients cooked to cook that recipe
### Build 3 / MacOS
- Updated MacOS version to align with the windows version of the game, the changes are the same so the patch notes for the windows version are inclusive of the MacOS version.
</br>
Thank you for reading this and downloading my game, I hope you enjoy it :smiley:
