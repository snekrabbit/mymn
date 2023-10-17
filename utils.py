import os

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
