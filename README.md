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
### Build 22 / Windows
- Replaced some of the get rating and get level functions in chef_skeleton to be dictionaries as this makes it easier to add and remove levels and ratings 
- Added a feature to chef_main check whether the user has the required modules installed on starting the application (also in chef_game to check for pygame) 
- Removed unnecessary double imports
- Fixed a slight bug with lootboxes when trying to run open_lootbox function when the player's lootbox inventory is empty which did not give you any prompts that the inventory is empty
- Fixed an issue with the keyboard module not importing properly
- Changed the look of max level to only include the experience instead of also listing next_level and max_xp
- Created a start for the pygame application
- Added new recipes, lootboxes and items
- Optimised timer function to have a dictionary to check for recipe_id instead of if statements in chef_func
- Massively improved on code in chef_func, made it much easier to work with and read
- Removed debugging statements
- Fixed a bug that caused lootboxes to only provide the same item over and over again
- Added a rating display for save slot 2 and 3 that was missing before
- Added a 41% chance to get a mythical lootbox at recipe rating 5
### Build 1.1 MacOS
- Created a version for MacOS
  - Tutorial cannot be played as keyboard module does not work properly within MacOS as of yet
</br>
Thank you for reading this and downloading my game, I hope you enjoy it :smiley:
