import os
import rooms
import utils
import time
import sys

def get_room(name=rooms.current_room):
    return rooms.rooms[name]

def enter(name):
    print(get_room()["enter"])

def act(cmd):
    print ("you said " + cmd)
    if cmd == "quit":
        lose()

def loop():
    cmd = get_room()["automate"]
    if cmd:
        time.sleep(1)
        print ("> ", end="")
        for c in cmd:
            print (c, end="")
            sys.stdout.flush()
            time.sleep(0.1)
        print("")    
    else:
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
    utils.say("GAME OVER")
    sys.exit (0)


begin()
