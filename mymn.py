import os
import rooms
import utils

def enter(room_name):
    room = rooms.rooms[room_name]
    print(room["enter"])

def act(cmd):
    print ("you said " + cmd)

def ask():
    cmd = input("> ")
    act(cmd)
    ask()

def begin():
    print ("WELCOME TO M Y M N")
    un = input("ENTER USERNAME\n> ")
    print ("WELCOME " + un)

    enter(rooms.current_room)
    ask()

def lose():
    say("GAME OVER")


begin()
