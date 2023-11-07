import curses
import os
import time
import sys
from config import CONFIG

def trace(msg):
    if CONFIG.get("VERBOSE"):
        print("### " + msg)

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

def say(msg, char_wait=0.01, line_wait=1):
    # os.system("say "+msg)
    last_c = None
    for c in msg:
        print (c, end="")
        sys.stdout.flush()
        if c == "\n":
            if last_c == "\n":
                continue
            else:
                nap(line_wait)
                print("")
        else:
            nap(char_wait)
        last_c = c
    print("")

def type(msg):
    nap(1.5)
    say(msg, 0.15, 0.15)
    nap(0.5)

def nap(secs):
    if CONFIG.get("FAST"):
        return
    else:
        time.sleep(secs)
