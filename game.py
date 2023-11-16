import curses
import os
import commands
import rooms
import utils
import time
import sys
import config

class Game(object):
    def __init__(self, username):
        self.username = username

    def get_room(self):
        return rooms.current_room

    def enter(self, room):
        rooms.current_room = room

        print("")
        utils.say("...", 0.2)
        utils.say("ENTER <" + room["name"] + ">")
        utils.say(self.get_room()["enter"])
        print("")
        if room.get("directions"):
            for dir, desc in room["directions"].items():
                utils.say(desc['desc'] + " (" + dir +")")

    def exit(self, room):
        exit_msg = room.get("exit")
        if exit_msg:
            utils.say(exit_msg)
        #utils.say("EXIT <" + room["name"] + ">")

    def act(self, cmd):
        utils.trace ("you said " + cmd)
        current_room = self.get_room()

        # search for a command that matches the input
        command = None
        for c in commands.ALL:
            if c.name == cmd:
                command = c
                break

        if command != None:
            c.run(self)
            return

        dir = None
        cmd = cmd.lower()
        if cmd in ["go up", "go u", "up", "u"]:
            dir = "UP"
        elif cmd in ["go down", "go d", "down", "d"]:
            dir = "DOWN"
        elif cmd in ["go north", "go n", "north", "n"]:
            dir = "N"
        elif cmd in ["go east", "go e", "east", "e"]:
            dir = "E"
        elif cmd in ["go south", "go s", "south", "s"]:
            dir = "S"
        elif cmd in ["go west", "go w", "west", "w"]:
            dir = "W"

        next_room = None
        dirs = current_room.get("directions")
        if dirs:
            next_room_dict = dirs.get(dir)
            if next_room_dict:
                next_room = rooms.rooms[next_room_dict["room"]]

        if not next_room:
            utils.say("we can't '" + cmd + "' in here")
            return

        self.move(current_room, next_room)

    def move(self, from_room, to_room):
        self.exit(from_room)
        self.enter(to_room)

    def lose(self):
        print("GAME OVER")
        sys.exit (0)

    def loop(self):
        utils.trace("looping inside room " + self.current_room["name"])
        cmd = self.current_room.get("automate")
        if cmd:
           utils.type("> " + cmd)
        else:
            print("")
            cmd = input("> ")

        print("")
        self.act(cmd)
        self.loop()

    def run(self):
        self.enter(self.current_room)
        self.loop()
