import os
import rooms
import utils
import time
import sys

def get_room():
    return rooms.current_room

def enter(room):
    utils.trace ("entering " + repr(room))
    rooms.current_room = room
    utils.say(get_room()["enter"])

def exit(room):
    utils.trace ("exiting " + repr(room))
    utils.say(room["exit"])

def act(cmd):
    utils.trace ("you said " + cmd)

    current_room = get_room()

    if cmd == "quit":
        lose()
        return

    if cmd == "go up":
        dir = "UP"
    elif cmd == "go down":
        dir = "DOWN"
    elif cmd == "go north":
        dir = "N"
    elif cmd == "go east":
        dir = "E"
    elif cmd == "go south":
        dir = "S"
    elif cmd == "go west":
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
    enter(to_room)

def loop():
    utils.trace("looping inside room " + repr(rooms.current_room))
    cmd = get_room().get("automate")
    if cmd:
        utils.type("> " + cmd)
    else:
        # no automate key, ask user
        cmd = input("> ")

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
