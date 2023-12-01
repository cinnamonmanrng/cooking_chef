# Cooking Chef

## Minimum Requirements:
OS: Windows 10 or later / MacOS: 12.2 Monterey or later
</br>
Python: Python 3 (version 10) or later 
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
### Build 26.1 / Windows:
- Fixed: Missing lootbox from previous updates now works in this one
### Build 26 / Windows:
- Fixed: Player could get a special recipe if they had 0 items in their inventory, the code only checked for 1 or more items when it would decide whether to grant a special recipe or not.
- Fixed: Special recipe ingredients were used when player used an incorrect item on the special recipe.
- Fixed: Some of the new items could be used on any recipes when they were meant for specific recipes.
- Fixed: An issue where a player could crash the game when putting in an invalid value in the sell recipes menu.
- Fixed: Issue where the selling a recipe function would only sell the last printed recipe instead of the player's selection
- Changed: Special Recipes are enabled
- Changed: Selling a recipe now keeps you in the Sell Recipes menu instead of bringing you back to the main menu.
- Changed: Slight text adjustment for options menu.
- Changed: Application now coded and runs in Python version 12.
- Changed: Windows 8 is no longer supported as the minimum requirement, although the game can be probably be started on windows 8 or below, future updates will not consider any system behaviours for windows 8 or below.
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
</br>
Thank you for reading this and downloading my game, I hope you enjoy it :smiley:
