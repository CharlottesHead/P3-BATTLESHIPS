# Hello Code Institue

This is my submission for the third portfolio project. It's fundamentally a battleship game with some slight alterations to keep up the tempo and enhance replay ability.

## Table of Contents
- [General Info](#general-information)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Screenshots](#screenshots)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)
- [Project Status](#project-status)
- [Responsiveness](#project-status)
- [Room for Improvement](#room-for-improvement)
- [Acknowledgements](#acknowledgements)

## General Information
Battleships is a stratigic boardgame that has a long historic origin but is mostly know for the table top version made by board game company, Mitlon Bradley. It pits two players against each other trying to guess the location of their battleships on a hidden grid. This version however will be player vs AI.

## Technologies Used
- Tech 1 - Python
- Tech 2 - html
- Tech 3 - JavaScript

## Features
List the ready features here:
- 8 * 8 grid.
- 5 ship placements of varying length and orientation.
- Realtime commentary.


## Screenshots
![Screenshot](assets/BATTLESHIP-1.png) ![Screenshot](assets/BATTLESHIP-2.png) ![Screenshot](assets/BATTLESHIP-3.png) ![Screenshot](assets/BATTLESHIP-5.png) 
![Screenshot](assets/BATTLESHIP-CODE.png) 

## Usage

Firstly, players are asked to place their battleships. The grid is 8 * 8 and each player has 5 ships ranging in length from 2 to 5 spaces long. Code has been written to prevent the player from placing ships overlapping each other.

Once ships are placed the main gameplay loop begins.

The player is given frequent prompts and realtime commentary to let them know exactly what is happening.

As it is the game is a race for the first to achieve 6 hits. I felt this to be an improvement over the standard formula, increasing the tempo of the game and encouraging replays while still being challenging.

## Testing

I have passed the code through a pep8 linter and there are no problems.

![ScreenShot](assets/PEP8.png)

I have tested it extensively by giving an incorrect command, imputing coordinates off grid and shooting the same location twice and at the time of writing this I can confirm there are no bugs.

The website has been tested on multiple browsers on different OS's with no issues found.
It has also been tested on Android and iPhone devices, also clear of issues.

### Development Testing

During the development process, It was tested in the following ways:-

 - Manually testing each element by running it within VSCode.
 
 - Passing it through PEP8 without any issues
   
 - Inviting friends to test and provide feedback.

## Deployment

### Heroku

The project was deployed on Heroku at https://p3-battleship.herokuapp.com/

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on
our GitHub account to view and/or make changes without affecting the original
repository by using the following steps...

1. Log in to GitHub and locate the [GitHub
   Repository](https://github.com/CharlottesHead/P3-BATTLESHIPS)
1. At the top of the Repository (not top of page) just above the "Settings"
   Button on the menu, locate the "Fork" Button.
1. Click the button (not the number to the right) and you should now have a copy
   of the original repository in your GitHub account.

## Credits
https://www.pythoncheatsheet.org/

https://docs.python.org/3/tutorial/

https://en.wikipedia.org/wiki/Under_Siege
