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
    if cmd == "quit":
        lose()
    elif cmd == "go up":
        current_room = get_room()
        next_room_name = current_room["directions"]["UP"]["room"]
        next_room = rooms.rooms[next_room_name]
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
