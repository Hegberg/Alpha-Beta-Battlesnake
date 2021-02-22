import os
import random

import cherrypy
from algorithms.get_move import get_move
from algorithms.puns import get_random_pun

"""
This is a Battlesnake server written in Python.
Instructions for simple Battlesnake server see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""


class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "Whitishmeteor",
            "color": "#000000",
            "head": "ski",
            "tail": "bolt",
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        #data = cherrypy.request.json

        #print("START")
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        data = cherrypy.request.json

        #print(data)

        # Choose a random direction to move in
        #possible_moves = ["up", "down", "left", "right"]
        #move = random.choice(possible_moves)

        move = get_move(data)
        pun = get_random_pun()

        #print(f"MOVE: {move}")
        return {"move": move, "shout": pun}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        #data = cherrypy.request.json

        #print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    #cherrypy.config.update({"server.socket_host": "192.168.1.65"})
    cherrypy.config.update({"server.socket_host": "10.0.0.4"})
    #cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
