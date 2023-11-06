# Cooking Chef

## Minimum Requirements:
OS: Windows 8 or later / MacOS: 12.2 Monterey or later
</br>
Python: Python 3.8 or later 
</br>
No other requirements
</br>
## Installing Python:
In order for the game to work, your system needs to have Python 3 installed.
</br>
### To do this on Windows 10 or later, here are some steps you can use to install Python 3 on your system:
- Navigate to Microsoft Store on your PC
- Search for "Python"
- Search results should show up with different releases of python. <b>(For the best results, download the latest version of Python 3.10)</b>
- Once it has finished, you should be able to execute the game.bat file in order to start the game!
- To check what version your python is on and if it installed correctly you can follow these steps:
  - Open powershell("Terminal" in Windows 11) or Command prompt in administrator mode
  - Write "python3 --version" within the prompt
### To do this on Windows 8, Follow these steps to install Python 3:
- Navigate to [Python Downloads](https://www.python.org/downloads/windows/)
- Select your desired Python version <b>(For the best results use the latest version of Python 3.10)</b>
- Follow the installation instructions once your installer has downloaded
- To check what version your python is on and if it installed correctly you can follow these steps:
  - Open powershell or Command prompt in administrator mode
  - Write "python3 --version" within the prompt
## Issues or enquiries:
If you have any enquiries, submit them to: cookingchefgame@gmail.com or ask within [Cooking Chef Discord](https://discord.gg/CFQdynhFNd)
</br>
If you encounter issues with the game or need technical support, submit these to with a detailed error report and your python version: ccg.issues@gmail.com or join our discord: [Cooking Chef Discord](https://discord.gg/CFQdynhFNd)
</br>
## Version History:
<b>Version History only shows the 5 most recent updates, if you wish to see older updates, please refer to the patch_notes.txt file</b>
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
### Build 23 / Windows
- Changed recipe xp rewards, it now awards players with more experience when the recipe quality is better (refer to chef_call_list for details)
- Fixed a bug that would sometimes exit the program with an error when trying to go back before loading a saved game
- Player level now defines what quality lootboxes the player recieves from random_lootbox
- Changed the code in the timer function to allow for easier workability with items that have specific recipe requirements
- Changed random_lootbox code to not take boxluck and boxluck_eq as a list
- random_lootbox now gives a 65% chance for an item lootbox starting from player level 4 (this is mainly to balance the heavy recipe time requirements later in the game)
- Changed the look of the progress bar in the tutorial
- Added a 16 character limit when entering a name for player
- Added a progress bar display when cooking a recipe
- Added a mechanic that allows the player to sell recipes for 1/4th of the xp value of that recipe
### Build 22.1 / Windows
- Fixed a bug that caused all items to be unusable unless they were items specific to a specific recipe
- Added all recipe, item and lootbox instances to chef_call_list
</br>
Thank you for reading this and downloading my game, I hope you enjoy it :smiley:
