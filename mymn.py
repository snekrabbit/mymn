import os
import rooms
import utils
import time
import sys

def get_room(name=rooms.current_room):
    return rooms.rooms[name]

def enter(name):
    utils.say(get_room()["enter"])

def act(cmd):
    print ("you said " + cmd)
    if cmd == "quit":
        lose()

def loop():
    cmd = get_room()["automate"]
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
