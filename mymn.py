import os
import rooms
import utils
import time
import sys

def get_room():
    return rooms.current_room

def enter(room):
    rooms.current_room = room

    print("")
    utils.say("ENTER <" + room["name"] + ">")
    utils.say(get_room()["enter"])
    print("")
    if room.get("directions"):
        for dir, desc in room["directions"].items():
            utils.say(desc['desc'] + " (" + dir +")")

def exit(room):
    exit_msg = room.get("exit")
    if exit_msg:
        utils.say(exit_msg)
    #utils.say("EXIT <" + room["name"] + ">")

def act(cmd):
    utils.trace ("you said " + cmd)
    current_room = get_room()

    if cmd == "quit":
        lose()
        return

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

    move(current_room, next_room)

def move(from_room, to_room):
    exit(from_room)
    utils.say("...", 0.2)
    enter(to_room)

def loop():
    utils.trace("looping inside room " + rooms.current_room["name"])
    #cmd = get_room().get("automate")
    #if cmd:
    #    utils.type("> " + cmd)
    #else:
    # no automate key, ask user
    print("")
    cmd = input("> ")

    print("")
    act(cmd)
    loop()

def begin():
    print ("WELCOME TO M Y M N")
    un = input("ENTER USERNAME\n> ")
    print ("WELCOME " + un)

    enter(rooms.current_room)
    loop()

def lose():
    print("GAME OVER")
    sys.exit (0)


begin()
