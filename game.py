import os
import time
import sys

import commands
import rooms

from term import Term

class Game(object):
    def __init__(self, term, begin_room):
        self.term = term

        begin_room = begin_room or "the_plane"
        self.current_room = None

        if not rooms.rooms.get(begin_room):
            raise Exception("unknown starting room: " + repr(begin_room))
        else:
            self.current_room = rooms.rooms[begin_room]

    def enter(self, room):
        self.current_room = room

        self.term.println()
        self.term.say("<" + room["name"] + ">")
        self.term.say(self.current_room["enter"])
        self.term.println()
        if room.get("directions"):
            for dir, desc in room["directions"].items():
                self.term.say(desc['desc'] + " (" + dir +")")

    def exit(self, room):
        exit_msg = room.get("exit")
        if exit_msg:
            self.term.say(exit_msg)
        #self.term.say("EXIT <" + room["name"] + ">")

    def act(self, cmd):
        self.term.trace ("you said " + cmd)

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
        dirs = self.current_room.get("directions")
        if dirs:
            next_room_dict = dirs.get(dir)
            if next_room_dict:
                next_room_name = next_room_dict["room"]
                next_room = rooms.rooms[next_room_name]
                action = next_room_dict.get("action")
                if action:
                    self.term.say(action)


        if not next_room:
            self.term.say("we can't '" + cmd + "' in here")
            return

        self.move(self.current_room, next_room)

    def move(self, from_room, to_room):
        self.exit(from_room)
        self.enter(to_room)

    def lose(self):
        self.term.print("GAME OVER")
        sys.exit (0) #raise Lose

    def loop(self):
        self.term.trace("looping inside room " + self.current_room["name"])
        cmd = self.current_room.get("automate")
        if cmd:
            self.term.type("> " + cmd)
        else:
            self.term.println()
            cmd = self.term.input("> ")

        self.term.println()
        self.act(cmd)
        self.loop()

    def run(self):
        self.term.println("WELCOME TO M Y M N")
        # self.term.println("ENTER USERNAME")
        # self.username = self.term.input("> ")
        # self.term.println("WELCOME " + self.username)

        self.enter(self.current_room)
        self.loop()
