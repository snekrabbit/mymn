import os
import time
import sys

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
        if c == "\n" and last_c != "\n":
            time.sleep(line_wait)
        else:
            time.sleep(char_wait)
        last_c = c
    print("") 

def type(msg):
    time.sleep(1)
    say(msg, 0.15, 0.15)  
    time.sleep(0.5)


