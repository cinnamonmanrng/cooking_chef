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
### Build 21.3
- Fixed a ValueError caused by not selecting an option within the browsing storage option
- Decreased double lootbox chance to 25%
- Added a new lootbox with new items and recipes
### Build 21.2
- Fixed a problem with timer permanently saving decreases in cooking times and increases in xp value
### Build 21.1
- Fixed a gamebreaking issue with the timer mechanic
</br>
Thank you for reading this and downloading my game, I hope you enjoy it :smiley:
