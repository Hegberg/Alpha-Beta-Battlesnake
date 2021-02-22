# A Complex Alpha-Beta [Battlesnake](http://play.battlesnake.com) Written in Python

This is a advanced implementation of the [Battlesnake API](https://docs.battlesnake.com/references/api). It's a great codebase for anyone struggling to program a more advanced Battlesnake with more complex algorithms.

For any people new to Battlesnake, please go to (https://github.com/battlesnakeofficial), for starting snakes and official documentation.

I encourage anyone with development questions to join the Battlesnake Slack (https://play.battlesnake.com/slack), it is a wonderful and supportive community for anyone looking to get into Battlesnake, or having any programming stuggles.

## Videos/Clips

A Tournament Victory on Dec 5th, 2020 using this snake. The tournament was using the Constrictor game mode. (Clip of Winning Game - https://clips.twitch.tv/CrepuscularBoxyFriesDoritosChip-W23LE3e_rxly6Xo7) (For the entire tournament, watch - https://www.twitch.tv/videos/826941359).

For this tournament I was able to beat the 1st highest seed (Tofu) and 5th highest seed (Neider Snake) in the "Group of Death", and beat the 3rd highest seed (SecretSnake) in the finals, along with several other snakes along the way. I was the 7th highest seed (Nebula) going into the tournament.

I actually discussed the code live with the Battlesnake platform developers if you would like the code explained (https://www.twitch.tv/videos/845302305)

## Disclaimer

This Battlesnake is not the most recent verion of my code, as I have made updates to improve the evaluation function and improve it's functionality and performance in high level games. I want this to be used as a helping hand for someone stuggling with more advanced algorithms, while not giving away all my secrets, and not being entirely optimal to discourage someone from copy-pasting this codebase and calling it a day.

### Algorithms Featured

ALPHA-BETA: This Battlesnake features an Alpha-Beta algorithm modified for Breadth First Search instead of Depth First Search (To give all levels of evaluation a more equal time, and to better utilize the amount of time given each turn), the Alpha-Beta is also modified to deal with multiple snakes acting on the same turn instead of only 1 snake acting.

FLOOD-FILL: This Battlesnake aslo features a flood fill algorithm used to determine a board evaluation mostly based off of space. While the Alpha-Beta algorithm leaves no room for improvement, this evaluation function can be improved, or replaced by an entorly different evaluation function, depending on how you think the best way of evaluating a board state is.

BOARD-GENERATOR: The last major algorithm featured in this Battlesnake is the child board creation used by Alpha-Beta. This algorithm builds all future board states (ignoring possible future food spawns). This board creation has no known bugs, and runs well, but isn't as efficient as it could be.

TEST-SUITE: This codebase also features a test suite I have set up from multiple board states encountered in previous games. If you haven't already, this is one way of implementing automated tests to make sure any changes to your code perform as expected to improve stability. There are plenty of ways of implenting automated tests with battlesnake, this is a simple one, and great for a developer of any level looking to create an intial Test-Suite of their own.

### Technologies Used

* [Python3](https://www.python.org/)
* [CherryPy](https://cherrypy.org/)

## Prerequisites

* [Battlesnake Account](https://play.battlesnake.com)
