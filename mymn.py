import os
import rooms


def say(msg):
    print(msg)
    os.system("say "+msg)


def prompt_until(msg, until, tries=4):
    say(msg)
    count = 1
    while count < tries:
        count = count+1
        print("> ", end="")
        i = input()
        if i == until:
            return True
        else:
            say("INCORRECT\n"+str(tries-count)+" TRIES LEFT")
    if count == tries:
        return False

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